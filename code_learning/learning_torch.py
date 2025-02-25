import torch

# ------------------------------
# 1. Define Input and Output
# ------------------------------
# Let's say we have 3 samples with 2 features each
X = torch.tensor([[1.0, 2.0],
                  [2.0, 3.0],
                  [3.0, 4.0]])

# Outputs for each sample
y = torch.tensor([[5.0],
                  [8.0],
                  [11.0]])

# ------------------------------
# 2. Initialize Weights and Biases
# ------------------------------
# For a simple linear model y = Wx + b
W = torch.randn((1, 2), requires_grad=True)  # Weight matrix (1x2)
b = torch.randn((1), requires_grad=True)     # Bias term

# ------------------------------
# 3. Forward Pass = Matrix Multiplication
# ------------------------------
# Forward pass = Multiply input by weights and add bias
y_pred = torch.matmul(X, W.T) + b  # X(3x2) * W.T(2x1) = (3x1)

print("Predictions before training:", y_pred)

# ------------------------------
# 4. Define Loss Function (Mean Squared Error)
# ------------------------------
loss = torch.mean((y_pred - y) ** 2)  # MSE = (y_pred - y)^2 / n

print("Initial loss:", loss.item())

# ------------------------------
# 5. Backward Pass = Compute Gradients
# ------------------------------
loss.backward()  # PyTorch computes the gradients of W and b automatically

print("Gradient for W:", W.grad)
print("Gradient for b:", b.grad)

# ------------------------------
# 6. Update Weights (Gradient Descent)
# ------------------------------
with torch.no_grad():  # Disable gradient tracking for manual weight update
    W -= 0.01 * W.grad  # Update weights with learning rate 0.01
    b -= 0.01 * b.grad  # Update bias

# Clear the gradients after updating
W.grad.zero_()
b.grad.zero_()

print("Updated weights:", W)
print("Updated bias:", b)
