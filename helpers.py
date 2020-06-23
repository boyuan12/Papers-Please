import numpy as np
import cv2
import requests
import random
import string
from datetime import date
import string

COUNTRIES_POS = {
    # code, dob, sex, iss, name, exp
    "arstotzka": [(10, 310), (130, 205), (130, 223), (130, 241), (35, 180), (130, 259)],
    "antegria": [(100, 310), (50, 210), (50, 230), (50, 250), (10, 285), (50, 270)],
    "impor": [(120, 305), (140, 203), (140, 220), (140, 237), (40, 180), (140, 254)],
    "kolechia": [(120, 310), (140, 220), (140, 235), (140, 250), (40, 205), (140, 275)],
    "obristan": [(20, 310), (50, 232), (50, 247), (50, 262), (40, 205), (50, 277)],
    "republia": [(130, 310), (50, 205), (50, 223), (50, 241), (40, 185), (50, 259)],
    "united-federation": [(125, 310), (135, 220), (135, 240), (135, 255), (40, 205), (135, 275)]
}

citys = {
    "arstotzka": [
        "Altan",
        "Vescillo",
        "Burnton",
        "Octovalis",
        "Gennistora",
        "Lendiforma",
        "Wozenfield",
        "Fardesto"
    ],
    "antegria": [
        "St. Marmero",
        "Glorian",
        "Outer Grouse"
    ],
    "impor": [
        "Enkyo",
        "Haihan",
        "Tsunkeido"
    ],
    "kolechia": [
        "Yurko City",
        "Vedor",
        "West Grestin"
    ],
    "obristan": [
        "Skal",
        "Lorndaz",
        "Mergerous"
    ],
    "republia": [
        "True Glorian",
        "Lesrenadi",
        "Bostan",
    ],
    "united-federation": [
        "Great Rapid",
        "Shingleton",
        "Korista City"
    ]
}

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
    # iss = random.choice(citys)
    exp = f"{random_num(int(date.today().year)-3, int(date.today().year)+7)}-{random_num(1, 12)}-{random_num(1, 28)}"
    # exp = random.choice([i + int(dob.split("-")[0]) for i in range(100)])
    return name, dob, sex, exp

def random_str(digits=10):
    ans = ""
    for i in range(digits):
        if i == digits // 2:
            ans += " "
        else:
            ans += random.choice(string.ascii_uppercase + string.digits)
    return ans

def passport_img(country, sex="", dob="", name="", exp=""):

    name_1, dob_1, sex_1, exp_1 = random_info()

    if len(name) == 0: name = name_1
    if len(dob) == 0: dob = dob_1
    if len(sex) == 0: sex = sex_1
    if len(exp) == 0: exp = exp_1

    image = cv2.imread(f'images/passports/{country}.png', cv2.IMREAD_UNCHANGED)

    if country != "cobrastan":
        # code
        cv2.putText(
            image, #numpy array on which text is written
            random_str(), #text
            COUNTRIES_POS[country][0], #position at which writing has to start
            cv2.FONT_HERSHEY_SIMPLEX, #font family
            0.6, #font size
            (0, 0, 0, 255), #font color
            1) #font stroke

    # dob
    cv2.putText(
        image, #numpy array on which text is written
        dob, #text
        COUNTRIES_POS[country][1], #position at which writing has to start
        cv2.FONT_HERSHEY_SIMPLEX, #font family
        0.4, #font size
        (0, 0, 0, 255), #font color
        1) #font stroke

    # sex
    cv2.putText(
        image, #numpy array on which text is written
        sex, #text
        COUNTRIES_POS[country][2], #position at which writing has to start
        cv2.FONT_HERSHEY_SIMPLEX, #font family
        0.4, #font size
        (0, 0, 0, 255), #font color
        1) #font stroke

    # iss
    cv2.putText(
        image, #numpy array on which text is written
        random.choice(citys[country]), #text
        COUNTRIES_POS[country][3], #position at which writing has to start
        cv2.FONT_HERSHEY_SIMPLEX, #font family
        0.4, #font size
        (0, 0, 0, 255), #font color
        1) #font stroke

    # name
    cv2.putText(
        image, #numpy array on which text is written
        name, #text
        COUNTRIES_POS[country][4], #position at which writing has to start
        cv2.FONT_HERSHEY_SIMPLEX, #font family
        0.5, #font size
        (0, 0, 0, 255), #font color
        1) #font stroke

    # exp
    cv2.putText(
        image, #numpy array on which text is written
        exp, #text
        COUNTRIES_POS[country][5], #position at which writing has to start
        cv2.FONT_HERSHEY_SIMPLEX, #font family
        0.5, #font size
        (0, 0, 0, 255), #font color
        1) #font stroke

    cv2.imwrite('output.png', image)

def citation_img(c_type, wrong=0):
    if c_type == "warning":
        image = cv2.imread('images/passports/warning-citation.png', cv2.IMREAD_UNCHANGED)
    elif c_type == "last":
        image = cv2.imread('images/passports/last-warning-citation.png', cv2.IMREAD_UNCHANGED)
    else:
        image = cv2.imread('images/passports/penalty-citation.png', cv2.IMREAD_UNCHANGED)

if __name__ == "__main__":
    data = random_info()
    passport_img("united-federation")