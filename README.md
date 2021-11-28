##
YOLO---Custom-Object-Detection

For running [Pedestrian_Detection.py](https://github.com/souvik0306/YOLO---Custom-Object-Detection/blob/main/Pedestrian_Detection.py) we need a custom weights file, please download it from here- [Google Drive Link](https://drive.google.com/file/d/1HTlwv4sklFxbRjeLUSE6tyk11Id1mxCh/view?usp=sharing)

```bash
**ATTENTION - It is advisable to use OpenCV version 4.5.3 instead of the latest 4.5.4 
                     due to a reported bug that inhibits the execution of the script.**
```
**Dataset Used for Training** - [University of Pennsylvania’s Penn-Fudan Database](https://www.cis.upenn.edu/~jshi/ped_html/) for Pedestrian Detection and Segmentation. 
This is an image database containing images that are used for pedestrian detection. 
The images are taken from scenes around campus and urban streets.

Each image contains at least one pedestrian in it and the heights of labelled pedestrians in this database fall into [180,390] pixels.
There are 170 images with 345 labelled pedestrians,
among which 96 images are taken from around the University of Pennsylvania, and the other 74 are taken from around Fudan University. The reason for choosing this particular 
dataset was that it provides a decent number of good quality images for training a model.

Use [Make Sense.ai](https://www.makesense.ai/) to manually label the images and export the final result in YOLO Bounding Box Format as a .txt file. In YOLO, a bounding box is represented by four values [x_center, y_center, width, height].x_center and y_center are the normalized coordinates of the center of the bounding box. To make coordinates normalized, we take pixel values of x and y, which marks the center of the bounding box on the x- and y-axis. Then we divide the value of x by the width of the image and value of y by the height of the image. 
width and height represent the width and the height of the bounding box and they are normalized as well. 

Final Results - 

<img src="https://github.com/souvik0306/YOLO---Custom-Object-Detection/blob/main/Result_2.jpg" width="750" height="600">
