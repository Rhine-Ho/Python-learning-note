import csv
# first"" is your opening file,second is the function of read
with open("form.csv", "r")as file:
    reader = csv.reader(file)
    for row in reader:

    favorite = row[1]
    print(row[1])
# if just row like this the computer will just show you the hall the string in that line.
