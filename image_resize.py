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
    return "{}__{}x{}{}".format(filename, height, width, extension)


def check_params(args):
    parser = argparse.ArgumentParser()
    if args.output:
        if not os.path.isdir(args.output):
            parser.error("Enter a valid path to directory")
    if all([args.scale, any([args.height, args.width])]):
        parser.error("Enter either scale or height and width.")
    if not any([args.width, args.height, args.scale]):
        parser.error("Enter valid height, width or scale.")
    return True


def count_height_and_width(act_width, act_height, height, width):
    if height is None:
        height = count_height(act_width, act_height, width)
    elif width is None:
        width = count_width(act_width, act_height, height)
    return width, height


def resize_image(image, width, height):
    return image.resize((width, height))


def save_the_image(image_name,
                   resized_image,
                   output_path,
                   original_image,
                   new_width,
                   new_height):
    if output_path:
        new_image_path = (os.path.join(output_path, image_name))
    else:
        dir_path = os.path.dirname(os.path.realpath(original_image))
        new_imgname = make_new_imgname(original_image, new_width, new_height)
        new_image_path = (os.path.join(dir_path, new_imgname))
    resized_image.save(new_image_path)


def parse_command_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--scale",
                        type=float,
                        help="scale to which height and width will be adjusted")
    parser.add_argument("--height",
                        type=int,
                        help="height of the pic")
    parser.add_argument("--width",
                        type=int,
                        help="width of the pic")
    parser.add_argument("--output",
                        type=str,
                        help="path to catalog to save the pic")
    parser.add_argument("--input",
                        required=True,
                        help="pic you want to resize")
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_command_line_args()
    input_image = Image.open(args.input)
    actual_width, actual_height = input_image.size
    if check_params(args):
        if all([args.height, args.width]):
            text = "Height and width are read from input and are not adjusted"
            print(text)
            new_width, new_height = args.width, args.height

        elif args.scale:
            new_width, new_height = count_height_and_width_by_scale(args.scale,
                                                                    actual_width,
                                                                    actual_height)
            print("Height and width are adjusted to scale")

        elif any([args.height, args.width]):
            print("Your second parameter is adjusted automatically")
            new_width, new_height = count_height_and_width(
                actual_width,
                actual_height,
                args.height,
                args.width)

        new_image = resize_image(input_image, new_width, new_height)
        save_the_image(args.input,
                       input_image,
                       args.output,
                       args.input,
                       new_width,
                       new_height)
