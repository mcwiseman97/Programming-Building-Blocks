import csv

with open("life-expectancy.csv", mode='r')as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        print(lines)

print()

year = int(input("Enter the year of preference: "))
maxpercentage = 86.751
minpercentage = 17.76
max_year = 2019
min_year = 1882
print()