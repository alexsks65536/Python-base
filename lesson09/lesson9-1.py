import time
import itertools
'''
######################## первый вариант

class TrafficLight:

    color = ''

    def running(self):
        color = {'Red': 7, 'Yellow': 2, 'Green': 5}
        for col, sek in color.items():

            print(f"Color: {col}")
            s = time.sleep(sek)

s  = TrafficLight()
s.running()
'''

#####################    второй вариант

class TrafficLight:
    paint = [['red', [7, 31]], ['yellow', [2, 33]], ['green', [7, 32]], ['yellow', [2, 33]]]

    def running(self):
        for flash in itertools.cycle(self.paint):
            print(f"\r\033[{flash[1][1]}m\033[1m{flash[0]}\033[0m", end="")
            time.sleep(flash[1][0])

s = TrafficLight()
s.running()