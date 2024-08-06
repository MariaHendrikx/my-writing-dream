# Day 5 of trying  to implement text to story



# Terminology

In machine learning, pipelines are sequential processes that automate the workflow of data preprocessing, feature extraction, model training, and evaluation to ensure consistency and reproducibility. They streamline and standardize the process, making it easier to manage and deploy models.

In TensorFlow, pipelines are built using tf.data to create efficient data input workflows and tf.keras to structure model training and evaluation. These tools enable seamless integration of data preprocessing, model training, and deployment, ensuring optimized and scalable machine learning workflows.

TensorFlow Core: Provides the low-level APIs for building and training machine learning models.

Keras: A high-level API within TensorFlow that simplifies model building and experimentation.

CUDA is a parallel computing platform and API for general-purpose GPU programming.

TensorFlow is a machine learning framework that can utilize CUDA to accelerate its operations on NVIDIA GPUs.

inference refers to the process of using a trained model to make predictions or generate outputs based on new, unseen data. It is the phase where the model is applied to real-world data to produce useful results, following the training phase where the model learns from a dataset.

If the model is too large for a single GPU and you are using PyTorch, you can set device_map="auto" to automatically determine how to load and store the model weights. Using the device_map argument requires the 🤗 Accelerate package: