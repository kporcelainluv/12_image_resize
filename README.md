# Image Resizer

The program resizes given picture by scale, height and width, or only by height or width (second argument is adjusted proportionally). 
The program outputs picture in the same directory or outputs to input directory and adds the size of file to the name.
(pic.jpg --> pic__200x400.jpg)

# How it works

The program takes such arguments:
```
--height - height
```
```
--width - width
```
```
--scale - scale
```
```
--input - picture [pic.png]
```
```
--output - path to directory for file saving
```

# Example input

```
$ python image_resize.py arg1 arg2 arg3 --input picture_name
```

```
$ python image_resize.py --height 500 --width 400 --output /Users/Ksusha/Desktop/programming/devman/12_image_resize/folder --input diagram.png
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
