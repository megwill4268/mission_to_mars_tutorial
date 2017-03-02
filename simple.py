# let's define some variables to use later on
speed = 1000
fuel = 100
structural_integrity = 100
speed_alteration = 200
fuel_usuage = 10
distance = 10000
landed_successfully= 'False'

# simple supporting functions 

# calculating damage on landing, the greater the speed the greater the damage
def cal_landing_damage():
    global speed, structural_integrity
    if speed != 0:
       structural_integrity -= (speed * 0.1)


# calculate distance change when `fall` is choosen 
def falling():
    global distance
    if distance >= 2000:
        distance -= 2000
    else:
        distance = 0 # can't go below the surface!


# calculate distance, fuel and speed changes when 'break' is choosen
def breaking():
    """Not allowing negative speed, distance or fuel"""
    global speed, speed_alteration, fuel, fuel_usuage, distance
    if speed >= speed_alteration:
        speed -= speed_alteration
    else:
        speed = 0
    if fuel >= fuel_usuage:
        fuel -= fuel_usuage
    else:
        fuel = 0
    if distance >= 1000:
        distance -= 1000
    else:
        distance = 0

import sys # normally we would put this at the very top of our file
#  function for calculating if landing successful
def cal_landing_success():
    global fuel, structural_integrity
    if fuel < 60:
        print("You landed saftely but do not have enough fuel to return to Earth. You plant the lichen and die watching strange stars dance.")
        sys.exit()   # this is a function built into python that tells the program to exit and stop running
    elif structural_integrity <= 30:
        print("You hit the surface too fast and explode in a blaze of glory.")
        sys.exit()
    elif (structural_integrity > 30) and (structural_integrity < 80):
        print("You hit the surface in a crumpled hull that no longer remotely resembles a shuttle. You can no longer return to earth. You die watching strange stars dance.")
        sys.exit()
    else:
        print("Like a pro you gracefully swoop down onto the red marshain surface with a perfect landing.")



# main logic function

def land_shuttle():
    global distance
    while distance != 0:
        print("Shuttle distance from surface: {dist}, speed {speed}, fuel {fuel}".format(dist=distance, speed=speed, fuel=fuel))
        choice = raw_input("Type 'break' to slow fall. Type 'fall' to continue falling.")
        if choice == "break":
            breaking()
        elif choice == "fall":
            falling()

    if distance == 0:
        cal_landing_damage()
        cal_landing_success()
  

# let's put it all together

print("Approaching mars")

astronaut_name = raw_input("Please type your name to start landing sequence.")
  
print("Astronaut %s selected to start shuttle landing sequence. Initiating release from main ship." % astronaut_name)

land_shuttle()