# **Finding Lane Lines on the Road** 

## Pipeline
1. Convert image to be grayscale.
2. Use Gaussian blur to reduce noise.
3. Canny edge detection.
4. Use rudimentary masking to get rid of unwanted lines
5. Run hough transform to find lines in the image
6. Do line classification with highest slope from the left and the right
7. Calculate mean slope and intercept 
8. Overlay the drawings on the original image

## Results

---

**Finding Lane Lines on the Road**

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report


[//]: # (Image References)

[image1]: ./examples/grayscale.jpg "Grayscale"

---

### Reflection

### 1. Describe your pipeline. As part of the description, explain how you modified the draw_lines() function.

My pipeline consisted of 5 steps. First, I converted the images to grayscale, then I .... 

In order to draw a single line on the left and right lanes, I modified the draw_lines() function by ...

If you'd like to include images to show how the pipeline works, here is how to include an image: 

![alt text][image1]


### 2. Identify potential shortcomings with your current pipeline
#### Classification of lines
The classification of lines falls short when there are lines on the road surface. Here a better classification would be needed, that isn't just dependent on the steepest slope. One possibility would be a plausibility check of the slope. For example only allowing the slope to be between 0.5 and 0.9.
#### Hough parameters
The hough function uses absolute values for threshold, min_line_len and max_line_gap that were derived from the provided low resolution videos. They don't work very well on a higher resolution video like the challenge video. One possible solution would be the usage of relative values depending on the size of the image.
#### Smoothing of line
in the videos the detected lane lines are jittering quite bad, especially in the challenge video. A smoothing between the frames would solve this. 


### 3. Suggest possible improvements to your pipeline

#### Grayscale conversion 
I chose not to use the provided conversion to grayscale since it's just averaging over all channels. This isn't working very well on the yellow line, especially on light road surfaces like in the challenge video.
By just averaging we lose all contrast here. One possibility would be a weighted average (e.g. squared) to give a bias to brighter monocromatic colors. See below for an algorithm enhancing the contrast.

For this project it's more sensible to just use the red channel as the grayscale image. This keeps most of the contrast without much computation. The red channel is the most useful because yellow is strongest in the red channel. 
This is of course no universal approach. Lines of colors other than yellow, red, pink and white would be at a disadvantage to the point of beeing totally invisible.


![](https://github.com/stefancyliax/CarND-LaneLines-P1/blob/master/output_images/grayscale_conversion.png)

#### Increasing the contrast of the lines
The challenge video is hard because there is very little contrast between the yellow line and the light surface. Besides having lots of shadows, tire marks and other noise.

I added a experimental line of code to the pipeline that increases the contrast of the picture, but slows the processing down significantly. The render time went from 18 seconds to 15 minutes. There may be a faster implementation though.

The code lowers the value of every pixel below the value of 230. This threshold is deliberatly choosen to separate the light road surface from the yellow line in the challenge video. See the effect in the picures above. The result of the algorithm is on the right.
