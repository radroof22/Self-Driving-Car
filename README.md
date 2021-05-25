# Self-Driving-Car
This project include a self-driving car which uses Tensorflow, convolutional neural networks, and a Raspberry Pi mounted on an RC car to drive through a path traced out on the ground by white paper.

![Image of Self-Driving Car Created](https://user-images.githubusercontent.com/23004551/119425305-1e756c80-bcd5-11eb-86af-e4d66b0dcda7.png)

## Overview
* This project was created using a Tensorflow LSTM which would recieve images from the client robot and make predicition for which turns it should make
* The pictures on the client were taken using OpenCV2 and would be sent over as raw pixels in the form of a real-time web socket
* The model learned to drive through a paper track on the ground and passed the statistical analysis proof

## Awards
* Montgomery County Science Research Competition Certificate of Achievement for Division D First Place 0500 Computers on March 09, 2018 (Ursinus College)
* MCSTA: Excellence in Student Science Research Award in Computer Science High School Level Award at the 2018 Montgomery County Science Research Competition on March 9, 2018 (Ursinus College)
* Delaware Valley Science Fairs, 70th Annual Delaware Valley Science Fairs: First Place April 4 th 2018:
* Pennsylvania Junior Academy of Science at Pennsylvania State University May 21, 2018: First Award State
* Intel Excellence in Computer Science Award

## Hypothesis
- I believe the machine learning model will outperform random chance decisions during driving because Convolutional networks have been proven to understand images as well as neural networks being able to understand complex processes.
- Null: There is no statistical advantage of using machine learning models compared to random decisions for autonomous driving.

## Hardware
- Raspberry Pi 3 Model B
- 5v Power Bank with Micro-USB cable
- L293d
- RC Car (needs to be motted so motors connect to L293d)
- 9 volt Battery with Conversion to Two Open Wires
- USB Webcam
- Breadboard
- 7 Female to Female Jumper Wires
- 20 Male to Male Jumper Wires

## Software
**Raspberry Pi**
* Python
* Raspberry Pi GPIO
* Pygame
* Pickle
* Numpy 
* PILLOW
* Socket

**Desktop**
* Python
* Tensorflow
* Pickle
* Numpy
* PILLOW
* Socket

## Steps
1. **Mod RC Car**: Connect RC Car motors to L293d and connect L293d to Breadboard which connects to Raspberry Pi
2. **Collect Training Data**: Create track out of paper and use car to drive and take pictures
![Flow Chart for Collecting Data and Image of Track](https://user-images.githubusercontent.com/23004551/119425307-1e756c80-bcd5-11eb-8784-6c0cc76ee705.png)
3. **Train Model**: Files ranem to dictionary of directions possible, filter images to black and white, and input into *multilayer convolutional neural network*
4. **Evaluate Model**: Create new track and create websocket connection between Laptop and Pi so that images are sent to desktop, evaluated by model, and directions are sent back to Pi to drive the car
![Flow Chart of Evaluation of Model](https://user-images.githubusercontent.com/23004551/119425308-1e756c80-bcd5-11eb-88c0-29561dfb4018.png)


## Data Analysis
- Compare the number of correct directional movements it does compared to the total number it does
- Incorrect directional movement is one that takes it outside of the course or would not be appropriate given the current circumstances 
- **Null Hypothesis**: The use of autonomous cars trained on pure image data has no statistically significant advantage over random decisions
- **Anti-Hypothesis**: The use of AI trained on pure image data is statistically significantly superior compared to random movements
- Z = 32.25 > 1.96 so can *reject the null hypothesis*
