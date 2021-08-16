from honda import io

print("UNLK (GPIO16): " + str(io.input(16)))
print("LOCK (GPIO12): " + str(io.input(12)))
print("TRUNK (GPIO19): " + str(io.input(19)))
print("DOME (GPIO20): " + str(io.input(20)))
print("HORN (GPIO21): " + str(io.input(21)))
print("PLIGHTS (GPIO06): " + str(io.input(6)))
print("ACC (GPIO23): " + str(io.input(23)))
print("IGN (GPIO27): " + str(io.input(27)))
print("START (GPIO22): " + str(io.input(22)))

