### HOW TO NOT RUN OUT OF FUEL: Calculating Number of Race Laps Remaining

When participating in races requiring refuelling, you do not want to run out of fuel at any time during the event. Aside from being embarassing, the lack of fuel will result in your car slowing drastically which in turn will result in your competitors gaining rapidly then overtaking you. 

Yikes.

To avoid the above, it is important to know the number of laps remaining plus the number of laps of remaining fuel there is sloshing about in your fuel tank. To calculate the *number of race laps remaining* you will need to know the following:
- Race Distance
- Current lap
To calculate the *Number of Race Laps Remaining* use the following formula:

Number of race laps - (Current Lap + 1) = Number of Race Laps Remaining

#### Example
- Number of race laps: 13
- Current lap: 7 
- 13 - (7 + 1) = 5

Compare the above result, *Number of Race Laps Remaining*, to the number of laps of fuel remaining in your fuel tank to determine whether or not refuelling is necessary.

IF *Number Of Race Laps Remaining* is **GREATER THAN** Number Of Laps Of Fuel Remaining **THEN** Refuel 
IF *Number Of Race Laps Remaining* is **LESS THAN** *Number of Laps Of Fuel Remaining* Race on!

if \[ $NumberOfRaceLapsRemaining > $NumberOfLapsOfFuelRemaining \]
then
  Refuel
fi

- Number of Race Laps Remaining: 5
- Number of Laps of Fuel Remaining: 3
- 5 > 3 ∴ PIT!

if \[ $NumberOfRaceLapsRemaining < $NumberOfLapsOfFuelRemaining \]
then
  Continue Racing
fi

- Number of Race Laps Remaining: 5
- Number of Laps of Fuel Remaining: 6
- 5 > 6 ∴ DO NOT PIT!

#### RESOURCES 
- Mathmatics: [PEMDAS](https://www.purplemath.com/modules/orderops.htm) 
- Bash: [IF-ELSE](https://linuxize.com/post/bash-if-else-statement/)
- Logic/Mathematical Proof: [Therefore/∴](https://en.wikipedia.org/wiki/Therefore_sign)

