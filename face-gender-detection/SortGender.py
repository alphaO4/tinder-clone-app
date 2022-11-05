#! /usr/bin/python3
# -*- coding: utf-8 -*-

#imports
import os
from predict_gender import predict_gender
import requests
from faker import Faker
from time import sleep
import json
import sys

#config
path = "E:/github/tinder-clone-app/Fake people"
files = [f for f in os.listdir(path) if f.endswith(".jpg")]

fake = Faker()

#download fake people from thispersondoesnotexist.com
def download_pics(i):
    url = "https://thispersondoesnotexist.com/image"
    if i == 0:
        pics_to_download = input("How many pic's should be downloaded? ")
    else:
        pics_to_download = i
    print("Downloading "+ str(pics_to_download) + " pic's...")
    for i in range(int(pics_to_download)):
        response = requests.get(url)
        with open(
            "E:/GitHub/tinder-clone-app/Fake people/fake_people-{}.jpg".format(i), "wb"
        ) as file:
            file.write(response.content)
            file.close()
        print("Downloaded fake_people-{}.jpg".format(i))
        sleep(2)
    print("Downloaded " + str(pics_to_download) + " pic's\n")

#identify the gender of the fake people

def identify_gender(path, files):
    gender = 0
    males = 0
    females = 0
    # loop through all the files
    for file in files:
        full_path = path + "/" + file
        gender = predict_gender(full_path)
        if gender == "Female":
            # delete the file
            os.rename(full_path, path + "/delete{}.jpg".format(females))
            females += 1

        else:
            males += 1
    delete_files = [f for f in os.listdir(path) if f.endswith(".jpg")]
    for file in delete_files:
        full_path = path + "/" + file
        # if the filename is 'delete' delete the file
        if file.find ("delete") != -1:
            # delete the file
            os.remove(full_path)

    print("Saved " + str(males) + " Males and ignored " + str(females) + " Females\n")

#add fake names and the expected imgURL to a json file
def add_to_json(path, files, fake):
    json_file = "E:/Github/tinder-clone-app/Fake people/fake_people.json"
    input_for_json_file = []
    files = [f for f in os.listdir(path) if f.endswith(".jpg")]
    # loop through all the files
    try:
        os.remove(json_file)
        print("Deleted old json file\n")
    except:
        print("No old json file found\n")
        print("Adding to json...\n")
        pass
    for file in files:
        #since we are going to upload to Github we can predict the imgURL
        # the imgURL will have the format "https://raw.githubusercontent.com/alphaO4/tinder-clone-app/master/Fake%20people/"
        imgURL = "https://raw.githubusercontent.com/alphaO4/tinder-clone-app/master/Fake%20people/"
        #creat fake male name
        name = fake.name_male()
        # add the imgURL to the name
        imgURL = imgURL + file
        # add the name and the imgURL to a json file
        input_for_json_file.append({"name": name, "imgUrl": imgURL})
        print("Added Name: " + name + "and URL: " + imgURL + " to fake_people.json\n")
    
    with open(json_file, "a") as file:
        json.dump(input_for_json_file, file)
        file.close()

if __name__ == '__main__':
    i = sys.argv[1]
    print("Starting...\n")
    download_pics(i)
    print("Downloaded fake people\n")
    sleep(1)
    print("Identifying...\n")
    identify_gender(path, files)
    print("Identified people\n")
    sleep(1)
    add_to_json(path, files, fake)
    print("Added to json\n")
    sleep(1)
    print("Done, exiting...\n")
    sleep(1)
    exit()
