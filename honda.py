import RPi.GPIO as io
import time

# GPIO Assignments #
UNLK = 16
LOCK = 12
TRUNK = 19
DOME = 20
HORN = 21
PLIGHTS = 6
ACC = 23
IGN = 27
START = 22

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

io.output(UNLK, 1)
io.output(LOCK, 1)
io.output(TRUNK, 1)
io.output(DOME, 1)
io.output(HORN, 1)
io.output(PLIGHTS, 1)
io.output(ACC, 1)
io.output(IGN, 1)
io.output(START, 1)

# Lock/Unlock #
def lock():
    io.output(LOCK, 0)
    time.sleep(.1)
    io.output(LOCK, 1)
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
    io.output(UNLK, 0)
    time.sleep(.1)
    io.output(UNLK, 1)
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

# # Trunk #
def trunk():
    io.output(TRUNK, 0)
    time.sleep(.1)
    io.output(TRUNK, 1)
    print("Trunk Release Activated.")

# Horn #
def horn():
    io.output(HORN, 0)
    time.sleep(.1)
    io.output(HORN, 1)
    print("Horn Activated")

# Dome Light (On/Off) #
def dome():
    io.output(DOME, not io.input(DOME))
    if io.input(DOME) == 0:
        print("Dome Light On.")
    if io.input(DOME) == 1:
        print("Dome Light Off.")

# # Accessory (On/Off) #
def acc():
    io.output(ACC, not io.input(ACC))
    if io.input(ACC) == 0:
        print("Accessory On.")
    if io.input(ACC) == 1:
        print("Accessory Off.")

# Ignition (On/Off) #
def ign():
    io.output(IGN, not io.input(IGN))
    if io.input(IGN) == 0:
        print("Ignition On.")
    if io.input(IGN) == 1:
        print("Ignition Off.")

# Start #
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
