floorRequestButtonID = 1
callButtonID = 1


class Column:
    def __init__(self, _id, _amountOfFloors, _amountOfElevators):
        self.ID = 1
        self.status = "online"
        self.elevatorList = []
        self.callButtonList = []
        self.createElevators(_amountOfFloors, _amountOfElevators)
        self.createCallButtons(_amountOfFloors)

        # ---------------------------------Methods--------------------------------------------
    def createCallButtons(self, _amountOfFloors):
        global callButtonID
        print ("Create Call Button")
        buttonFloor = 1            
        for i in range (_amountOfFloors):
            if (i < _amountOfFloors): # If it's not the last floor
                callButton = CallButton(callButtonID, buttonFloor, "Up") #id, status, floor, direction
                self.callButtonList.append(callButton)
                callButtonID+=1
            if (i > 1): #If it's not the first floor
                callButton = CallButton(callButtonID, buttonFloor, "Down") #id, status, floor, direction
                self.callButtonList.append(callButton)
                callButtonID+=1
                buttonFloor+=1

    def createElevators(self, _amountOfFloors, _amountOfElevators):
        print ("Create Elevator")
        for _amountOfElevators in range(_amountOfElevators):
            elevator = Elevator(_amountOfElevators+1, _amountOfFloors) #id, status, amountOfFloors, currentFloor
            self.elevatorList.append(elevator)

        # Simulate when a user press a button outside the elevator
    def requestElevator(self, floor, direction):
        print ("Request Elevator")        
        elevator = self.findElevator(floor, direction)
        elevator.floorRequestList.append(floor)
        elevator.move()
        elevator.operateDoors()
        return elevator


        # We use a score system depending on the current elevators state. Since the bestScore and the referenceGap are
        # higher values than what could be possibly calculated, the first elevator will always become the default bestElevator,
        # before being compared with to other elevators. If two elevators get the same score, the nearest one is prioritized.
    def findElevator(self, requestedFloor, requestedDirection):
        print ("find elevator")
        bestElevator = None
        bestScore = 5
        referenceGap = 10000000
        bestElevatorInformations = {"bestElevator":bestElevator, "bestScore":bestScore, "referenceGap":referenceGap}
        
        for elevator in self.elevatorList:
            # The elevator is at my floor and going in the direction I want
            if (requestedFloor == elevator.currentFloor and elevator.status == "stopped" and requestedDirection == elevator.direction):
                bestElevatorInformations = self.checkIfElevatorIsBetter(1, elevator, bestElevatorInformations, requestedFloor)
                # The elevator is lower than me, is coming up and I want to go up
            elif (requestedFloor > elevator.currentFloor and elevator.direction == "up" and requestedDirection == elevator.direction):
                bestElevatorInformations = self.checkIfElevatorIsBetter(2, elevator, bestElevatorInformations, requestedFloor)
                # The elevator is higher than me, is coming down and I want to go down
            elif (requestedFloor < elevator.currentFloor and elevator.direction == "down" and requestedDirection == elevator.direction):
                bestElevatorInformations = self.checkIfElevatorIsBetter(2, elevator, bestElevatorInformations, requestedFloor)
                # The elevator is idle
            elif (elevator.status == "idle"):
                bestElevatorInformations = self.checkIfElevatorIsBetter(3, elevator, bestElevatorInformations, requestedFloor)
                # The elevator is not available, but still could take the call if nothing better is found
            else:
                bestElevatorInformations = self.checkIfElevatorIsBetter(4, elevator, bestElevatorInformations, requestedFloor)
        print ("Best elevator", bestElevatorInformations["bestElevator"])
        elevator = bestElevatorInformations.get("bestElevator")
        return elevator

    def checkIfElevatorIsBetter(self, scoreToCheck, newElevator, bestElevatorInformations, floor):
        print ("Check if elevator is better")
        if (scoreToCheck < bestElevatorInformations["bestScore"]):
            bestElevatorInformations["bestScore"] = scoreToCheck
            bestElevatorInformations["bestElevator"] = newElevator
            bestElevatorInformations["referenceGap"] = abs(newElevator.currentFloor - floor)
        elif (bestElevatorInformations["bestScore"] == scoreToCheck):
            gap = abs(newElevator.currentFloor - floor)
            if (bestElevatorInformations["referenceGap"] > gap):
                bestElevatorInformations["bestElevator"] = newElevator
                bestElevatorInformations["referenceGap"] = gap
        return bestElevatorInformations


class Elevator:
    def __init__(self, _id, _amountOfFloors):
        self.ID = _id
        self.status = "idle"
        self.currentFloor = 1
        self.amountOfFloors = _amountOfFloors
        self.direction = None
        self.door = Door(_id) 
        self.floorRequestButtonList = []
        self.floorRequestList = []
        self.createFloorRequestButtons(_amountOfFloors)

    def createFloorRequestButtons(self, _amountOfFloors,):
        global floorRequestButtonID
        print ("create Floor Request Buttons")
        buttonFloor = 1    
        for _amountOfFloors in range(_amountOfFloors):
            floorRequestButton = FloorRequestButton(floorRequestButtonID, buttonFloor)
            self.floorRequestButtonList.append(floorRequestButton)
            buttonFloor+=1
            floorRequestButtonID+=1

        # Simulate when a user press a button inside the elevator
    def requestFloor(self, floor):
        print ("Request Floor")
        self.floorRequestList.append(floor)
        self.move()
        self.operateDoors()

    def move(self):
        print ("Move")
        while (len(self.floorRequestList) != 0):
            destination = self.floorRequestList[0]
            self.status = "moving"
            if (self.currentFloor < destination):
                self.direction = "up"
                self.sortFloorList()
                while (self.currentFloor < destination):
                    self.currentFloor+=1
                    self.screenDisplay = self.currentFloor
            elif (self.currentFloor > destination):
                self.direction = "down"
                self.sortFloorList()
                while (self.currentFloor > destination):
                    self.currentFloor-=1
                    self.screenDisplay = self.currentFloor
            self.status = "stopped"
            self.floorRequestList.pop()
        self.status = "idle"

    def sortFloorList(self):
        print ("Sort Floor list")
        if (self.direction == "up"):
            self.floorRequestList.sort
        else:
            self.floorRequestList.reverse

    def operateDoors(self):
        print("operate Doors")
        self.door.status = "opened"
        print("Wait 5 secondes.")
        obstruction = None
        if self != "overweight":
            self.door.status = "closing"
            if obstruction == False:
                self.door.status = "closed"
            else:
                self.operateDoors
        else:
            while self.isOverweight:
                    print("Activate overweight alarm")
            self.operateDoors



class CallButton:
    def __init__(self, _id, _floor, _direction):
        self.ID = _id
        self.status = "OFF"
        self.floor = _floor
        self.direction = _direction

class FloorRequestButton:
    def __init__(self, _id, _floor):
        self.ID = _id
        self.status = "OFF"
        self.floor = _floor

class Door:
    def __init__(self, _id):
        self.ID = _id
        self.status = "closed"


# Scenario 1
testColumn = Column(1, 10, 2)
testColumn.elevatorList[0].currentFloor = 2
testColumn.elevatorList[1].currentFloor = 6

elevator = testColumn.requestElevator(3, "up")
elevator.requestFloor(7)

# ******************