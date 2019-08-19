# Write classes for the following class hierarchy:

class Vehicle(object):
    # Vehicle is the base class for FlightVehicle and GroundVehicle
    pass

class FlightVehicle(Vehicle):
    #FlightVehicle is the base class for starship and Airplane
    pass
class Starship(FlightVehicle):
    pass
class Airplane(FlightVehicle):
    pass
class GroundVehicle(Vehicle):
    # GroundVehicle is the base class for Car and Motorcycle
    pass
class Car(GroundVehicle):
    pass
class Motorcycle(GroundVehicle):
    pass



#   class
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
