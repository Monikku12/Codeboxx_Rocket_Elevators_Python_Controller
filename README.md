# Description

This program controls a Column of elevators.

It sends an elevator fetch a user when a button on a floor is press and it takes
this user to its desired floor when the corresponding button inside the elevator is pressed.

The program first creates the columns, elevators, buttons and other variables it needs to operate depending on the data you will input. From then, the program operates and controls the elevators in accordance of you scenario.

The elevator selection is based on a calculation determinating the best elevator possible. This calculation considers the status of the elevator, its position and its direction if it's moving.

# Dependencies

To be able to run the program, you need to have the python language installed. 

Depending on your python version, you want to make sure to install the Package Installer for Python (PIP) if needed:

https://pip.pypa.io/en/stable/installing/

# Usage

To use the program, follow the steps below:

- If you have your own output file, you need to link both file together by adding this line to the top of your file <import residential_controller>.

- If you don't have an external file or if you wish to run a scenario directly in the file, you need to fill the TEMPLATE section 
at the bottom of the file. Fill the TEMPLATE by entering your own data by replacing the text with the <>. 

## Example

Here is the empty TEMPLATE:

TEMPLATE - empty
templateColumn = Column(1, <numberOfFloors>, <numberOfElevators>)
templateColumn.elevatorList[0].currentFloor = <yourFirstElevatorCurrentFloor>
templateColumn.elevatorList[1].currentFloor = <yourSecondElevatorCurrentFloor>
elevator = templateColumn.requestElevator(<yourCurrentFloor>, "<yourRequestedDirection>")
elevator.requestFloor(<yourRequestedFloorNumber>)

TEMPLATE - filled
templateColumn = Column(1, 10, 2)
templateColumn.elevatorList[0].currentFloor = 10
templateColumn.elevatorList[1].currentFloor = 3
elevator = templateColumn.requestElevator(1, "up")
elevator.requestFloor(6)

Which means you have a building with one column of 2 elevators. The first elevator is on the 10th floor and the second elevator is on the third floor. Someone enters the building and press the button to call the elevator. In this case, the best elevator to reach the users will be the second elevator. The program will then operate the second elevator to pick up the users and bring him to the 6F like requested. 