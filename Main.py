# Name: Alexis Nieves
# Student ID: 010674042
# Title: C950 WGUPS Routing Program
import csv
import datetime
from trucks import Truck
from CreateHashTable import HashTable
from Packages import Package

# Reads distance, address, and package data from the CSV files
with open("csvfiles/distance.csv") as distance_file:
    csv_distance = csv.reader(distance_file)
    csv_distance = list(csv_distance)

with open("csvfiles/address.csv") as address_file:
    csv_address = csv.reader(address_file)
    csv_address = list(csv_address)

with open("csvfiles/package.csv") as package_file:
    csv_package = csv.reader(package_file)
    csv_package = list(csv_package)

# Hash table from CreateHashTable.py
hash_table = HashTable()

# Creates package objects from the CSV package file
# and loads the objects into the hash table
# Has a time complexity of O(n)
def load_packages(filename, hash_table):
    with open(filename) as packages:
        package_data = csv.reader(packages, delimiter=',')
        for package in package_data:
            package_id = int(package[0])
            package_address = package[1]
            package_city = package[2]
            package_state = package[3]
            package_zipcode = package[4]
            package_deadline = package[5]
            package_weight = package[6]
            package_status = "At hub"

            # Package object
            p = Package(package_id, package_address, package_city, package_status,
                        package_zipcode, package_deadline, package_weight, package_status)
            
            # Inserts package data into the hash table
            hash_table.insert(package_id, p)

# Creates method to calculate the distance between two addresses
def distance_between(x, y):
    distance = csv_distance[x][y]
    if distance == '':
        distance = csv_distance[y][x]

    return float(distance)

# Method to retrieve the address number
def get_address(address):
    for row in csv_address:
        if address in row[2]:
            return int(row[0])
        
# Loads packages manually into the 3 trucks
truck1 = Truck(16, 18, None, [14, 15, 16, 34, 20, 21, 19, 13, 39, 24, 31, 12, 29, 30, 37], 0.0, "4001 South 700 East", datetime.timedelta(hours=8, minutes=0))
truck2 = Truck(16, 18, None, [1, 33, 7, 10, 5, 38, 3, 36, 18, 2, 8, 40, 6], 0.0, "4001 South 700 East", datetime.timedelta(hours=9, minutes=5))

# Loads final packages into the last truck
truck3 = Truck(16, 18, None, [32, 23, 11, 22, 27, 35, 17, 4, 28, 9, 25, 26], 0.0, "4001 South 700 East", datetime.timedelta(hours=10, minutes=20))

# Loads packages into hash table
load_packages("csvfiles/package.csv", hash_table)

# Creates method to calculate the minimum distance between current address
# and the nearest address using the Nearest Neighbor algorithm
# Has a time complexity of O(n)
def delivering_truck(truck):
    undelivered = []
    for package_id in truck.packages:
        package = hash_table.search(package_id)
        undelivered.append(package)
    truck.packages.clear()

    while len(undelivered) > 0:
        next_address = 2000
        next_package = None
        for package in undelivered:
            if distance_between(get_address(truck.address), get_address(package.address)) <= next_address:
                next_address = distance_between(get_address(truck.address), get_address(package.address))
                next_package = package
        # Adds closest package to the list
        truck.packages.append(next_package.id)
        # Removes package from undelivered
        undelivered.remove(next_package)
        # Takes miles driven for package and stores in truck.mileage
        truck.miles += next_address
       # Updates current address
        truck.address = next_package.address
        # Updates time taken by driver to get to the nearest address
        truck.time += datetime.timedelta(hours=next_address / 18)
        next_package.delivered_at = truck.time
        next_package.departed_at = truck.departure_time

# Places trucks in to the loading process
delivering_truck(truck1)
delivering_truck(truck2)
# Ensuring third truck does NOT leave until either truck1 or truck2 have finished and returned for the day
truck3_departure = min(truck1.time, truck2.time)
delivering_truck(truck3)

# User Interface
# End user will be met with a list of options
class Main:
    print("Welcome to the WGUPS Package and Delivery Information")
    print("Total mileage: ")
    print(truck1.miles + truck2.miles + truck3.miles)
    text = input("To begin, please type 'go': ")
    if text == "go":
        time = input("Please enter a time for package status in the following format: HH:MM:SS ")
        (h, m, s) = time.split(":")
        convert_timedelta = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        print("""
              Please select an option from the list below.
              1. Get status of a single package
              2. Get status of all packages with a time
              3. Exit""")
        option = input()
        if option == '1':
            pID = input("Please enter the package ID: ")
            package = hash_table.search(int(pID))
            package.status_update(convert_timedelta)
            print(package)
        elif option == '2':
            for pID in range(1, 41):
                pkg = hash_table.search(pID)
                print(pkg.status_update(convert_timedelta))
        elif option == '3':
            exit()
        else:
            print("Invalid option. Terminating program.")
            exit()
    else:
        print("Invalid option. Please try again.")
