# low_image_enhancement

During the past years, deep convolutional neural networks have achieved impressive success in low-light Image Enhancement. Existing deep learning methods mostly enhance the ability of feature extraction by stacking network structures and deepening the depth of the network. In order to reduce inference time while fully extracting local features and global features. Inspired by SGN, we propose an Attention based Broadly Self- guided Network (ABSGN) for real world low-light image Enhancement. 
The basic structure of ABSGN is a top- down self-guidance architecture which is able to efficiently incorporate multi-scale information and extract good local features to recover clean images. Moreover, such a structure requires a smaller number of parameters and enables us to achieve better effectiveness than U-Net structure. In addition, the proposed network comprises several multi-level guided Dense Blocks (MGDB) which can be viewed as a novel extension of Dense block in feature space. 
At the lowest resolution level of ABSGN, we offer more efficient module to fully extract the global information to generate the better final output, which called Global Spatial Attention (GSA). Such broad strategy is able to handle the noise at different exposures. The proposed network is validated by many mainstream benchmarks. Additional experimental results show that the proposed network outperforms most of state-of-the- art low-light image enhancement solutions.