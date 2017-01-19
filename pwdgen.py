from random import randint


def gen_pwd():
    chars = "12345qwertasdfgzxcvb!@#$%QWERTASDFGZXCVB"
    password = ""
    for n in range(randint(7, 11)):
        password = password + chars[randint(0, (len(chars) - 1))]
    return password


if __name__ == "__main__":
    print(gen_pwd())
