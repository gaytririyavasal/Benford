# File: Benford.py
# Student: Gaytri Vasal
# UT EID: grv377
# Course Name: CS303E
# 
# Date Created: 11/9/2021
# Date Last Modified: 11/12/2021
# Description of Program: The following program processes data to ensure that it follows and is in accordance with Benford's Law.

def main():
    inputtedname = input("Enter the name of a file of census data: ")

    if (inputtedname == "Census_2009.txt"):
        s1 = set()
        d1 = {"1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}
        file = open ("Census_2009.txt", "r" )
        linecount = 0
        dictvalue = 0
        file.readline()
        for line in file:
            value = line.split()
            number = value[len(value)-1]
            firstdigit = number[0]
            firstdigitstring = str(firstdigit)
            s1.add(number)
            d1[firstdigitstring] += 1
            linecount += 1
        file.close()
        print("Output written to benford.txt")
        outfile = open("benford.txt", "w")
        outfile.write("Total number of cities: " + str(linecount) + "\n" +
                      "Unique population counts: " + str(len(s1)) + "\n" +
                      "First digit frequency distributions: " + "\n" +
                      "Digit\tCount\tPercentage" + "\n")
        sum = 0
        for digit in range (1, 10):
            digitstringg = str(digit)
            sum += d1[digitstringg]
        for digit in range(1, 10):
            digitstring = str(digit)
            outfile.write(digitstring + "\t" + str(d1[digitstring]) + "\t" + format((d1[digitstring]/sum)*100, ".1f") + "\n")
    else:
        print("File does not exist")
        return

main()
