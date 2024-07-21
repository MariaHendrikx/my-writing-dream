# Personalized text-to-image Models

So, I am creating a new application, ToddlerStories, that creates personalized stories for toddlers with images. Creating the text is easy these days, but I want the images to be consistent. When using Dall-E, it is incredibly difficult to get this consistency. So, I need another solution. I then remembered a course I took at DTU, Biometric Systems, where I learned about personalized text-to-image models. My abstract for that project was as follows:
```
This term paper investigates the use of personalized text-to-image models for face age manipulation using machine learning. The goal is to simulate facial appearances under different age conditions and assess their impact on face recognition performance. To achieve this result, person- alized text-to-image models will be researched and the models Dreambooth in combination with Stable Diffusion will then be used to generate a new dataset with age-modified facial images. The result will then be evaluated with an open-source face recognition system, MagFace. Finally, the results will be interpret with Biometric performance evaluation.
```

So important links:
- [Dreambooth](https://dreambooth.github.io/)
- [Article about Dreambooth by NVIDEA](https://developer.nvidia.com/blog/generative-ai-research-spotlight-personalizing-text-to-image-models/)

Also, there was this hype of "High school" pictures a while ago, where people upload a picture of themselves and then some typical highschool pictures would be generated with their face. So.. I can use this mechanism to create an avatar, and then use this avatar for different scenarios, thus creating consistency.

# My research

... I might try to do it with Dreambooth, LoRa, Perfusion and Textual Inversion

Might be interesting to use:
- [AnimateDiff: Animate Your Personalized Text-to-Image Diffusion Models without Specific Tuning](https://arxiv.org/pdf/2307.04725)
    - more about animating certain parts in an image. Might be interesting for future work, but not atm.
- [Text2Cinemagraph](https://text2cinemagraph.github.io/website/)
    - Seems to be the same as AnimateDiff: Animating pictures, not what we are searching for atm, maybe for future work.
- [Low-Rank Adaptation (LoRA)](https://arxiv.org/pdf/2106.09685)
- GAN technology (Artbreeder uses GAN technology to allow users to create and evolve images, including character portraits and landscapes.)
- Runway ML provides a platform for running machine learning models, including image generation models like StyleGAN and BigGAN.
- [HyperDreamBooth: HyperNetworks for Fast Personalization of Text-to-Image Models](https://hyperdreambooth.github.io/)
    - Seems to be more about character in a picture and modifying it, but not really about image-story continuation. Could be used, for the "my own approach"
- [SEED-Story: Multimodal Long Story Generation with Large Language Model](https://arxiv.org/pdf/2407.08683v1)
    - lol. This was exactly what I had in mind to make XD I have atm a method in my mind to do it, but I will just assume they are better at it? Might test both methods.
- [SEED-X: Multimodal Models with Unified Multi-granularity Comprehension and Generation](https://github.com/AILab-CVC/SEED-X)
    - Seed-Story is based on this.

# Terminology Learned
- LoRA (Low-Rank Adaptation) is a technique used to efficiently fine-tune large language models by adjusting only a low-rank subset of their parameters, significantly reducing the computational cost and memory requirements. This approach allows for faster training and adaptation of models to new tasks with limited data.

- Interleaved image-text refers to the integration of images and text within the same document or content, arranged in a way that alternates between them. This technique enhances comprehension and retention by providing visual context to textual information. It's commonly used in educational materials, websites, and multimedia presentations.






