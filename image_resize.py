from PIL import Image
import os
import argparse


def resize_the_pic(picture_name, width, height):
    return picture_name.resize((width, height))


def count_width(actual_width, actual_height, new_height):
    return int(new_height * actual_width) // actual_height


def count_height(actual_width, actual_height, new_width):
    return int(new_width * actual_height) // actual_width


def get_scale(scale_number, pic_name, actual_height, actual_width):
    new_height = round(scale_number * actual_height)
    new_width = round(scale_number * actual_width)
    return resize_the_pic(pic_name, new_width, new_height)


def argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--scale",
                        type=int,
                        action='store',
                        nargs=1)
    parser.add_argument("--height",
                        type=int,
                        action='store',
                        nargs=1)
    parser.add_argument("--width",
                        type=int,
                        action='store',
                        nargs=1)
    parser.add_argument("--output",
                        type=str,
                        action='store',
                        nargs=1)

    args = parser.parse_known_args()
    picname, args_dict = args[-1][0], vars(args[0])
    return picname, args_dict


def make_new_picname(picname, height, width):
    dot = picname.rfind(".")
    return "{}_{}x{}{}".format(picname[:dot], height, width, picname[dot:])

def make_new_picture(picname, args_dict, picture):
    width = args_dict["width"] and args_dict["width"][0]
    height = args_dict["height"] and args_dict["height"][0]
    scale = args_dict["scale"] and args_dict["scale"][0]
    output = args_dict["output"] and args_dict["output"][0]

    if scale is not None and (height is not None or width is not None):
        print("Enter either scale or height and width")
        raise SystemExit

    if scale is not None:
        picture = get_scale(scale, picture, actual_height, actual_width)
        height, width = actual_height, actual_width

    else:
        if height is None and width is not None:
            height = count_height(actual_width, actual_height, width)

        elif width is None and height is not None:
            width = count_width(actual_width, actual_height, height)

        picture = resize_the_pic(picture, width, height)

    new_picname = make_new_picname(picname, height, width)
    if output is not None:
        return picture.save(os.path.join(output, new_picname))
    else:
        dir_path = os.path.dirname(os.path.realpath(picname))
        return picture.save(os.path.join(dir_path, new_picname))



if __name__ == '__main__':
    (picname, args_dict) = argument_parser()
    picture = Image.open(picname)
    make_new_picture(picname, args_dict, picture)
