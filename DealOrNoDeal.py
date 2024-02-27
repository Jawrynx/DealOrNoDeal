import random
import time

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

class game():
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
            print(numbers)
            print(values)
            print("Select a number from above!")
            selection = input()
            for i in BoxList:
                if i.number == int(selection):
                    print("You have removed {value} from the playing field!".format(value=i.value))
                    values.remove(i.value)
                    numbers.remove(i.number)
                    BoxList.remove(i)

    def start():
        Host = host
        Host.spawn()
        Player = player(Host.getName())
        time.sleep(1)
        BoxList = game.spawnBoxes()
        game.round()
            


game.start()
        