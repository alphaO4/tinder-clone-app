import requests
from time import sleep

url = "https://thispersondoesnotexist.com/image"

input("How many pic's should be downloaded? ")

for i in range(input):
    response = requests.get(url)
    with open('E:/Tinder/tinder-clone-app/Fake people/fake_people-{}.jpg'.format(i), "wb") as file:
        file.write(response.content)
        file.close()
    print("fake_people-{}.jpg downloaded".format(i))
    sleep(1)

