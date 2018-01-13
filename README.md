# Image Resizer

The program resizes given picture by scale, height and width, or only by height or width (second argument is adjusted proportionally). 
The program outputs picture in the same directory with the size of file in the name (pic.jpg --> pic__200x400.jpg) or outputs to input directory.

# How it works

The program takes such arguments:
```
--height - input height
```
```
--width - input width
```
```
--scale - input scale
```
```
--output - input path to directory for file saving
```
Picture name must be the last input argument

# Example input

```
$ python image_resize.py arg1 arg2 arg3 picture_name
```

```
$ python image_resize.py --height 500 --width 400 --output /Users/Ksusha/Desktop/programming/devman/12_image_resize/folder diagram.png
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
