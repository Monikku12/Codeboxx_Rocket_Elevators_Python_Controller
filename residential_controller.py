floorRequestButtonID = 1
callButtonID = 1


class Column:
    def __init__(self, _id, _amountOfFloors, _amountOfElevators):
        self.ID = 1
        self.status = "online"
        self.amountOfFloors = _amountOfFloors
        self.elevatorList = []
        self.callButtonList = []
        self.createElevators(_amountOfFloors, _amountOfElevators)
        self.createCallButtons(_amountOfFloors)

        # ---------------------------------Methods--------------------------------------------
    def createCallButtons(self, _amountOfFloors):
        global callButtonID
        print ("Create Call Button")
        buttonFloor = 1            
        for _amountOfFloors in range (_amountOfFloors):
            if (buttonFloor < _amountOfFloors): # If it's not the last floor
                callButton = CallButton(callButtonID, buttonFloor, "Up") #id, status, floor, direction
                self.callButtonList.append(callButton)
                callButtonID+=1

            if (buttonFloor > 1): #If it's not the first floor
                callButton = CallButton(callButtonID, buttonFloor, "Down") #id, status, floor, direction
                self.callButtonList.append(callButton)
                callButtonID+=1
                buttonFloor+=1






    def createElevators(self, _amountOfFloors, _amountOfElevators):
        print ("Create Elevator")
        for _amountOfElevators in range(_amountOfElevators):
            elevator = Elevator(_amountOfElevators+1, _amountOfFloors, 1) #id, status, amountOfFloors, currentFloor
            self.elevatorList.append(elevator)


    

class Elevator:
    def __init__(self, _id, _amountOfFloors, _currentFloor):
        self.ID = _id
        self.status = "idle"
        self.currentFloor = _currentFloor
        self.amountOfFloors = _amountOfFloors
        self.direction = None
        self.door = Door(_id, "closed") 
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
        self.floorRequestList.push(floor)
        self.move()
        self.operateDoors()
    
    def move(self):
        print ("Move")
        while (self.floorRequestList.length != 0):
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
            self.floorRequestList.shift()
        self.status = "idle"

    def sortFloorList(self):
        print ("Sort Floor list")
        if (self.direction == "up"):
            self.floorRequestList.sort
        else:
            self.floorRequestList.reverse

    # def operateDoors(self):
    #     print("operate Doors")
    #     self.door.status = "opened"
    #     print("Wait 5 secondes.")
    #     obstruction
    #     if self != "overweight":
    #         self.door.status = "closing"
    #         if "obstruction" == false:
    #             self.door.status = "closed"
    #         else:
    #             self.operateDoors
    #     else:
    #         while self.isOverweight:
    #                 print("Activate overweight alarm")
    #         self.operateDoors



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
    def __init__(self, _id, _status):
        self.ID = _id
        self.status = _status


# Scenario 1
testColumn = Column(1, 10, 2)
testColumn.elevatorList[0].currentFloor = 2
testColumn.elevatorList[1].currentFloor = 6

elevator = testColumn.requestElevator(3, "up")
elevator.requestFloor(7)

# ******************