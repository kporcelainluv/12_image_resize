# Image Resizer

The program resizes given picture by scale or height and width or only by height or width (second argument is adjusted proportionally). 
The program outputs picture to the same directory (and adds picsize to the name, ex pic__200x400.jpg) or to output directory if given.

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
# Example output
If user enters scale
```
Height and width are adjusted to scale
```
If user enters either height or width
```
Your second parameter is adjusted automatically
```
If user enters both height and width
```
Height and width are read from input and are not adjusted
```

# Error output

If user enters wrong directory path for output
```
Enter a valid path to directory.
```
if user enters height, width and scale at once
```
Enter either scale or height and width.
```
If user doesn't enter height, width or scale
```
Enter valid height, width or scale.
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
