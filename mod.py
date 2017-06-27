import random

for x in range(5):
    result = random.randint(1, 6)
    print(result)


def calc_bmi(w, h):
    return w/h**2

weight = int(input('How much do you weigh?'))
height = int(input('How tall are you?'))
bmi = calc_bmi(weight, height)
print(bmi)