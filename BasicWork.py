#Imported pandas module and mode from the statistics module
import pandas
from statistics import mode

# Read the basic work orders file using the panda csv file reader
data_frame = pandas.read_csv("basic_work_orders.csv")

# Use .values to get the correct number of work orders
machine_types = data_frame["Machine Type"].values.tolist()

# Write if/elif logic that will give the correct phrasing for each result
if machine_types.count("TRUCK 001") > 1:
    print("Truck 001 had " + str(machine_types.count('TRUCK 001')) + " work orders")
elif machine_types.count("TRUCK 001") == 1:
    print("Truck 001 had " + str(machine_types.count('TRUCK 001')) + " work order")
elif machine_types.count("TRUCK 001") == 0:
    print("Truck 001 had " + str(machine_types.count('TRUCK 001')) + " work orders")

if machine_types.count("TRUCK 002") > 1:
    print("Truck 002 had " + str(machine_types.count('TRUCK 002')) + " work orders")
elif machine_types.count("TRUCK 002") == 1:
    print("Truck 002 had " + str(machine_types.count('TRUCK 002')) + " work order")
elif machine_types.count("TRUCK 002") == 0:
    print("Truck 002 had " + str(machine_types.count('TRUCK 002')) + " work orders")

if machine_types.count("TRUCK 003") > 1:
    print("Truck 003 had " + str(machine_types.count('TRUCK 003')) + " work orders")
elif machine_types.count("TRUCK 003") == 1:
    print("Truck 003 had " + str(machine_types.count('TRUCK 003')) + " work order")
elif machine_types.count("TRUCK 003") == 0:
    print("Truck 003 had " + str(machine_types.count('TRUCK 003')) + " work orders")

# Use .mode to find the most mentioned part replaced
machine_part = data_frame["Main Part Replaced"].values.tolist()
print("The " + mode(machine_part) + " was the most replaced part")
