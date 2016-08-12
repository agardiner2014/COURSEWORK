# COT 4930  Python Programming
# name: Aldrick Gardiner
# id  : agardiner2014
# lab : 02


def fib():
 a,b = 0,1
 while True:
     num = int(input("Enter a Number sequence: "))
     if num <= 20: break
     print("\nEnter a number in the range from 2 to 20\n")
 myList = []
 myList.append(a)
 for i in range(num-1):
     a,b = b,a+b
     myList.append(a)

 for i in range(0, len(myList), 6):
     outputString = (str(myList[i:i+6])).replace(",", "     ").replace("[","").replace("]","")
     print(outputString)

fib()
 


    

