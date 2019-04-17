# Lift_Simulator

3 lifts simulator system implemented for 30 storey building - Python

## Running the tests

To run the test cases, run execute.py - [Python 2.7]

### Test Input1: Lift is called at 12th floor UP direction

```
Lift 0 chosen
Floor 1 ===> Floor 2 ===> Floor 3 ===> Floor 4 ===> Floor 5 ===> Floor 6 ===> Floor 7 ===> Floor 8 ===> Floor 9 ===> Floor 10 ===> Floor 11 ===> Floor 12 ===> 
Opening lift 0.
```

### Test Input2: The person in Lift wants to go to 18th floor

```
Lift 0 chosen
Floor 13 ===> Floor 14 ===> Floor 15 ===> Floor 16 ===> Floor 17 ===> Floor 18 ===> 
Opening lift 0.
```

### Test Input 3: Input from 0th floor is made to Down Direction, should throw an error

```
Invalid Entry: Lift can't go DOWN
```

### Test Input 4: Input from 29th floor is made to UP Direction, should throw an error

```
Invalid Entry: Lift can't go UP
```

## Status: Now Elevator 0 is on 18th floor and 1 and 2 are on 0th flooor

### Test Input 5: Person on 5th floor wants to go on 17th floor

```
Lift 1 chosen
Floor 1 ===> Floor 2 ===> Floor 3 ===> Floor 4 ===> Floor 5 ===> 
Opening lift 1.
Lift 1 chosen
Floor 6 ===> Floor 7 ===> Floor 8 ===> Floor 9 ===> Floor 10 ===> Floor 11 ===> Floor 12 ===> Floor 13 ===> Floor 14 ===> Floor 15 ===> Floor 16 ===> Floor 17 ===> 
Opening lift 1.
```

### Test Input 6: Person on 6th floor calls the lift to go to 0th floor

```
Lift 2 chosen
Floor 1 ===> Floor 2 ===> Floor 3 ===> Floor 4 ===> Floor 5 ===> Floor 6 ===> 
Opening lift 2.
Lift 2 chosen
Floor 5 ===> Floor 4 ===> Floor 3 ===> Floor 2 ===> Floor 1 ===> Floor 0 ===> 
Opening lift 2.
```

### Test Input 7: Invalid floor entered for calling. Say 30

```
Traceback (most recent call last):
  File "execute.py", line 48, in <module>
    lif = cs.call_lift(30,1)
  File "/home/ssardana08/Documents/projects/lift_simulator/lift_sim.py", line 41, in call_lift
    self.is_valid_floor(floor)
  File "/home/ssardana08/Documents/projects/lift_simulator/lift_sim.py", line 24, in is_valid_floor
    "have {} floors.".format(floor, 30))
ValueError: Invalid floor 30, building have 30 floors.
```
