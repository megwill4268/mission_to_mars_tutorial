import sys


class Shuttle(object):
    def __init__(self):
        self.speed = 1000                 # speed shuttle is moving at
        self.fuel = 100                   # perceent of fuel in shuttle
        self.structural_integrity = 100   # percent structural integrity left
        self.speed_alteration = 200       # rate at which speed changes
        self.fuel_usuage = 10             # rate at which fuel is used
        self.distance = 10000             # distance from surface
        self.landed_successfully = False  # shuttle landed successfully or not

    def cal_landing_damage(self):
        if self.speed != 0:
            self.structural_integrity -= (self.speed * 0.1)

    # calculate distance change when `fall` is choosen
    def falling(self):
        if self.distance >= 2000:
            self.distance -= 2000
        else:
            self.distance = 0  # can't go below the surface!

    # calculate distance, fuel and speed changes when 'break' is choosen
    def breaking(self):
        """Not allowing negative speed, distance or fuel"""
        if self.speed >= self.speed_alteration:
            self.speed -= self.speed_alteration
        else:
            self.speed = 0
        if self.fuel >= self.fuel_usuage:
            self.fuel -= self.fuel_usuage
        else:
            self.fuel = 0
        if self.distance >= 1000:
            self.distance -= 1000
        else:
            self.distance = 0

    #  function for calculating if landing successful
    def cal_landing_success(self):
        if self.fuel < 60:
            print("You landed saftely but do not have enough fuel to return to Earth.\n\
            You plant the lichen and die watching strange stars dance.")
            sys.exit()  # this is a function built into python that tells the program to exit and stop running
        elif self.structural_integrity <= 30:
            print("You hit the surface too fast and explode in a blaze of glory.")
            sys.exit()
        elif (self.structural_integrity > 30) and (self.structural_integrity < 80):
            print("You hit the surface in a crumpled hull that no longer remotely resembles a shuttle.\n\
            You can no longer return to earth. You die watching strange stars dance.")
            sys.exit()
        else:
            print("Like a pro you gracefully swoop down onto the red marshain surface with a perfect landing.")

    # main logic function
    def land_shuttle(self):
        while self.distance != 0:
            print("Shuttle distance from surface: {dist}, speed {speed}, fuel {fuel}".format(
                dist=self.distance, speed=self.speed, fuel=self.fuel))
            choice = raw_input("Type 'break' to slow fall. Type 'fall' to continue falling.")
            if choice == "break":
                self.breaking()
            elif choice == "fall":
                self.falling()

        if self.distance == 0:
            self.cal_landing_damage()
            self.cal_landing_success()

print("Approaching mars")
astronaut_name = raw_input("Please type your name to start landing sequence.")
print("Astronaut %s selected to start shuttle landing sequence. Initiating release from main ship." % astronaut_name)
shuttle = Shuttle()
shuttle.land_shuttle()
