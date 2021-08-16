from honda import unlock, lock, trunk, dome, horn, acc, ign, start, kill
from thermometer import read_temp

while True:
    print("----------------")
    print("2001 Honda Accord LX:")
    print("(u) Unlock")
    print("(l) Lock")
    print("(t) Trunk Release")
    print("(d) Dome Light")
    print("(h) Horn")
    print("(a) Accessory (I)")
    print("(i) Ignition (II)")
    print("(s) Start (III)")
    print("(f) Temperature")
    print("(o) Off")
    print("(x) Exit" )
    print("----------------")
    kb = input('Enter command: ')

# Lock/Unlock
    if kb == "u":
        unlock()
    if kb == 'unlock':
        unlock()
    if kb == 'l':
        lock()
    if kb == 'lock':
        lock()

# Trunk Release
    if kb == 't':
        trunk()
    if kb == 'trunk':
        trunk()

# Dome Light (On/Off)
    if kb == 'd':
        dome()
    if kb == 'dome':
        dome()

# Horn
    if kb == 'h':
        horn()
    if kb == 'horn':
        horn()

# Accessory (On/Off)
    if kb == 'a':
        acc()
    if kb == 'acc':
        acc()

# Ignition (On/Off)
    if kb == 'i':
        ign()
    if kb == 'ign':
        ign()

##### START #####
    if kb == 's':
        start()
    if kb == 'start':
        start()

##### TEMP #####
    if kb == 'f':
        read_temp()
    if kb == 'temp':
        read_temp()

##### OFF #####
    if kb == 'o':
        kill()
    if kb == 'off':
        kill()

##### EXIT #####
    if kb == 'x':
        exit()
    if kb == 'exit':
        exit()
