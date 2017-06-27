import random

names = ['apple']

print(len(names))

def fruits():
    print('apple')
    print('oranges')
    print('pears')

fruits()

boots = ['apple', 'cheese', 'cake', 'pear']

for x in range(1,6):
    print("Rob")

for x in boots:
    print(x)

for x in range(0,21,2):
    print(x)

username = "admin"
password = "admin123"

if username == "admin" and password == "admin123":
    print("valid user")
else:
    print("invalid user")

if username == "admin" or password == "admin123":
    print("valid user")
else:
    print("invalid user")

counter = 0
while counter <= 10:
    print(counter)
    counter += 1




food = ["potato", "greens", "pizza", "banana"]

print(food[2])

food.append("cheese")

print(food)

food.insert(2, "tacos")

print(food)


for x in range(5):
    print("I am a programmer")


def display_square():
    for i in range(1,10):
        print(i**2)
display_square()

def add(a, b):
    c = a + b
    return c

result = add(100, 200)
print(result)


def add(a, b):
    return a + b

def square(c):
    return c * c

result = square(add(2, 3))
print(result)


for x in range(5):
    result = random.randint(1, 6)
    print(result)
