from PIL import Image
import os
import argparse


def resize_image(image, width, height):
    return image.resize((width, height))


def count_width(actual_width, actual_height, new_height):
    width = (new_height * actual_width) // actual_height
    return width


def count_height(actual_width, actual_height, new_width):
    height = (new_width * actual_height) // actual_width
    return height


def resize_img_by_scale(scale_number, image, actual_height, actual_width):
    new_height = round(scale_number * actual_height)
    new_width = round(scale_number * actual_width)
    return resize_image(image, new_width, new_height)


def make_new_imgname(img_name, height, width):
    filename, extension = os.path.splitext(img_name)
    return "{}_{}x{}{}".format(filename, height, width, extension)


def check_params_and_resize(image, args):
    width, height = args.width, args.height
    actual_width, actual_height = image.size

    if all([args.scale, any([height, width])]):
        return None

    if args.scale:
        new_image = resize_img_by_scale(args.scale, image, actual_height, actual_width)

    else:
        if height is None:
            height = count_height(actual_width, actual_height, width)

        elif width is None:
            width = count_width(actual_width, actual_height, height)

        new_image = resize_image(image, width, height)
    return new_image


def save_the_image(image, args, new_imgname):
    if args.output:
        image.save(os.path.join(args.output, new_imgname))
    else:
        dir_path = os.path.dirname(os.path.realpath(args.input))
        image.save(os.path.join(dir_path, new_imgname))


def define_command_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--scale", type=float)
    parser.add_argument("--height", type=int)
    parser.add_argument("--width", type=int)
    parser.add_argument("--output", type=str)
    parser.add_argument("--input")
    return parser.parse_args()


if __name__ == '__main__':
    args = define_command_line_args()
    if args.input is None:
        print("Please enter your png/jpeg file")
    input_image = Image.open(args.input)
    new_image = check_params_and_resize(input_image, args)
    if new_image is None:
        print("Enter either scale or height and width")
    else:
        width, height = new_image.size
        new_imgname = make_new_imgname(args.input, height, width)
        save_the_image(input_image, args, new_imgname)
