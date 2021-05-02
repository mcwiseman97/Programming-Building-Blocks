from array import *
import random

print("\n")
print("Please enter the following: ")
print("\n")

adj = input("Adjectve: ")
animal = input("Animal: ")
#verbOne = input("Verb One: ")
#verbTwo = input("Verb Two: ")
#verbThree = input("Verb Three: ")
exclamation = input("Exclamation: ")


verb = [" ", "run", "walk", "skate", "fly", "prance", "float", "cry"]
for x in range(10):
    a = random.randint(1,8)
    b = random.randint(1,8)
    c = random.randint(1,8)

    
print("\n")
print("The other day, I was really in trouble. It all started when I saw a very " + adj + " " + animal + " " + verb[a] + " down the hallway. \n" + exclamation + "! I yelled. But all I could think to do was to " + verb[b] + " over and over. Miraculously, that caused it to stop, \nbut not before it tried to " + verb[c] + " right in front of my family.")
print("\n")


