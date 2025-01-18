class Customer:
    def __init__(self, roomBooking, name):
        self.__roomBooking = roomBooking
        self.__name = name
        self.__feedback = 0
    
    def getBooking(self):
        return self.__roomBooking
    def getName(self):
        return self.__name
    def getFeedback(self):
        return self.__feedback
    def updFeedback(self):
        self.__feedback += 1


class Room:
    def __init__(self, number, size, clean):
        self.__number = number
        self.__size = size
        self.__occupants = []
        self.__clean = clean
    
    def getNumber(self):
        return self.__number
    def getSize(self):
        return self.__size
    def getOccupants(self):
        return self.__occupants
    def isClean(self):
        return self.__clean
    def listOccupants(self):
        for count, occupant in enumerate(self.__occupants):
            print(f"Occupant no.{count} is {occupant.getName()}.")
    def roomCleaned(self):
        self.__clean = True  
    
    def addOccupant(self, occupantIn):
        self.__occupants.append(occupantIn)
        if not self.__clean:
            occupantIn.updFeedback()
        if len(self.getOccupants()) > self.getSize():
            occupantIn.updFeedback()

    def removeOccupant(self, occupantOut):
        for index, occupant in enumerate(self.getOccupants()):
            if occupant == occupantOut:
                del self.__occupants[index]
            else:
                print("ERROR NO SUCH OCCUPANT")


class Hotel:
    def __init__(self, rooms):
        self.__rooms = rooms
    
    def checkRooms(self):
        return self.__rooms
    

class Manager:
    def __init__(self, name):
        self.__name = name
    
    def getName(self):
        return self.__name

    def takeFeedback(self, manager, customer):
        match customer.getFeedback():
            case 0:
                print(f"{self.getName()} says: {customer.getName()} was happy with their stay.")
            case 1:
                print(f"{self.getName()} says: {customer.getName()} was ok with their stay.")
            case 2:
                print(f"{self.getName()} says: {customer.getName()} was unhappy with their stay.")
            case _:
                print("Error.")


class Cleaner:
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def cleanRooms(self, hotel):
        for room in hotel.checkRooms():
            if room:
                print(f"{self.getName()} cleaned room {room.getNumber()}")


class Receptionist:
    def __init__(self, name):
        self.__name = name 
    
    def getName(self):
        return self.__name

    def checkIn(self, hotel, customer):
        #Call addOccupant from room
        roomNo = customer.getBooking()
        hotel.checkRooms()[roomNo - 1].addOccupant(customer)
    
    def checkOut(self, hotel, customer, manager):
        #Call removeOccupant from room
        roomNo = customer.getBooking()
        hotel.checkRooms()[roomNo - 1].removeOccupant(customer)
        manager.takeFeedback(manager, customer)





def main():
    room1 = Room(1, 1, False)
    room2 = Room(2, 2, True)
    room3 = Room(3, 1, False)
    hotel = Hotel([room1, room2, room3])
    customer1 = Customer(1, "Mrs. White")
    customer2 = Customer(2, "Mr. Green")
    customer3 = Customer(2, "Miss. Scarlett")
    customer4 = Customer(3, "Mrs. Peacock")
    customer5 = Customer(2, "Prof. Plum")
    customer6 = Customer(3, "Col. Mustard")
    receptionist = Receptionist("Jane")
    cleaner = Cleaner("Michael")
    manager = Manager("Janhavi")

    receptionist.checkIn(hotel, customer1)
    receptionist.checkIn(hotel, customer2)
    receptionist.checkIn(hotel, customer3)
    receptionist.checkOut(hotel, customer1, manager)

    cleaner.cleanRooms(hotel)

    receptionist.checkIn(hotel, customer4)
    receptionist.checkOut(hotel, customer4, manager)
    receptionist.checkIn(hotel, customer5)
    receptionist.checkOut(hotel, customer5, manager)
    receptionist.checkOut(hotel, customer2, manager)
    receptionist.checkOut(hotel, customer3, manager)

    cleaner.cleanRooms(hotel)
    
    receptionist.checkIn(hotel, customer6)
    receptionist.checkOut(hotel, customer6, manager)

if __name__ == '__main__':
    main()