<br />
<p align="center">
  <a href="https://github.com/retruxstudio/hycam">
    <img src="assets/hycam.ico" width="70" height="70"alt="Logo">
  </a>

  <h3 align="center">hycam</h3>
  <p align="center">
    A face tracking and gesture control camera for hybrid teaching solution
    <br>
    <br>
  </p>
</p>

![Animation](assets/hero.gif)

[![OS](https://img.shields.io/badge/v1.0.0-Install-9F66FF)](https://github.com/retruxstudio/hycam/releases/tag/v1.0.0)

## About the Project

Pandemic already change every aspect in the world including education and learning process. Since school and institution do hybrid teaching for they class, it should be haved a proper and well setup for doing that. The class should be have a camera that can be use to capture teacher in any position, and student in the class, so online student can see both of them in any online meeting platform from they place. Introducing hycam, a smart camera kit for a hybrid teaching solution. with this camera, teachers can naturally teach both onsite and online students without worrying about any gap between them. This camera use face tracking and gesture control algoritm to control and rotate camera position depend on teacher face and hand gesture in the class.

## Hardware setup

Hycam kit uses serial monitor to communicate with the app, and the app itself can be running well with a camera connected to your device, so make sure you already pluged in both serial and camera USB cable first into your device before running hycam app.

## Setup

Hycam app available in python-based and windows app. For the windows app, you can install it from <a href="https://github.com/retruxstudio/hycam/releases/tag/v1.0.0">Release page</a>. And for the python-based, you should have all of the requirements shown below before use it:

- Python 3.9.7+
- Mediapipe 0.8.9+
- Numpy 1.21.4+
- Opencv_python 4.5.4.60+
- Pillow 9.0.0+
- Pyserial 3.5+
- Tensorflow 2.7.0+

If you already have `Python 3.9.7+` on your device, you can easily install all of the requirements with running this: 

```python
pip install -r requirements.txt
```

## Feature

- ✔ Tracking teacher face while teaching in front of the class, and students' faces when near the mic.
- ✔ Perform rotations depending on the following hand gesture commands:

  - ✋ Camera rotate to student mic location
  - 👍 Camera rotate back to teacher location
  - 👌 Camera rotate to all over the student in the class 

## Retrux's development lab

Retrux Studio, hello@retrux.com

Retrux is a leading digital agency with solid design and development expertise. We build mobile and web products for startups. Drop us a line.