from PIL import Image
import os
import argparse


def count_width(actual_width, actual_height, new_height):
    width = (new_height * actual_width) // actual_height
    return width


def count_height(actual_width, actual_height, new_width):
    height = (new_width * actual_height) // actual_width
    return height


def height_and_width_by_scale(scale_number, actual_width, actual_height):
    new_height = round(scale_number * actual_height)
    new_width = round(scale_number * actual_width)
    return new_width, new_height


def make_new_imgname(img_name, height, width):
    filename, extension = os.path.splitext(img_name)
    return "{}_{}x{}{}".format(filename, height, width, extension)


def check_params(image, args):
    width, height = args.width, args.height
    actual_width, actual_height = image.size

    if all([args.scale, any([height, width])]):
        raise SystemExit("Enter either scale or height and width")

    if args.scale:
        return height_and_width_by_scale(args.scale, actual_width, actual_height)

    if any([height, width]):
        if height is None:
            height = count_height(actual_width, actual_height, width)

        elif width is None:
            width = count_width(actual_width, actual_height, height)

        return width, height
    else:
        raise SystemExit("Enter valid height, width or scale")


def resize_image(image, width, height):
    return image.resize((width, height))


def save_the_image(image, args, new_imgname):
    if args.output:
        new_image_path = (os.path.join(args.output, new_imgname))
    else:
        dir_path = os.path.dirname(os.path.realpath(args.input))
        new_image_path = (os.path.join(dir_path, new_imgname))
    image.save(new_image_path)

def define_command_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--scale", type=float)
    parser.add_argument("--height", type=int)
    parser.add_argument("--width", type=int)
    parser.add_argument("--output", type=str)
    parser.add_argument("--input", required=True)
    return parser.parse_args()


if __name__ == '__main__':
    args = define_command_line_args()
    input_image = Image.open(args.input)
    new_width, new_height = check_params(input_image, args)
    new_image = resize_image(input_image, new_width, new_height)
    new_imgname = make_new_imgname(args.input, new_height, new_width)
    save_the_image(input_image, args, new_imgname)
