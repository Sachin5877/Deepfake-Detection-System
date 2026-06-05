# Day 3

## Project Decision

Selected Project:
Image Deepfake Detection

Reason:
Image deepfake detection is simpler to build, train, test, and explain in a college mini project.

## Next Task

Research suitable datasets containing real and fake images.

## Task Answer
# Day 3 - Image Deepfake Dataset Research

## Selected Project

### Project Name

Image Deepfake Detection

### Reason

Image deepfake detection is simpler to build, train, test, and explain in a college mini project.

---

## Dataset Comparison

| Dataset                  | Real Images          | Fake Images              | Storage | Download Method     |
| ------------------------ | -------------------- | ------------------------ | ------- | ------------------- |
| 140K Real and Fake Faces | 70,000               | 70,000                   | 4.04 GB | Kaggle ZIP Download |
| Deepfake Image Dataset   | Contains Real Images | Contains Deepfake Images | 504 MB  | Kaggle ZIP Download |

---

## Dataset 1: 140K Real and Fake Faces

### Dataset Information

* Total Images: 140,000
* Real Images: 70,000
* Fake Images: 70,000
* Image Resolution: 256 × 256 pixels
* Storage Required: 4.04 GB

### Source

* Real images from FFHQ (Flickr-Faces-HQ)
* Fake images generated using StyleGAN

### Download Method

* Download from Kaggle as a ZIP file.
* Extract the ZIP file before training.

### Advantages

* Balanced dataset with equal real and fake images.
* Large dataset suitable for deep learning.
* Preprocessed and resized images.
* Good for training accurate deepfake detection models.

### Disadvantages

* Limited to face images.
* Fake images are mainly generated using StyleGAN.

---

## Dataset 2: Deepfake Image Dataset

### Dataset Information

* Contains real and deepfake images.
* Includes training and testing datasets.
* Storage Required: 504 MB

### Download Method

* Download from Kaggle as a ZIP file.
* Extract the ZIP file before use.

### Advantages

* Small size and easy to download.
* Suitable for quick experiments and testing.
* Requires less storage and training time.

### Disadvantages

* Smaller dataset.
* May not provide the same accuracy as larger datasets.
* Limited diversity compared to larger datasets.

---

## Recommended Dataset

### Selected Dataset

140K Real and Fake Faces

### Reason

This dataset contains a large number of balanced real and fake images, making it ideal for training an image deepfake detection model. The dataset size is manageable while still providing enough data for good model performance in a college mini project.

---

## Conclusion

For the Image Deepfake Detection project, the 140K Real and Fake Faces dataset is selected as the primary dataset because it provides a balanced collection of real and fake images, sufficient training data, and manageable storage requirements. The Deepfake Image Dataset can be used later for additional testing and evaluation.
