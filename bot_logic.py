import random

def gen_pass(pass_lenght):
    elements = "abcdefg"
    password = ""

    for i in range(pass_lenght):
        password += random.choice(elements)

    return password