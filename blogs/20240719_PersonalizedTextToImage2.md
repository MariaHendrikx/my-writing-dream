# Personalized text-to-image Models 2

So, yesterday I started searching about personalized text-to-image models. And today I am continuing this search. I was thinking to first get an overview of what exists and what methods I should try, and then just try to implement something. In this blog I will note my findings.

## Overview Research

Might be interesting to use:
- [StoryGAN: A Sequential Conditional GAN for Story Visualization](https://arxiv.org/abs/1812.02784)
    - Apr 2019  
    - = story-to-image-sequence generation model
    - They are stating the exact problem I am trying to solve as well: 
    There are two main challenges in this task. First, `the sequence of images must consistently and coherently depict the whole story` and `sequentially applying text-to-image methods to a story will not generate a coherent image sequence, failing on the story visualization task`
    The second challenge is `how to display the logic of the storyline`. Specifically, the appearance of objects and the layout in the background must evolve in a coherent way as the story progresses.
    - Seed-story said: The domain of story visualization, initially pioneered by StoryGAN
- [StoryDALL-E: Adapting Pretrained Text-to-Image Transformers for Story Continuation](https://arxiv.org/abs/2209.06192)
    - Sep 2022
-  StoryGANc
- [StoryGPT-V: Large Language Models as Consistent Story Visualizers](https://arxiv.org/abs/2312.02252)
    - Dec 2023
    - `he objective of story visualization is to transform a textual narrative, composed of a series of N descriptions S1, ...SN , into a sequence of corresponding visual frames I1, ..., IN that illustrate the story.` They explain the exact thing I want to accomplish.
    - it has [code](https://xiaoqian-shen.github.io/StoryGPT-V/)
- [SEED-Story: Multimodal Long Story Generation with Large Language Model](https://arxiv.org/pdf/2407.08683v1)
    - Jul 2024
    - lol. This was exactly what I had in mind to make.

## Different approaches
### My Approach
- Use dreambooth way: Upload a picture of yourself, use this picture of yourself as "character" and c all it ID_1 and describe the context of it.
- When new character is introduced, train it to also know this character as ID_2 and describe the context
- Interested in using Small Language Models

### Approach 2
- 

## Terminology

- Text2Gist is an automated process or tool designed to condense longer pieces of text into shorter summaries while retaining the key information and overall meaning. It typically uses natural language processing (NLP) techniques to analyze and extract the most relevant content from the original text.



## Explanations by ChatGPT

```
Can you explain the related work of StoryGAN?
```
Certainly! The text you provided discusses the evolution of story visualization, a domain that focuses on generating sequences of images that narrate a story based on given text descriptions. It contrasts this with the newer approach of multimodal story generation, which not only generates images but also continues the narrative with additional text.

### Key Points Explained

1. **Story Visualization**:
   - **Pioneering Work - StoryGAN**: This was one of the first models in the domain, using sequential conditional Generative Adversarial Networks (GANs) with dual discriminators to improve both the narrative coherence (the flow of the story) and visual fidelity (the quality of the images).
   
   - **Advancements**:
     - **DuCoStoryGAN and VLCStoryGAN**: These models incorporated video captioning techniques to better align the generated visuals with the story's text descriptions, enhancing the overall coherence between text and images.
     - **Diffusion Models**: Newer models adopted diffusion techniques to improve the quality of generated images. For instance:
       - **StoryDALL-E**: Uses pre-trained models with cross-attention layers to ensure the story progresses logically from one image to the next.
       - **AR-LDM and Story-LDM**: Introduced auto-regressive diffusion models that generate coherent sequences of images, ensuring a smooth narrative flow.
       - **TaleCrafter**: Utilizes LoRA (Low-Rank Adaptation) and optimization techniques to maintain consistent characters throughout the story.
     - **Intelligent Grimm**: Proposed an open-ended story visualization approach using an auto-regressive model called StoryGen, which includes a vision-language context module to enhance character consistency throughout the story.

2. **Multimodal Story Generation**:
   - This newer approach goes beyond simply generating images based on text. It also continues the story by generating additional text and corresponding images, creating a richer and more engaging narrative experience.
   - **Difference from Story Visualization**: While story visualization focuses primarily on generating image sequences that tell a story, multimodal story generation integrates both text and image generation. This allows for a more dynamic and immersive storytelling process where the narrative can evolve with both new images and new textual content.

### Summary

- **Story Visualization**: Focuses on creating sequences of images to narrate a story based on given text descriptions. It has evolved from simple GAN-based models to more complex systems using video captioning and diffusion models to enhance image quality and narrative flow.
- **Multimodal Story Generation**: Extends the concept of story visualization by generating not only images but also continuing the text of the story. This approach provides a more comprehensive storytelling experience by combining visual and textual narrative elements.

Overall, while story visualization is about creating coherent visual sequences from text, multimodal story generation aims to create a holistic narrative experience with both visual and textual elements progressing together.