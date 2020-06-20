import numpy as np
import cv2
import requests
import random
import string
from datetime import date

import string

citys = [
    "Antoinetteston",
    "Letaville",
    "Juanaville",
    "Ebonyston",
    "Araville",
    "Callieville",
    "Chelseaston",
    "Maryston",
    "Kodyville",
    "Maryjaneville",
]

def random_num(start, end):
    nums = []
    for i in range(start, end+1):
        nums.append(i)
    return random.choice(nums)

def valid_name(name):
    for i in name:
        if i not in string.ascii_letters:
            return False
    return True


def random_info():
    info = requests.get("https://randomuser.me/api/").json()
    while valid_name(info["results"][0]["name"]["last"]) == False or valid_name(info["results"][0]["name"]["first"]) == False:
        info = requests.get("https://randomuser.me/api/").json()
    name = f'{info["results"][0]["name"]["last"]}, {info["results"][0]["name"]["first"]}'.upper()
    dob = info["results"][0]["dob"]["date"].split("T")[0]
    sex = info["results"][0]["gender"]
    iss = random.choice(citys)
    exp = f"{random_num(int(date.today().year)-3, int(date.today().year)+7)}-{random_num(1, 12)}-{random_num(1, 28)}"
    # exp = random.choice([i + int(dob.split("-")[0]) for i in range(100)])
    return name, dob, sex, iss, exp

def random_str(digits=10):
    ans = ""
    for i in range(digits):
        if i == digits // 2:
            ans += " "
        else:
            ans += random.choice(string.ascii_uppercase + string.digits)
    return ans

def passport_img():
    name, dob, sex, iss, exp = random_info()

    image = cv2.imread('images/passports/arstotzka.png', cv2.IMREAD_UNCHANGED)

    position = (10,310)

    cv2.putText(
        image, #numpy array on which text is written
        random_str(), #text
        position, #position at which writing has to start
        cv2.FONT_HERSHEY_SIMPLEX, #font family
        0.6, #font size
        (0, 0, 0, 255), #font color
        1) #font stroke

    cv2.putText(
        image, #numpy array on which text is written
        dob, #text
        (130, 205), #position at which writing has to start
        cv2.FONT_HERSHEY_SIMPLEX, #font family
        0.4, #font size
        (0, 0, 0, 255), #font color
        1) #font stroke

    cv2.putText(
        image, #numpy array on which text is written
        sex, #text
        (130, 223), #position at which writing has to start
        cv2.FONT_HERSHEY_SIMPLEX, #font family
        0.4, #font size
        (0, 0, 0, 255), #font color
        1) #font stroke

    cv2.putText(
        image, #numpy array on which text is written
        iss, #text
        (130, 241), #position at which writing has to start
        cv2.FONT_HERSHEY_SIMPLEX, #font family
        0.4, #font size
        (0, 0, 0, 255), #font color
        1) #font stroke

    cv2.putText(
        image, #numpy array on which text is written
        name, #text
        (35, 180), #position at which writing has to start
        cv2.FONT_HERSHEY_SIMPLEX, #font family
        0.5, #font size
        (0, 0, 0, 255), #font color
        1) #font stroke

    cv2.putText(
        image, #numpy array on which text is written
        name, #text
        (35, 180), #position at which writing has to start
        cv2.FONT_HERSHEY_SIMPLEX, #font family
        0.5, #font size
        (0, 0, 0, 255), #font color
        1) #font stroke

    cv2.putText(
        image, #numpy array on which text is written
        exp, #text
        (130, 259), #position at which writing has to start
        cv2.FONT_HERSHEY_SIMPLEX, #font family
        0.5, #font size
        (0, 0, 0, 255), #font color
        1) #font stroke

    cv2.imwrite('output.png', image)

"""if __name__ == "__main__":
    data = random_info()
    main(data[0], data[1], data[2], data[3], data[4])"""