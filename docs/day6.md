# Day 6

## Goal

Analyze the downloaded dataset using Python.

## Dataset Location

Stored locally outside the GitHub repository.

## Tasks Completed

- Created dataset_info.py
- Read dataset folders using Python
- Counted images in each category
- Verified dataset structure

## Dataset Structure

dataset/
└── deepfake_faces/
    ├── train/
    │   ├── real/
    │   └── fake/
    ├── validation/
    │   ├── real/
    │   └── fake/
    └── test/
        ├── real/
        └── fake/

## Output
TEST
Fake: 5492
Real: 5413

TRAIN
Fake: 70001
Real: 70001

VALIDATION
Fake: 19641
Real: 19787
## Learning Outcome

- Learned how to access folders using Python.
- Learned how to count files in directories.
- Verified that the dataset was extracted correctly.

## Next Step

Load and display sample images using OpenCV.