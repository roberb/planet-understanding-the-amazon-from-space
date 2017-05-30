import datetime
from pymongo import MongoClient
import os
import PIL.Image
import PIL.ExifTags


def store_images_data(directory):
    client = MongoClient('localhost', 27017)
    db = client.kaggle_amazon
    imagesCollection = db.images

    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".tiff"):
            img = PIL.Image.open(filename)
            nameParts = filename.split('.')
            extension = nameParts[len(nameParts) - 1]
            exif = {
                PIL.ExifTags.TAGS[k]: v
                for k, v in img._getexif().items()
                if k in PIL.ExifTags.TAGS
                }
            image = {
                "path": "filename",
                "extension": extension,
                "exif": exif,
                "time_add": datetime.datetime.utcnow()
            }
            inserted_id = imagesCollection.insert_one(image).inserted_id
            print "Element " + inserted_id + " successfully added with info:\n"
            for x in image:
                print (x)
                for y in image[x]:
                    print (y, ':', image[x][y])
            continue
        else:
            continue
    return
