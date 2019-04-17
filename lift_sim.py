import sys
from time import sleep

def _print(string):
    sys.stdout.write(string)
    sys.stdout.flush()

class CentralSystem():

    def __init__(self):

        #Create a List of Lift and initialize a list of floor to maintain Lifts in that floor
        #Initialize all lifts at floor 0

        self.lifts = [Lift(i) for i in range(3)]
        self.floors = [[] for _ in range(30)]
        self.floors[0] = self.lifts[:]

    """ Functio to check the validation of floor """
    def is_valid_floor(self, floor):

        if floor >= 30:
            raise ValueError("Invalid floor {}, building "
                             "have {} floors.".format(floor, 30))

    """ Based on the lifts present on the floor, we'll select the lift"""
    def select_lift(self, lifts, direction):

        chosen_lifts = [lift for lift in lifts if
                                lift.direction is None]

        if not chosen_lifts:
            chosen_lifts = lifts

        return chosen_lifts[0];


    """ Function to be invoked when a person presses button from outside the Lift"""
    def call_lift(self, floor, direction):

        self.is_valid_floor(floor)
        if direction not in (1, -1):
            raise ValueError("direction only accepts 1 or -1, Invalid Entry{}".
                                                        format(direction))
        if(floor == 0 and direction == -1):
            print("Invalid Entry: Lift can't go DOWN")
            return None

        if(floor == 29 and direction == 1):
            print("Invalid Entry: Lift can't go UP")
            return None

        if self.floors[floor]:
            lift = self.select_lift(self.floors[floor], direction)
            lift.open()
            return lift

        check_floors = map(None, range(floor + 1, len(self.floors)),
                                 range(floor - 1, -1, -1))
        for up, down in check_floors:
            if down is not None and self.floors[down]:
                lift = self.select_lift(self.floors[down], direction)
                break
            if up is not None and self.floors[up]:
                lift = self.select_lift(self.floors[up], direction)
                break

        self.start_lift(lift, floor)
        return lift

    def start_lift(self, lift, floor):

        self.is_valid_floor(floor)
        print("Lift {} chosen".format(lift.num))

        move_up = lift.floor < floor
        lift.direction = 1 if move_up else -1

        for _ in (range(lift.floor, floor) if move_up
                            else range(lift.floor, floor, -1)):
            lift.move(self)

        print("")
        lift.open()
        lift.direction = None

class Lift():

    def __init__(self, num):

        self.floor = 0
        self.num = num
        self.direction = None

    def open(self):
        print ("Opening lift {}.".format(self.num))

    def close(self):
        print ("Closing lift {}.".format(self.num))

    def move(self, system):

        system.floors[self.floor].remove(self)
        self.floor += self.direction
        system.floors[self.floor].append(self)

        _print("Floor {} ".format(self.floor))
        sleep(0.1)
        _print("=")
        sleep(0.1)
        _print("=")
        sleep(0.1)
        _print("=")
        sleep(0.1)
        _print("> ")
