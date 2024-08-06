# Personalized text-to-image Models -- Day 4

Day 4! Let's try to finish the overview today and try to implement 1 solution.

## Overview Research

Might be interesting to use:

- [Make-A-Story: Visual Memory Conditioned Consistent Story Generation](https://arxiv.org/pdf/2211.13319)
  - May 2023
  - [Code available](https://github.com/ubc-vision/Make-A-Story)
- [FastComposer: Tuning-Free Multi-Subject Image
  Generation with Localized Attention](https://arxiv.org/pdf/2305.10431v2) - May 2023 - To integrate multiple personal people in the same image.

### Summarized Usefulness in One Sentence

1. **[StoryGAN: A Sequential Conditional GAN for Story Visualization](https://arxiv.org/abs/1812.02784) (April 2019)**:
   Provides foundational insights into achieving consistency and logical progression in story visualization.

2. **[StoryDALL-E: Adapting Pretrained Text-to-Image Transformers for Story Continuation](https://arxiv.org/abs/2209.06192) (September 2022)**:
   Offers strategies to adapt powerful pretrained models for generating coherent visual story sequences.

3. **[Make-A-Story: Visual Memory Conditioned Consistent Story Generation](https://arxiv.org/pdf/2211.13319) (May 2023)**:
   Utilizes visual memory to ensure consistent image generation across story frames.

4. **[StoryGPT-V: Large Language Models as Consistent Story Visualizers](https://arxiv.org/abs/2312.02252) (December 2023)**:
   Employs large language models to transform text into coherent visual frames, perfectly aligning with your objectives.

5. **[StoryGen -- Intelligent Grimm - Open-ended Visual Storytelling via Latent Diffusion Models](https://haoningwu3639.github.io/StoryGen_Webpage/) (March 2024)**:
   Uses latent diffusion models to maintain narrative coherence in visual storytelling.

6. **[SEED-Story: Multimodal Long Story Generation with Large Language Model](https://arxiv.org/pdf/2407.08683v1) (July 2024)**:
   Combines multimodal story generation with the latest advancements in large language models for comprehensive story creation.

# Implementation of Seed-Story

## Random thoughts during the process

- Damn, a lot of data to download!
- had to add these to the requirements file / install these: `pip install torch
transformers
einops 
transformers_stream_generator
pillow
torchvision
accelerate
hydra-core
pyrootutils
diffusers`

and `C++` and `NVIDEA CUDA`
