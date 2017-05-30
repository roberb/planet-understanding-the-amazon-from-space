from PIL import Image, ExifTags
import numpy as np
import datetime
import exifread


def save_image_binary(array_image, path):
    img = Image.fromarray(array_image)
    img.save(path)


def load_image_binary(path):
    binary = Image.open(path)
    return binary


def image_to_array(binary):
    binary.load()
    array_image = np.asarray(binary, dtype="int32")
    return array_image


def get_image_exif_data(path):
    # Open image file for reading (binary mode)
    f = open(path, 'rb')
    # Return Exif tags
    tags = exifread.process_file(f)
    return tags


def get_image_metadata(path):
    name_parts = path.split('.')
    extension = name_parts[len(name_parts) - 1]
    exif = get_image_exif_data(path)
    size = get_image_size(path)
    metadata = {
        "path": path,
        'size': size,
        "extension": extension,
        "exif": exif,
        "time_add": datetime.datetime.utcnow()
    }
    return metadata


def get_image_size(path):
    im = load_image_binary(path)
    width, height = im.size
    return str(width) + 'x' + str(height)
