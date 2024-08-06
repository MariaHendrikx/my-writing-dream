# Day 7

Waw.. already working 1 week on it, and not really achieving a lot. I did know I would do a while on it though.

So... I almost got to run DreamBooth, but I have the same problem as I had a year ago: I need 24 VRAM to run it. Which brings me to CoPilot to ask: "what has published after dreambooth that needs less vram?"

And the answer is .... 

```
Since Dreambooth, there have been several advancements aimed at reducing VRAM requirements for similar tasks. One notable development is the use of Low-Rank Adaptation (LoRA), which allows for Dreambooth training on GPUs with as little as 6GB of VRAM1. This method leverages techniques like xFormers and bitsandbytes to optimize memory usage and improve efficiency12.
```

So... `LoRA` .. A term I have been seeing a lot lately! Let's figure out what it is and how to apply it :D

`"LoRA can reduce the number of trainable parameters by 10,000 times and the
GPU memory requirement by 3 times."`

My friend also suggeest ControlNet