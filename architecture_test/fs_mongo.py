import os
import architecture_test.common as common
from pymongo import MongoClient


def store_images_data(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".tiff"):
            image = common.get_image_metadata(directory + '/' + filename)
            mongo_insert_image(image)
            continue
        else:
            continue
    return


def mongo_insert_image(image):
    client = MongoClient("mongodb://qashops:abc123.,@localhost:27017")
    db = client.kaggle_amazon
    images_collection = db.images
    inserted_id = images_collection.insert_one(image).inserted_id
    # print "Element " + str(inserted_id) + " successfully added\n"
    return
