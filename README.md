# low_image_enhancement

During the past years, deep convolutional neural networks have achieved impressive success in low-light Image Enhancement. Existing deep learning methods mostly enhance the ability of feature extraction by stacking network structures and deepening the depth of the network. In order to reduce inference time while fully extracting local features and global features. Inspired by SGN, we propose an Attention based Broadly Self- guided Network (ABSGN) for real world low-light image Enhancement. 
The basic structure of ABSGN is a top- down self-guidance architecture which is able to efficiently incorporate multi-scale information and extract good local features to recover clean images. Moreover, such a structure requires a smaller number of parameters and enables us to achieve better effectiveness than U-Net structure. In addition, the proposed network comprises several multi-level guided Dense Blocks (MGDB) which can be viewed as a novel extension of Dense block in feature space. 
At the lowest resolution level of ABSGN, we offer more efficient module to fully extract the global information to generate the better final output, which called Global Spatial Attention (GSA). Such broad strategy is able to handle the noise at different exposures. The proposed network is validated by many mainstream benchmarks. Additional experimental results show that the proposed network outperforms most of state-of-the- art low-light image enhancement solutions.


This python script is based on the implementation concenpt of haze removal from Zhiming Tan Et al. [Research Paper](https://www.semanticscholar.org/paper/Fast-Single-image-Defogging-Tan-Bai/64caa24f2cb3fff6d8eb966f90078f0d0b8a7db0?p2df)

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


Intensity of atmospheric light <code>A</code> is estimated form hazed image <code>I(x)</code> Transmission map <code>t(x)</code> is estimated using <code>A</code> and <code>I(x)</code> Image is clarified with the image defogging model

### Estimate intensity of atmospheric light:
Finding the top 0.1% brightest pixels in the dark channel then choose one with highest intensity as the representing of atmospheric light. This part is not needed in our case and thus ignored

### Estimate transmission map:
Find a dark channel based on a local area(coarsemap) Then, the transmission map <code>t(x)</code> is thereby obtained:

<code>t(x) = 1 – defoggingParam * darkPixelFromCoarseMap / AtmosphericLightIntensity</code>

The <code>defoggingParam</code> is a value between 0 to 1. The higher value the lesser amount of fog would be kept for the distant objects.

### Clarify image:
The image is clarified by:<code> J(x)=(I(x)- A)/max(t(x), t0)+A</code>

Where <code>J(x)</code> is output, <code>I(x)</code> is input,<code> t(x) </code>is transmission map, A is atmospheric light and t0 is set to a constant value to avoid dividing by zero.

## Usage:
Currently, the user has to specify the input image and output image path in a main() function. Next update will use console arguments to specify the image path. Feel free to add new things to the code and pull a merge request.

## Dependencies
cv2 numpy Pytorch ski-image
