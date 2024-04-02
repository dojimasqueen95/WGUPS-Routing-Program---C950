# Name: Alexis Nieves
# Student ID:
# Title: C950 WGUPS Routing Program
import csv
import datetime
import Trucks
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


# Creates package objects from the CSV package file
# and loads the objects into the hash table
# Has a time complexity of O(n)
def load_packages(filename, package_hash):
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
            package_hash.insert(package_id, p)