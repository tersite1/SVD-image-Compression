# SVD-image-Comprresion


Reducing Image Size by SVD(Singular Value Decomposition).

This Visualizes Singular Value, numbers of SV, and actual data size of Compressed Image. 


A Python code that uses singular value decomposition (SVD) to process image files, specifically decomposing and reconstructing the RGB channels of the image individually. Briefly, it is as follows:

## Load image and perform SVD:
* Read an image file and convert it to a numpy array.
* For each RGB channel (Red, Green, Blue) in the image, we perform SVD to decompose that channel.

  
## Singular value visualization:
* Singular values ​​extracted from SVD are visualized on a logarithmic scale to show the singular values ​​of each channel.

  
## Image reconstruction per channel:
* The image for each channel is approximated using various 'r' values ​​(number of singular values), and these are combined into an RGB image for visualization. For each 'r' value, generate an approximated image using only one of the RGB channels and display the image with the remaining channels set to 0.

# Usage
* SampleImageComprresion.ipynb is exaplning Image Comprresion by SVD step by step. This Uses yonsei.jpeg file as a sample program.
* SVDImageCompressor.py is GUI Program that actually can be process your custom file, and number of Singular Value you want.




## Technologies Used
- Python 3.8+
- NumPy for numerical computations
- Matplotlib for generating plots and visualizing images

## Installation
To set up the project locally, follow these steps:

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
pip install numpy matplotlib
