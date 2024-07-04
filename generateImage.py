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
client = openai.OpenAI()

def generate_visual_prompt(content):
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a helpful assistant that generates descriptive and visually engaging prompts for creating images with DALL-E."},
            {"role": "user", "content": f"Generate a detailed and visually focused prompt for DALL-E to create an image based on the following blog content, emphasizing simplicity and clarity:\n\n{content}"}
        ]

    # messages=[
    #     {"role": "system", "content": "You are a helpful assistant that generates descriptive and visually engaging prompts for creating images with DALL-E."},
    #     {"role": "user", "content": f"Generate a detailed and descriptive prompt for DALL-E to create an image based on the following blog content:\n\n{content}"}
    # ]
    )

    summarized_text = completion.choices[0].message.content

    return summarized_text

def generate_image(prompt):
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
    path_blog = filename_blog
    output_path = filename_blog.replace('.md', '.png')

    content_blog = read_blogpost(path_blog)
    summarized_text = generate_visual_prompt(content_blog)

    prompt = "" + summarized_text
    print("prompt for Dall-e: \n\n" + prompt)
    image_url = generate_image(prompt)
    print(image_url)

    save_image(image_url, output_path)

    return output_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate an image for a blog post.')
    parser.add_argument('filename_blog', type=str, help='The filename of the blog post')

    args = parser.parse_args()

    generate_image_from_blogpost(output_folder, args.filename_blog)

