# COT 4930  Python Programming
# name: Aldrick Gardiner
# id  : agardiner2014
# lab : 01

def main ():

    MilesToKilometer()


def MilesToKilometer():
    
    #Kilometers input from user
    miles = float(input('Enter the amount of miles you want to convert: '))

    #Conversion From Miles To Kilometer
    kilometer = miles * 1.609

    #Print Conversion
    print('This converts to', kilometer, 'kilometers')
