print ("Hello, my name is Barista-06, and I am a huge fan of the Lord of the Rings.")

name = input ("\nWhat is your name? ")

if name == "Evil Ben" or name == "Carma":
    evil = input ("Are you evil, " + name + "? ")
    if evil == "yes" or evil == "Yes":
        gooddeeds = int(input ("How many good deeds have you done in the past week? "))
        if gooddeeds < 4:
            print ("You're not welcome here, " + name + ".")
            input ("You must leave")
            exit ()
        else: 
            print ("\nBeep - boop \n\nBehavior override approved.")
    else:
        print ("\nBeepBeep - Boop\n\n...approved...I love you")
elif name == "Gandalf" or name == "Frodo":
    print ("Oh, wow. I love you in The Lord of the Rings, " + name + ". Sorry, I will be professional now.")
else:
    print ("\nBeep - Boop")

menu = "bananas, water, coffee, latte and frappuccino"

order = input ("\nHello, " + name + ". Thank you for coming in today. We are offering " + menu + " today. \nWhat would you like? ")

if order == "Chai" or order == "chai":
    price = 4
elif order == "frappuccino":
    price = 8
elif order == "water":
    price = 1
elif order == "banana":
    price =3
else:
    price =5

if order == "water" or order == "coffee" or order == "banana":
    print ("\nAbsolutely. Our " + order + " is $" + str(price) + ".")
elif order == "Latte" or order == "latte":
    print ("\nI can happily get that put together for you.")
    whip = input ("Would you like some whipped cream on that Latte for $2 more? ")
    if whip == "yes" or whip == "YES" or whip == "Yes" or whip == "Yes, please":
        price = 7
    else:
        price = 5
else:
    print ("\nGreat! We don't normally offer " + order + " but I am happy to make an exception for you, " + name +". \n\nThose are $" + str(price) + ".")
    
number = int(input ("\nHow many do you want? "))

total = number * price

if name == "Gandalf" or name == "Frodo":
    total = (total * .90)
    input ("\nBeep - Beep - Boop \n\nThat's coming out to $" + str(total) + ", and I am making sure you get the LOTR discount. \nDo you want to pay with cash or card? ")
else:
    input ("\nBeep - Beep - Boop \n\nThat's coming out to $" + str(total) + ". \nDo you want to pay with cash or card? ")
print ("\nSounds good, " + name + ". I can get working on those " + str(number) + " " + order + "s right away. \nIt should be ready in 5 minutes.\nSee you then and thank you for choosing to shop with us.\n")
input ("Later!")
exit ()
