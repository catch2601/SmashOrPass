import time
import os
import colorama
import ctypes
import pyfiglet


from pick import pick
from playsound import playsound
from PIL import Image
os.system('color')
from colorama import Fore


title = pyfiglet.figlet_format("SMASH or PASS")
print(Fore.RED + "THIS GAME IS NSFW!!!!")
print(Fore.WHITE + title)
print("Welcome to a game where you are shown a Roblox Avatar and then have to choose whether you would smash it, or if you would pass.")
input("Press enter to continue!")
print("                                                ")


# ROUND ONE
title = pyfiglet.figlet_format("ROUND ONE")
print(Fore.WHITE + title)
print("                                                ")
print("Would you " + Fore.GREEN + "SMASH" + Fore.WHITE + " or " + Fore.RED + "PASS")
img = Image.open("avatars\oneone.png")
img.show()
print(Fore.WHITE + "Please select from the new window!")


title = 'SMASH OR PASS:'
options = ['SMASH', 'PASS']

option, index = pick(options, title, indicator='=>', default_index=0)

print("                                                ")
if option == 'SMASH':
    print("You choose to " + Fore.GREEN + "SMASH" + Fore.WHITE + " that avatar! ")
    round_one = "You choose to " + Fore.GREEN + "SMASH" + Fore.WHITE + " that avatar! "
else:
    print("You choose to " + Fore.RED + "PASS" + Fore.WHITE + " that avatar! ")
    round_one = "You choose to " + Fore.RED + "PASS" + Fore.WHITE + " that avatar! "

input("Press enter to continue to the next round!")
print("                                                ")


# ROUND TWO
title = pyfiglet.figlet_format("ROUND TWO")
print(Fore.WHITE + title)
print("                                                ")
print("Would you " + Fore.GREEN + "SMASH" + Fore.WHITE + " or " + Fore.RED + "PASS")
img = Image.open("avatars\onetwo.png")
img.show()
print(Fore.WHITE + "Please select from the new window!")


title = 'SMASH OR PASS:'
options = ['SMASH', 'PASS']

option, index = pick(options, title, indicator='=>', default_index=0)

print("                                                ")
if option == 'SMASH':
    print("You choose to " + Fore.GREEN + "SMASH" + Fore.WHITE + " that avatar! ")
    round_two = "You choose to " + Fore.GREEN + "SMASH" + Fore.WHITE + " that avatar! "
else:
    print("You choose to " + Fore.RED + "PASS" + Fore.WHITE + " that avatar! ")
    round_two = "You choose to " + Fore.RED + "PASS" + Fore.WHITE + " that avatar! "

input("Press enter to continue to the next round!")
print("                                                ")


# ROUND THREE
title = pyfiglet.figlet_format("ROUND THREE")
print(Fore.WHITE + title)
print("                                                ")
print("Would you " + Fore.GREEN + "SMASH" + Fore.WHITE + " or " + Fore.RED + "PASS")
img = Image.open("avatars\onethree.png")
img.show()
print(Fore.WHITE + "Please select from the new window!")


title = 'SMASH OR PASS:'
options = ['SMASH', 'PASS']

option, index = pick(options, title, indicator='=>', default_index=0)

print("                                                ")
if option == 'SMASH':
    print("You choose to " + Fore.GREEN + "SMASH" + Fore.WHITE + " that avatar! ")
    round_three = "You choose to " + Fore.GREEN + "SMASH" + Fore.WHITE + " that avatar! "
else:
    print("You choose to " + Fore.RED + "PASS" + Fore.WHITE + " that avatar! ")
    round_three = "You choose to " + Fore.RED + "PASS" + Fore.WHITE + " that avatar! "

input("Press enter to continue to the next round!")
print("                                                ")



# ROUND FOUR
title = pyfiglet.figlet_format("ROUND FOUR")
print(Fore.WHITE + title)
print("                                                ")
print("Would you " + Fore.GREEN + "SMASH" + Fore.WHITE + " or " + Fore.RED + "PASS")
img = Image.open("avatars\onefour.png")
img.show()
print(Fore.WHITE + "Please select from the new window!")


title = 'SMASH OR PASS:'
options = ['SMASH', 'PASS']

option, index = pick(options, title, indicator='=>', default_index=0)

print("                                                ")
if option == 'SMASH':
    print("You choose to " + Fore.GREEN + "SMASH" + Fore.WHITE + " that avatar! ")
    round_four = "You choose to " + Fore.GREEN + "SMASH" + Fore.WHITE + " that avatar! "
else:
    print("You choose to " + Fore.RED + "PASS" + Fore.WHITE + " that avatar! ")
    round_four = "You choose to " + Fore.RED + "PASS" + Fore.WHITE + " that avatar! "

input("Press enter to continue to the next round!")
print("                                                ")


# ROUND FIVE
title = pyfiglet.figlet_format("ROUND FIVE")
print(Fore.WHITE + title)
print("                                                ")
print("Would you " + Fore.GREEN + "SMASH" + Fore.WHITE + " or " + Fore.RED + "PASS")
img = Image.open("avatars\onefive.png")
img.show()
print(Fore.WHITE + "Please select from the new window!")


title = 'SMASH OR PASS:'
options = ['SMASH', 'PASS']

option, index = pick(options, title, indicator='=>', default_index=0)

print("                                                ")
if option == 'SMASH':
    print("You choose to " + Fore.GREEN + "SMASH" + Fore.WHITE + " that avatar! ")
    round_five = "You choose to " + Fore.GREEN + "SMASH" + Fore.WHITE + " that avatar! "
else:
    print("You choose to " + Fore.RED + "PASS" + Fore.WHITE + " that avatar! ")
    round_five = "You choose to " + Fore.RED + "PASS" + Fore.WHITE + " that avatar! "

input("Press enter to continue to the results!")
print("                                                ")
print("                                                ")
print("                                                ")
print("                                                ")
print("                                                ")
print("                                                ")
print("                                                ")
print("                                                ")
print("                                                ")
print("                                                ")
print("                                                ")
print("                                                ")
print("                                                ")
print("                                                ")
print("                                                ")
print("                                                ")
print("                                                ")



# RESULTS
title = pyfiglet.figlet_format("RESULTS")
print(Fore.WHITE + title)
print("Thank you for playing " + Fore.GREEN + "SMASH" + Fore.WHITE + " or " + Fore.RED + "PASS")
print(Fore.WHITE + "Your results are listed below:")
print("                                                ")
print("ROUND ONE: " + round_one)
print("ROUND TWO: " + round_two)
print("ROUND THREE: " + round_three)
print("ROUND FOUR: " + round_four)
print("ROUND FIVE: " + round_five)

time.sleep(30)






