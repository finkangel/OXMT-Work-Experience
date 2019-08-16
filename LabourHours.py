import pandas
import statistics
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt

data_frame = pandas.read_csv("engine_work_orders_with_labour_hrs.csv")
print(data_frame)

print ("")

don = (data_frame.loc[data_frame["Assigned Maintenance Person"] == "Donald Knuth", "Labour Hours"]).tolist()
# print(don)
print("Average Labour Hours for Donald Knuth: " + str(sum(don) / len(don)))
print("Median Labour Hours for Donald Knuth: " + str(statistics.median(don)))

print("")

jon = (data_frame.loc[data_frame["Assigned Maintenance Person"] == "John Carmack", "Labour Hours"]).tolist()
# print(jon)
print("Average Labour Hours for John Carmack: " + str(sum(jon) / len(jon)))
print("Median Labour Hours for John Carmack: " + str(statistics.median(jon)))

jon.remove(99)
print("Average Labour Hours for John Carmack with Outliers Removed: " + str(sum(jon) / len(jon)))
print("Median Labour Hours for John Carmack with Outliers Removed: " + str(statistics.median(jon)))

print("")

#median_name = input("Who's predicted labour hours do you want?: ")
#if median_name == "John Carmack" or " John Carmack" or "John":
#    print("Predicted labour hours: " + str(statistics.median(jon)))
#elif median_name == "Donald Knuth" or " Donald Knuth" or "Donald":
#    print("Predicted labour hours: " + str(statistics.median(don)))
#else:
#    print("Unrecognised name")

data_frame.set_index("Assigned Maintenance Person")[["Labour Hours"]].plot.bar()
names = data_frame.groupby("Assigned Maintenance Person")
names.boxplot(showfliers=False)
plt.show()
