import time , os
from pynput import keyboard as kla
from pynput.keyboard import Key, Controller
from pynput import mouse as my
from pynput.mouse import Button

my = my.Controller()
kl = kla.Controller()

kldelay = 0.1
mydelay = 0.1
tlacitko = ""

acjede = True
kcjede = True
akjede = True

def maz():
    os.system("cls")

def konec(key):
    global acjede
    global kcjede
    global akjede
    if key == kla.Key.esc:
        acjede = False
        kcjede = False
        akjede = False
        return False
        
def ac():
    global kldelay
    while acjede:
        my.press(Button.left)
        my.release(Button.left)
        time.sleep(float(kldelay))
        
def kc():
    global mydelay
    global tlacitko
    while kcjede:
        kl.press(tlacitko)
        kl.release(tlacitko)
        time.sleep(float(mydelay))
        
def ak():
    while akjede:
        kl.press("w")
        kl.release("w")
        time.sleep(1)
        kl.press("a")
        kl.release("a")
        time.sleep(1)
        kl.press("s")
        kl.release("s")
        time.sleep(1)
        kl.press("d")
        kl.release("d")
        time.sleep(1)
        my.move(10, 10)
        time.sleep(1)
        my.move(-10, -10)
        time.sleep(1)

def autoclicker():
    global kldelay
    kldelay = input("Enter click delay (default is 0.1s): ")
    if kldelay == "":
        kldelay = 0.1
    else:
        kldelay = float(kldelay)

    print(f"Your delay is {kldelay}s | Starting in 5 seconds")
    for i in range(6):
        time.sleep(1)
        print(i)
    ac()


def keyclicker():
    global mydelay
    global tlacitko
    mydelay = input("Enter key delay (default is 0.1s): ")
    if mydelay == "":
        mydelay = 0.1
    else:
        mydelay = float(mydelay)

    tlacitko = input("Enter key to spam: ")
    maz()
    print(f"Delay: {mydelay}s | Key: {tlacitko} | Starting in 5 seconds")
    
    for i in range(6):
        time.sleep(1)
        print(i)

    print("Press ESC to stop the program")
    kc()
    
def antikick():
    for i in range(4):
        print("This program will simulate WASD movement and mouse movement")

    souhlas = input("Do you want to start this program? (1 = yes / 2 = no): ")
    if souhlas == "1":
        print("Starting in 5 seconds")
        for i in range(6):
            time.sleep(1)
            print(i)

        print("Press ESC to stop the program")
        ak()

    elif souhlas == "2":
        print("Returning to menu...")
        time.sleep(2)
        maz()
        otazecka()
        

def otazecka():
    print("1 | Auto Clicker")
    print("2 | Key Clicker")
    print("3 | Anti AFK Movement")
    print("END | Exit tool")

    otazka = input("Choose option: ")

    if otazka == "":
        print("Please choose a valid option")
        time.sleep(2)
        maz()
        otazecka()

    elif otazka == "1":
        autoclicker()

    elif otazka == "2":
        keyclicker()

    elif otazka == "3":
        antikick()

    elif otazka.lower() == "end":
        print("Exiting program...")
        time.sleep(2)


if __name__ == "__main__":
    while True:
        listener = kla.Listener(on_press=konec)
        listener.start()
        otazecka()
        listener.join()