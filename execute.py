from lift_sim import CentralSystem

print("An Elevator Control System with 3 lifts and 30 floors")
print("=====================================================")
cs = CentralSystem()

print("")
print("")

print("Test Input1: Lift is called at 12th floor UP direction")
lif = cs.call_lift(12,1)
print("")
print("")

print("Test Input2: The person in Lift wants to go to 18th floor")
cs.start_lift(lif, 18)
print("")
print("")

print("Test Input 3: Input from 0th floor is made to Down Direction, should throw an error")
lif = cs.call_lift(0,-1)
print("")
print("")

print("Test Input 4: Input from 29th floor is made to UP Direction, should throw an error")
lif = cs.call_lift(29,1)
print("")
print("")

print("Status: Now Elevator 0 is on 18th floor and 1 and 2 are on 0th flooor")
print("")
print("")

print("Test Input 5: Person on 5th floor wants to go on 17th floor")
lif = cs.call_lift(5, 1)
cs.start_lift(lif, 17)
print("")
print("")

print("Test Input 6: Person on 6th floor calls the lift to go to 0th floor")
lif = cs.call_lift(6,-1)
cs.start_lift(lif, 0)

print("")
print("")

print("Test Input 7: Invalid floor entered for calling. Say 30")
lif = cs.call_lift(30,1)
