class Customer:
    def __init__(self, roomBooking, name):
        self.__roomBooking = roomBooking
        self.__name = name
        self.__feedback = 0

class Room:
    def __init__(self, number, size, clean):
        self.__number = number
        self.__size = size
        self.__occupants = []
        self.__clean = clean

class Hotel:
    def __init__(self, rooms):
        self.__rooms = rooms
    
    def checkRooms(self):
        return self.__rooms
    
class Manager:
    def __init__(self, name):
        self.__name = name

class Cleaner:
    def __init__(self, name):
        self.name = name

class Receptionist:
    def __init__(self, name):
        self.__name = name 
    
    def checkIn(receptionist, hotel, customer):
        pass
    
    def checkOut(receptionist, hotel, customer, manager):
        pass

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
    customer6 = (3, "Col. Mustard")
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