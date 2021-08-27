from honda import IGN, BUTTON, check, car_on, start, kill
from finger_module import finger_OK

kill()

def get_button():
    result = (not check(BUTTON))
    return result

while True:

    button_on = get_button()

    if button_on:
        if check(IGN):
            car_on()
        if finger_OK():
            start()
            while button_on:
                button_on = get_button()

        if get_button() == 0:
            kill()
