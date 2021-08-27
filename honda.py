import RPi.GPIO as io
import time

UNLK = 16
LOCK = 12
TRUNK = 19
HORN = 21
PLIGHTS = 6
START = 22
DOME = 20
ACC = 23
IGN = 27
BUTTON = 5

# Index  0      1     2      3      4       5      6    7    8      9
gpio = [UNLK, LOCK, TRUNK, HORN, PLIGHTS, START, DOME, ACC, IGN, BUTTON]

io.setwarnings(False)
io.setmode(io.BCM)

for x in range(0, 10): # Set BUTTON as an input, all other channels as outputs
  if x < 9:
    io.setup(gpio[x], io.OUT)
    if x < 6:
      io.output(gpio[x], 1) # Set outputs UNLK, LOCK, TRUNK, HORN, PLIGHTS, START as HIGH
    if x >= 6:
      io.output(gpio[x], io.input(gpio[x])) # Set DOME, ACC, IGN according to input value
  else:
    io.setup(gpio[x], io.IN, io.PUD_UP)


def activate(pin):
  io.output(pin, 0)
  time.sleep(.1)
  io.output(pin, 1)

def toggle(pin):
  io.output(pin, not io.input(pin))

def check(pin):
  result = io.input(pin)
  return result

def full_check():
  for x in gpio:
    print("(GPIO " + str(x) + ") = " + str(io.input(x)))

def lock():
  activate(LOCK)
  with open("lockstat", "r") as lockstat:
    if '0' in lockstat.read():
      io.output(PLIGHTS, 0)
      time.sleep(.6)
      io.output(PLIGHTS, 1)
      print("Car Locked")
      with open("lockstat", "w") as lockstat:
        lockstat.write("LOCKED = 1")
    else:
      print("Car Already Locked")

def unlock():
  activate(UNLK)
  with open("lockstat", "r") as lockstat:
    if '1' in lockstat.read():
      io.output(PLIGHTS, 0)
      time.sleep(.6)
      io.output(PLIGHTS, 1)
      time.sleep(.7)
      io.output(PLIGHTS, 0)
      time.sleep(.7)
      io.output(PLIGHTS, 1)
      print("Car Unlocked")
      with open("lockstat", "w") as lockstat:
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
  if not check(DOME):
    print("Dome Light On.")
  if check(DOME):
    print("Dome Light Off.")

def acc():
  toggle(ACC)
  if not check(ACC):
    print("Accessory On.")
  if check(ACC):
    print("Accessory Off.")

def ign():
  toggle(IGN)
  if not check(IGN):
    print("Ignition On.")
  if check(IGN):
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
  for x in range(0, 9):
    io.output(gpio[x], 1)
  print("All Systems Off.")
