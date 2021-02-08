print(30 * "-")
print("Hello, Welcome to The Quarentine shop, Whe are here to help!")
print(30 * "-")
print("What are you looking for today?")

import pickle
import os
os.system("clear")

print(30 * "-")
print("  Items  ")
print(30 * '-')
print(" 1 - Masks -")
print(" 2 - Toilet Paper -")
print(" 3 - Hand Sanitizer -")
print(" 4 - Twinkies -")
print(30 * "-")

import pickle
import os
os.system("clear")

print(" 0-DATA PASSCODE ")

tp = [0]
masks = [0]
twink = [0]
hs = [0]

selection = input('Enter your choice [1-4] : ')

selection = int(selection)

if selection == 1:
    print()
    print ("Best way to Keep Yourself safe from Coronavirus!")
    print()
    print("Thats going to be $250")
    print()
    x = input('If you want to purchase this press [1]')
    x = int(x)
    if x == 1:
        print("Thank you for your purchase")
        masks = masks +1
        
        

    else:
        print()

          
elif selection == 2:
    print ("So Youre the one thats been hording all the toilet paper")
    print()
    print("you cant find this anywhere so $50 a roll")
    print()
    y = input('If you want to purchase this press[1]')
    y = int(y)
    if y == 1:
        print("Thank you for your purchase")
        tp = (tp+[1])
        pickle.dump(tp, open("tp.dat","wb"))
elif selection == 3:
    print ("Dont sell this on ebay")
    print()
    print("these are $10")
    print()
    y = input('If you want to purchase this press[1]')
    y = int(y)
    if y == 1:
        print("Thank you for your purchase")
elif selection == 4:
    print("Gotta have the twinkies when theres a global emergency!")
    print()
    print("Thats going to be $100 a box")
    print()
    y = input('If you want to purchase this press[1]')
    y = int(y)
    if y == 1:
        print("Thank you for your purchase")

elif selection == 0:
    password = input("password")
    if password == ('Pythonrocks'):
        print("Youre either the boss or the worlds best professor! either way, WELCOME")
        print()
        choice = input('What info would you like? TP, MASKS, HS,TWINK')
        if choice == 'MASKS':
              print(masks)
        elif choice == 'TP':
              print(tp)
        elif choice == 'HS':
              print(hs)
        elif choice == 'TWINK':
              print(twink)
else:    
    print ("Im sorry but thats all we have at the moment")
        
