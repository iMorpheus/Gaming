# Farming math

## OVERVIEW

I want to start farming in _No Man's Sky_. Unfortunately, my numeracy/my math skills are meh. My goal here is to rectify that. Before I can even think of farming, I need to identify available information, variables required for math and stuff that requires formulas(?).

## RESOURCE INFORMATION FOUND IN GAME

### Frost Crystal

- NAME: Frost Crystal
- YIELD/OUTPUT: 81 units
- TIME TO YEILD: 1 hour

## VARIBLES: INPUTS

- `TimeToYield`: Time required before resource is ready for collection measured in minutes.
- `Output`: Number of units available for collection after `TimeToYield`
- `NumberOfHydroponicTrays`: Number of trays to be used
- `DesiredYield`: Amount of resource desired/reqired.

## VARIABLES: OUTPUT

> TODO: Require Inputs and/or Fixed Variables. Formulas?

- `NumberOfChecksPerHour`: Number of checks per hour
- `CarbonRequired`: Units of carbon required to build the required number of Hydroponic Trays
- `PureFerriteRequired`: Units of Pure Ferrite required to build required the number of Hydroponic Trays
- `FerriteDustRequired`: Units of Ferrite Dust required to build required the number of Metal Plates
- `MetalPlatesRequired`: Number of Metal Plates required to build the required number of Hydroponic Trays.

## VARIABLES: FIXED

- `MinutesInOneHour`: Number of minutes in an hour
- `HydroponicTrayCost`: Resources required to craft one Hydroponic Tray
  - `Carbon`: 20
  - `PureFerrite`: 30
  - `MetalPlating * 2`
    - `FerriteDust`: `50 * 2`
    
## FIRST FLOOR FREIGHTER:
- `AREA: 28 * 36 = 1008`
- `HYDROPONIC TRAY AREA: 4 * 4 = 16`
- `AISLE SPACE: 2`
- `TOTAL HYROPONIC TRAY + AISLE SPACE: 5 * 5 = 25`
- `TOTAL NUMBER OF HYDROPONIC TRAYS POSSIBLE = 1008 / 25 = 40`

### WORKSPACE CALCULATOR `HydroCalculator.py`

```
### Let's figure out how many trays we can build in a space/area in No Man's Sky
## Farming Area Input From USER ##

height = input("Enter the height: ")
width = input("Enter the width: ")
width = int(width)
height = int(height)

# Above code courtesy of student.

### FIXED VALUE

HydroTrays = 25 # Actual Hydroponic Tray dimensions 4*4 but we have added an extra row and column as aisles.

### MATHS
Area=width*height
PossibleTrays = Area / HydroTrays

### OUTPUT
print(PossibleTrays)

#  TODO:
### - Formula for squares
### - Shape menu picker: Square or rectangle 
# DONE
# - Collect User Input.
```
