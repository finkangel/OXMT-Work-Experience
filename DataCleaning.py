import pandas
import statistics
import matplotlib.pyplot as plt; plt.rcdefaults()

data_frame = pandas.read_csv("unclean_work_orders_with_labour_hrs.csv")
print("Null Main Part Replaced data values: " + str(sum(data_frame["Main Part Replaced"].isnull())))
print("Null Assigned Maintenance Person data values: " + str(sum(data_frame["Assigned Maintenance Person"].isnull())))
print("Null Labour Hours data values: " + str(sum(data_frame["Labour Hours"].isnull())))

data_frame["Machine Type"] = data_frame["Machine Type"].replace(["TRUCK 1", "TRUCK 01", "TRUCK_001"], "TRUCK 001")

data_frame["Main Part Replaced"] = data_frame["Main Part Replaced"].replace(["engine", "Enjine", "Eng"], "Engine")
data_frame["Main Part Replaced"] = data_frame["Main Part Replaced"].replace(["WHEL"], "Wheel")
data_frame["Main Part Replaced"] = data_frame["Main Part Replaced"].replace(["EXHAUST"], "Exhaust")
data_frame["Main Part Replaced"] = data_frame["Main Part Replaced"].replace(["Air Con", "AC", "A/C", "AirCon"], "Air Conditioning")

data_frame["Assigned Maintenance Person"] = data_frame["Assigned Maintenance Person"].replace(["Don Knuth", "Donald Knuth…", "{Donald Knuth}"], "Donald Knuth" )
data_frame["Assigned Maintenance Person"] = data_frame["Assigned Maintenance Person"].replace(["john carmack", "J. Carmack", "John Carmark"], "John Carmack")

data_frame = data_frame.dropna(how='any', axis=0)
data_frame["Labour Hours"] = data_frame["Labour Hours"].replace([99], 9)

print(data_frame)

# Engine plot
data_frame.iloc[:13].set_index("Assigned Maintenance Person")[["Labour Hours"]].plot.bar()
names = data_frame.iloc[:13].groupby("Assigned Maintenance Person")
names.boxplot(showfliers=False)

# Wheel plot
data_frame.iloc[14:21].set_index("Assigned Maintenance Person")[["Labour Hours"]].plot.bar()
names = data_frame.iloc[14:21].groupby("Assigned Maintenance Person")
names.boxplot(showfliers=False)

# Exhaust plot
data_frame.iloc[21:24].set_index("Assigned Maintenance Person")[["Labour Hours"]].plot.bar()
names = data_frame.iloc[21:24].groupby("Assigned Maintenance Person")
names.boxplot(showfliers=False)

# Air Conditioning Plot
data_frame.iloc[24:35].set_index("Assigned Maintenance Person")[["Labour Hours"]].plot.bar()
names = data_frame.iloc[24:35].groupby("Assigned Maintenance Person")
names.boxplot(showfliers=False)

def predict(name, machine):
    filtered_by_part_and_name = data_frame[
        (data_frame["Assigned Maintenance Person"] == name) & (data_frame["Main Part Replaced"] == machine)]
    return statistics.median(filtered_by_part_and_name["Labour Hours"])

print("")

input_name = input("Enter a name: ")
input_part = input("Enter a part: ")
print(predict(input_name, input_part))

plt.show()
