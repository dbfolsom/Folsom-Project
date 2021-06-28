dict_member = {}
VINs = dict_member

class Vehicle():
    def __init__(self, VIN, make, model, year, mileage):
        self.VIN = VIN
        self.make = make
        self.model = model
        self. year = year
        self.mileage = mileage
    def display (self):
        for VIN, VINs in dict_member.items():
            print(('VIN:', VINs.VIN + ', ''Model:' + VINs.model + ', ''Make:' + VINs.make + ', ''Year:' + VINs.year + ',' 'Mileage:' + VINs.mileage))
            if VINs == 0:
                print('NO VINs FOUND ON RECORD.')
    def add(self):
            VIN = input("Enter VIN of Car:\n ")
            make = input("Enter Make:\n ")
            model = input("Enter Model:\n ")
            year = input("Enter Year:\n ")
            mileage = input("Enter Car's Mileage:\n")
            dict_member[VIN] = Vehicle(VIN, make, model, year, mileage)
    def remove(self):
            VIN = str(input("Enter VIN of Car to Remove:\n"))
            if VIN in VINs:
                print('VEHICLE DELETED.')
                del VINs[VIN]
                
            else:
                print("VIN NOT FOUND PLEASE ENTER CORRECT VIN TO REMOVE IT FROM RECORD.")
    def edit(self, VIN):
            if VIN in VINs:
                print('VEHICLE CAN BE EDITED.')
                V = input("Enter New VIN for the Car:\n")
                ma = input("Enter New Make for the Car:\n ")
                mo = input("Enter the New Model for the Car:\n ")
                y = input("Enter the New Car Year:\n ")
                mi = input("Enter the New Car Mileage:\n ")
                del dict_member[VIN]
                dict_member[VIN] = Vehicle(V, ma, mo, y, mi)
            else:
                print("PLEASE ENTER THE CORRECT VIN TO EDIT.")


def display_menu():
    try:
        print("")
        print("1. View Vehicle Records")
        print("2. Add Vehicle to Records")
        print("3. Remove Vehicle from Records ")
        print("4. Edit Vehicle Record")
        print("5. Exit ")
        print("")
        return int(input("Selection> "))
    except ValueError:
        print("Selection Not Valid.")
    return VINs

print("Welcome to the Car Inventory System")
vehicle_instance = Vehicle(None, None, None, None, None)
menu_item = display_menu()
while menu_item != 5:
    if menu_item == 1:
        vehicle_instance.display()
    elif menu_item == 2:
        vehicle_instance.add()
    elif menu_item == 3:
        vehicle_instance.remove()
    elif menu_item == 4:
        m = input("Enter VIN to edit Car Characteristics\n")
        vehicle_instance.edit(m)
    elif menu_item == 5:
        vehicle_instance.saveData()
    elif menu_item == 6:
        vehicle_instance.loadData()
    menu_item = display_menu()
print("Exiting Program...")