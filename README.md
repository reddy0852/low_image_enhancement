# ABSGN: Attention-based Broadly Self-guided Network for Low-Light Image Enhancement

## Introduction

In recent years, deep convolutional neural networks have achieved impressive success in low-light image enhancement. This repository introduces the Attention-based Broadly Self-guided Network (ABSGN) for real-world low-light image enhancement.

## Key Features

- **Efficient Multi-Scale Information:** ABSGN efficiently incorporates multi-scale information and extracts valuable local features for cleaner image restoration.

- **Reduced Parameters:** ABSGN's top-down self-guidance architecture reduces the number of parameters while maintaining effective feature extraction, surpassing the performance of U-Net structures.

- **Multi-Level Guided Dense Blocks (MGDB):** The network introduces MGDB, a novel extension of Dense Blocks in feature space.

- **Global Spatial Attention (GSA):** ABSGN employs Global Spatial Attention at the lowest resolution level to extract global information efficiently, accommodating noise at different exposures.

## Validation

ABSGN has been rigorously tested against popular benchmarks and has consistently outperformed most state-of-the-art low-light image enhancement solutions.


## Screenshots

![WorkFlow Diagram](/pictures/workflow.png)
*WorkFlow Diagram: [Image enhancement involves several stages of processing - CNN, DWT etc  ]*

![CNN + Relu](/pictures/cnn.png)
*CNN + ReLU : [Image enhancement is achieved using CNNs with ReLU activation (CNN + ReLU)]*

## Image Enhancement Technique
The whole technique is based on three steps,

  1.Inverting the low light image<br />
  2.Applying the Haze Removal technique on the inverted image<br />
  3.Invert the enhanced image<br />
## Haze Removal
The removal part comprises of three steps,

  1.Determine the intensity of atmospheric light. *<br />
  2.Estimate transmission map.<br />
  3.Clarify image.<br />
  
   This in our case is constant which is 255, obtain from experimenting on multiple images. This will be updated so that it is calculated through a function. Si nce it was taking too long to compute this value it is better to find the average value of a batch.


## Technologies Used

- Python
- NumPy
- Pandas
- Scikit-learn
- PyTorch
- Opencv2

## Installation

To set up the required libraries, follow these steps:

1. Open a terminal or command prompt.

2. Navigate to the project directory.

3. Run the following command:
   ```shell
   python -m requirements.py
   ```
This will automatically install the necessary libraries for the project.

