import RPi.GPIO as io
import time

UNLK = 16
LOCK = 12
TRUNK = 19
DOME = 20
HORN = 21
PLIGHTS = 6
ACC = 23
IGN = 27
START = 22
BUTTON = 5

io.setwarnings(False)
io.setmode(io.BCM)
io.setup(UNLK, io.OUT)
io.setup(LOCK, io.OUT)
io.setup(TRUNK, io.OUT)
io.setup(DOME, io.OUT)
io.setup(HORN, io.OUT)
io.setup(PLIGHTS, io.OUT)
io.setup(ACC, io.OUT)
io.setup(IGN, io.OUT)
io.setup(START, io.OUT)
io.setup(BUTTON, io.IN, io.PUD_UP)
io.output(UNLK, 1)
io.output(LOCK, 1)
io.output(TRUNK, 1)
io.output(DOME, io.input(DOME))
io.output(HORN, 1)
io.output(PLIGHTS, 1)
io.output(ACC, io.input(ACC))
io.output(IGN, io.input(IGN))
io.output(START, 1)

def activate(pin):
    io.output(pin, 0)
    time.sleep(.1)
    io.output(pin, 1)

def toggle(pin):
    io.output(pin, not io.input(pin))

def check(pin):
    result = (io.input(pin))
    return result

def full_check():
    print("UNLK    (GPIO16): | " + str(io.input(16)) + " |")
    print("LOCK    (GPIO12): | " + str(io.input(12)) + " |")
    print("TRUNK   (GPIO19): | " + str(io.input(19)) + " |")
    print("DOME    (GPIO20): | " + str(io.input(20)) + " |")
    print("HORN    (GPIO21): | " + str(io.input(21)) + " |")
    print("PLIGHTS (GPIO06): | " + str(io.input(6)) + " |")
    print("ACC     (GPIO23): | " + str(io.input(23)) + " |")
    print("IGN     (GPIO27): | " + str(io.input(27)) + " |")
    print("START   (GPIO22): | " + str(io.input(22)) + " |")
    print("BUTTON  (GPIO05): | " + str(io.input(5)) + " |")

def lock():
    activate(LOCK)
    with open("lockstat.txt", "r") as lockstat:
        if '0' in lockstat.read():
            io.output(PLIGHTS, 0)
            time.sleep(.6)
            io.output(PLIGHTS, 1)
            print("Car Locked")
            with open("lockstat.txt", "w") as lockstat:
                lockstat.write("LOCKED = 1")
        else:
            print("Car Already Locked")

def unlock():
    activate(UNLK)
    with open("lockstat.txt", "r") as lockstat:
        if '1' in lockstat.read():
            io.output(PLIGHTS, 0)
            time.sleep(.6)
            io.output(PLIGHTS, 1)
            time.sleep(.7)
            io.output(PLIGHTS, 0)
            time.sleep(.7)
            io.output(PLIGHTS, 1)
            print("Car Unlocked")
            with open("lockstat.txt", "w") as lockstat:
                lockstat.write("LOCKED = 0")
        else:
            print("Car Already Unlocked")

def trunk():
    activate(TRUNK)
    print("Trunk Release Activated.")

def horn():
    activate(HORN)
    print("Horn Activated")

def dome():
    toggle(DOME)
    if io.input(DOME) == 0:
        print("Dome Light On.")
    if io.input(DOME) == 1:
        print("Dome Light Off.")

def acc():
    toggle(ACC)
    if io.input(ACC) == 0:
        print("Accessory On.")
    if io.input(ACC) == 1:
        print("Accessory Off.")

def ign():
    toggle(IGN)
    if io.input(IGN) == 0:
        print("Ignition On.")
    if io.input(IGN) == 1:
        print("Ignition Off.")

def car_on():
    io.output(ACC, 0)
    io.output(IGN, 0)
    print("Accessory and Ignition On.")

def start():
    io.output(IGN, 0)
    io.output(ACC, 1)
    time.sleep(1)
    io.output(START, 0)
    time.sleep(.8)
    io.output(START, 1)
    time.sleep(.3)
    io.output(ACC, 0)
    print("Car Started.")

def kill():
    io.output(DOME, 1)
    io.output(ACC, 1)
    io.output(IGN, 1)
    print("All Systems Off.")
