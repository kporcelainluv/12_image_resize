from PIL import Image
import os
import argparse


def count_width(actual_width, actual_height, new_height):
    width = (new_height * actual_width) // actual_height
    return width


def count_height(actual_width, actual_height, new_width):
    height = (new_width * actual_height) // actual_width
    return height


def count_height_and_width_by_scale(scale_number, actual_width, actual_height):
    new_height = round(scale_number * actual_height)
    new_width = round(scale_number * actual_width)
    return new_width, new_height


def make_new_imgname(img_name, height, width):
    filename, extension = os.path.splitext(img_name)
    return "{}_{}x{}{}".format(filename, height, width, extension)


def check_params(args):
    parser = argparse.ArgumentParser()

    if all([args.scale, any([args.height, args.width])]):
        parser.error("Enter either scale or height and width.")
    if not any([args.width, args.height, args.scale]):
        parser.error("Enter valid height, width or scale.")
    return True


def count_height_and_width(actual_width, actual_height, height, width, scale):
    if scale:
        return count_height_and_width_by_scale(scale, actual_width, actual_height)

    if all([height, width]):
        print("Height and width are being read from input and are not adjusted to each other.")
        return width, height

    elif any([height, width]):
        print("Your second parameter (either height or width) will be adjusted automatically.")

        if height is None:
            height = count_height(actual_width, actual_height, width)

        elif width is None:
            width = count_width(actual_width, actual_height, height)

        return width, height


def resize_image(image, width, height):
    return image.resize((width, height))


def save_the_image(image_name, image, output_image, input_image, new_width, new_height):
    if output_image:
        new_image_path = (os.path.join(output_image, image_name))
    else:
        dir_path = os.path.dirname(os.path.realpath(input_image))
        new_imgname = make_new_imgname(input_image, new_width, new_height)
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
    actual_width, actual_height = input_image.size
    if check_params(args):
        new_width, new_height = count_height_and_width(
            actual_width,
            actual_height,
            args.height,
            args.width,
            args.scale)
        new_image = resize_image(input_image, new_width, new_height)
        save_the_image(args.input, input_image, args.output, args.input, new_width, new_height)
