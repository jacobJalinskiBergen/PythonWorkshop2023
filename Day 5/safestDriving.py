"""
Write a python program that finds the region with the least 
number of accidents between north, south, east, west, and central.
User must enter all 5 regions, one at a time.
"""

#This could have been a dictionary
class Region:
    def __init__(self, name):
        self.name = name
        self.accidents = 0

def getNumAccidents(region):
    accidents = int(input("Please enter the number of accidents in " + region.name + ": "))
    while accidents < 0:
        accidents = int(input("Please enter the number of accidents in " + region.name + " (But do it right this time): "))
    region.accidents = accidents   

def findLowest(allRegions):
    minReg = allRegions[0]
    for region in allRegions:
        if minReg.accidents > region.accidents:
            minReg = region
    print(minReg.name, minReg.accidents, sep=": ")

def main():
    NAMES = ("North", "South", "East", "West", "Central")
    regs = [Region(name) for name in NAMES]
    """
    for name in NAMES:
        regs.append(Region(name))
    """
    for i in regs:
        getNumAccidents(i)
    findLowest(regs)

main()