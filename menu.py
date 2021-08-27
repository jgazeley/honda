import honda
from finger_module import finger_menu
from thermometer import read_temp

while True:
    print("----------------")
    print("2001 Honda Accord LX:")
    print("(u) UNLK")
    print("(l) LOCK")
    print("(t) TRUNK")
    print("(d) DOME")
    print("(h) HORN")
    print("(a) ACC")
    print("(i) IGN")
    print("(s) START")
    print("(c) TEMP")
    print("(f) FINGER")
    print("(g) GPIO")
    print("(o) OFF")
    print("(x) EXIT" )
    print("----------------")
    key = input('Enter command: ')

    if key == 'u' or key == 'unlock' or key == 'U' or key == 'UNLK' or key == 'UNLOCK':
        honda.unlock()

    if key == 'l' or key == 'lock' or key == 'L' or key == 'LOCK':
        honda.lock()

    if key == 't' or key == 'trunk' or key == 'T' or key == 'TRUNK':
        honda.trunk()

    if key == 'd' or key == 'dome' or key == 'D' or key == 'DOME':
        honda.dome()

    if key == 'h' or key == 'horn' or key == 'H' or key == 'HORN':
        honda.horn()

    if key == 'a' or key == 'acc' or key == 'A' or key == 'ACC':
        honda.acc()

    if key == 'i' or key == 'ign' or key == 'I' or key == 'IGN':
        honda.ign()

    if key == 's' or key == 'start' or key == 'S' or key == 'START':
        honda.start()

    if key == 'temp' or key == 'TEMP' or key == 'c' or key == 'C':
        read_temp()

    if key == 'f' or key == 'enroll' or key == 'F' or key == 'ENROLL' or key == 'finger' or key == 'FINGER':
        finger_menu()

    if key == 'g' or key == 'G' or key == 'GPIO' or key == 'gpio':
        honda.full_check()

    if key == 'o' or key == 'off' or key == 'O' or key == 'OFF':
        honda.kill()

    if key == 'x' or key == 'exit' or key == 'X' or key == 'EXIT':
        exit()
