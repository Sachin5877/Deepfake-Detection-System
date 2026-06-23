# Day 12

## Goal

Train the first CNN model for deepfake detection.

## Dataset Used

Training Data:
- Real Images: 500
- Fake Images: 500
- Total Images: 1000

Testing Data:
- 20% of dataset
- Total Test Images: 200

## CNN Architecture

Layers:
1. Conv2D (32 filters)
2. MaxPooling2D
3. Conv2D (64 filters)
4. MaxPooling2D
5. Flatten
6. Dense (128 neurons)
7. Dense (1 neuron, Sigmoid)

Optimizer:
- Adam

Loss Function:
- Binary Crossentropy

Metric:
- Accuracy


## Training Results

### Epoch 1
- Accuracy: 72.06%
- Validation Accuracy: 88.75%
- Loss: 0.6069
- Validation Loss: 0.2547

### Epoch 2
- Accuracy: 92.25%
- Validation Accuracy: 90.25%
- Loss: 0.1814
- Validation Loss: 0.2375

### Epoch 3
- Accuracy: 95.13%
- Validation Accuracy: 91.75%
- Loss: 0.1349
- Validation Loss: 0.1716

## Final Evaluation

Test Accuracy:
91.75%

Test Loss:
0.1716

## Observations

- The model showed continuous improvement across all training epochs.
- Training accuracy increased from 72.06% to 95.13%.
- Validation accuracy reached 91.75%.
- Loss decreased steadily, indicating successful learning.
- The model can effectively distinguish between real and fake face images.

## Learning Outcome

- Learned how to train a CNN model.
- Learned how to monitor training and validation performance.
- Learned how to evaluate model accuracy and loss.
- Successfully developed a deepfake image classification model.

## Next Step

- Save the trained model.
- Test on unseen images.
- Create a prediction script.
- Build a simple user interface.