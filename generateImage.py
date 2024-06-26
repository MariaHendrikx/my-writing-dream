import openai
import os
from dotenv import load_dotenv, find_dotenv
import argparse

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

# Initialize the output folder
output_folder = 'blogs'

def generate_image(prompt):
    client = openai.OpenAI()

    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    image_url = response.data[0].url

    return image_url

def read_blogpost(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def save_image(image_url, file_path):
    import requests
    response = requests.get(image_url)
    with open(file_path, 'wb') as file:
        file.write(response.content)

def generate_image_from_blogpost(output_folder, filename_blog):
    path_blog = os.path.join(output_folder, filename_blog)
    output_path = os.path.join(output_folder, filename_blog.replace('.md', '.png'))

    content_blog = read_blogpost(path_blog)
    prompt = "Generate an image-banner for the following blogpost, image should contain no texts or words: " + content_blog

    image_url = generate_image(prompt)
    print(image_url)

    save_image(image_url, output_path)

    return output_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate an image for a blog post.')
    parser.add_argument('filename_blog', type=str, help='The filename of the blog post')

    args = parser.parse_args()

    generate_image_from_blogpost(output_folder, args.filename_blog)

