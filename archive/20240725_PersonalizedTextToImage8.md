# Day 8

So.. Today I am going to implement models that need a max of 8vram.


- [LoRa](https://arxiv.org/pdf/2106.09685)
- [HyperDreamBooth](https://openaccess.thecvf.com/content/CVPR2024/papers/Ruiz_HyperDreamBooth_HyperNetworks_for_Fast_Personalization_of_Text-to-Image_Models_CVPR_2024_paper.pdf)

So... I was reading some papers and then I realized I don't really understand everything and how machine learning is related to generating images. So, today is going to be about recreating something like stable diffusion.

Stable Diffusion is a type of latent diffusion model used for generating high-quality images. It operates by iteratively refining a noisy image into a desired output. Here's an overview of how it works behind the scenes in Python:

# The explanation of Stable Diffusion

### 1. Preprocessing and Noise Addition
- **Input Image**: Start with an input image (or a latent vector if generating from scratch).
- **Noise Addition**: Gradually add Gaussian noise to the image over several steps to reach a nearly pure noise image. This creates a sequence of increasingly noisy images.

### 2. Diffusion Process
- **Forward Process (Encoding)**: Define a forward process that adds noise to the input image. This is modeled as a Markov chain where each step slightly corrupts the image with noise.
- **Reverse Process (Decoding)**: Train a neural network to reverse the process, i.e., to predict the denoised image from a noisy one. This network is often a U-Net, which is effective for image-to-image translation tasks.

### 3. Model Architecture
- **U-Net Architecture**: The model architecture typically used is a U-Net, which has an encoder-decoder structure with skip connections that help in preserving high-resolution features.
- **Latent Space**: Images are often mapped to a latent space using an encoder. The diffusion process operates in this latent space, which helps in managing the complexity and size of the data.

### 4. Training
- **Objective Function**: The model is trained to minimize the difference between the predicted denoised image and the original image at each step of the diffusion process. This is usually done using a variant of the mean squared error (MSE) loss.
- **Noise Schedule**: Define a noise schedule that determines how much noise to add at each step. This schedule can be linear, cosine, or learned during training.

### 5. Generation
- **Sampling**: To generate a new image, start with a random noise image and iteratively apply the trained reverse process to denoise it step by step until a clean image is obtained.

### 6. Implementation in Python
Here's a simplified example of how the core concepts might be implemented in Python using PyTorch:

```python
import torch
import torch.nn as nn
import torch.optim as optim

# Define a simple U-Net architecture
class UNet(nn.Module):
    def __init__(self):
        super(UNet, self).__init__()
        self.encoder = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=4, stride=2, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(64, 128, kernel_size=4, stride=2, padding=1),
            nn.ReLU(inplace=True)
        )
        self.decoder = nn.Sequential(
            nn.ConvTranspose2d(128, 64, kernel_size=4, stride=2, padding1),
            nn.ReLU(inplace=True),
            nn.ConvTranspose2d(64, 3, kernel_size=4, stride=2, padding=1),
            nn.Tanh()
        )
    
    def forward(self, x):
        x = self.encoder(x)
        x = self.decoder(x)
        return x

# Forward diffusion process
def add_noise(img, t):
    noise = torch.randn_like(img)
    return img * (1 - t) + noise * t

# Reverse diffusion process (denoising step)
def denoise(model, noisy_img, t):
    return model(noisy_img) * t + noisy_img * (1 - t)

# Training loop
def train(model, dataloader, epochs, lr=1e-4):
    optimizer = optim.Adam(model.parameters(), lr=lr)
    criterion = nn.MSELoss()
    for epoch in range(epochs):
        for imgs in dataloader:
            t = torch.rand(1).item()  # Random noise level
            noisy_imgs = add_noise(imgs, t)
            denoised_imgs = denoise(model, noisy_imgs, t)
            loss = criterion(denoised_imgs, imgs)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        print(f"Epoch {epoch+1}/{epochs}, Loss: {loss.item()}")

# Example usage with random data
model = UNet()
dataloader = [torch.randn(8, 3, 64, 64) for _ in range(100)]  # Replace with real dataloader
train(model, dataloader, epochs=10)
```

### Key Components Explained
- **UNet**: A simple U-Net architecture for denoising.
- **add_noise**: Function to add Gaussian noise to the images.
- **denoise**: Function to denoise images using the trained model.
- **train**: Training loop to optimize the model.

In practice, the actual implementation of Stable Diffusion models is more complex and involves additional components like attention mechanisms, advanced loss functions, and sophisticated noise schedules. Libraries like Hugging Face's Diffusers provide a comprehensive framework for working with such models.