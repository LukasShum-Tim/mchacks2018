# mchacks2018
McHacks 2018 project

Not user friendly, but here are out steps:
1) Format gun and non-gun images for the computer to learn the trends. We had to change the RGB format to grayscale in order to have the correct format input.
2) We dumped the trained model in a file.
3) We tried to predict new images that the computer hasn't seen with the trained model. If the computer doesn't recognize a gun in the image, we tried to split the image in 4 in order to try to spot guns if ever they would be in smaller sizes on the image. If the result is still negative, then the computer will predict that there is no gun in the image.
