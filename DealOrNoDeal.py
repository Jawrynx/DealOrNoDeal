import random
import time
import math
import sys

num = 22
BoxList = []
numbers = [i for i in range(1, 23)]
values = ["1p", "10p", "50p", "£1", "£5", "£10", "£50", "£100", "£250", "£500", "£750", "£1,000", "£2,000", "£3,000", "£4,000", "£5,000", "£7,500", "£10,000", "£25,000", "£50,000", "£75,000", "£100,000"]

class player():
    def __init__(self, name):
        self.name = name
class host():
    def __init__(self, name='Host'):
        self.name = name
    def spawn():
        print("Hello and Welcome to DEAL OR NO DEAL!")
        print("Created by JAWRYNX \n ...")
        time.sleep(1)
    def getName():
        name = input("Please Enter Your Name: ")
        print("Hello {name}! Shall we get started?".format(name=name))
        return name       

class box():
    def __init__(self, number, value):
        self.number = number
        self.value = value
        self.boxOpen = False

class dealer():
    def offer(values, numbers):
        print("...\n...\n...\nThe Dealer Is Calling!\n...\n...\n...")
        time.sleep(1)
        valuesConverted = game.convertValues(values)
        highestValue = valuesConverted[-1]
        offerconversion = highestValue / len(numbers)
        Offer = int(math.ceil(offerconversion / 100)) * 100
        if Offer >= 1000 & Offer < 10000:
            strOffer = str(Offer)
            formatOffer = strOffer[:1] + "," + strOffer[1:]
        elif Offer >= 10000:
            strOffer = str(Offer)
            formatOffer = strOffer[:2]  + "," + strOffer[2:]
        else:
            formatOffer = str(Offer)

        print("The Dealer has offered you £{offer}! Do you wish to accept his offer? Type 'Y' or 'N' below to decide!".format(offer=formatOffer))
        decision = input()
        if decision == 'Y':
            print("Very well, you have accepted the Dealers Offer and won £{offer}! Thank you for playing Deal Or No Deal!".format(offer=formatOffer))
            time.sleep(3)
            print("EXITING GAME!")
            time.sleep(3)
            sys.exit()
        else:
            return



class game():
    def convertValues(values):
        strippedPence = [i.strip("p") for i in values]
        strippedPound = [i.strip("£") for i in strippedPence]
        strippedComma = [i.replace(",", "") for i in strippedPound]
        integerValues = [int(i) for i in strippedComma]
        return integerValues

    def spawnBoxes():
        values = ["1p", "10p", "50p", "£1", "£5", "£10", "£50", "£100", "£250", "£500", "£750", "£1,000", "£2,000", "£3,000", "£4,000", "£5,000", "£7,500", "£10,000", "£25,000", "£50,000", "£75,000", "£100,000"]
        Boxes = []
        for i in range(1, 23):
            val = random.choice(values)
            Boxes.append(box(i, val))
            values.remove(val)
        return Boxes
    
    def round():
        BoxList = game.spawnBoxes()
        numbers = [i for i in range(1, 23)]
        values = ["1p", "10p", "50p", "£1", "£5", "£10", "£50", "£100", "£250", "£500", "£750", "£1,000", "£2,000", "£3,000", "£4,000", "£5,000", "£7,500", "£10,000", "£25,000", "£50,000", "£75,000", "£100,000"]
        while len(BoxList) != 0:
            if len(BoxList) == 16:
                dealer.offer(values, numbers)
            if len(BoxList) == 12:
                dealer.offer(values, numbers)
            if len(BoxList) == 8:
                dealer.offer(values, numbers)
            if len(BoxList) == 4:
                dealer.offer(values, numbers)
            if len(BoxList) == 2:
                dealer.offer(values, numbers)
            if len(BoxList) == 1:
                prizeBox = values[0]
                print("Congratulations! You have won {prize}!".format(prize=prizeBox))
                time.sleep(3)
                print("...\n...\n...\nThank You For Playing!\nEXITING GAME!\n...\n...\n...")
                time.sleep(3)
                sys.exit()
            print(numbers)
            print(values)
            print("Select a number from above!")
            selection = input()
            if int(selection) in numbers:
                for i in BoxList:
                    if i.number == int(selection):
                        print("You have removed {value} from the playing field!".format(value=i.value))
                        values.remove(i.value)
                        numbers.remove(i.number)
                        BoxList.remove(i)
            else:
                print("Error!")
    def start():
        Host = host
        Host.spawn()
        Player = player(Host.getName())
        time.sleep(1)
        BoxList = game.spawnBoxes()
        game.round()

game.start()