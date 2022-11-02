import csv
# first"" is your opening file,second is the function of read
with open("form.csv", "r")as file:
    # reader = csv.reader(file)//reader will show all the list in the output
    # but if use dictionary will be output colletion of the key value pair.
    reader = csv.DictReader(file)
    for row in reader:

    form = row[1]
    print(form[1])
    # print(row[1])
# if just row like this the computer will just show you the hall the string in that line.
