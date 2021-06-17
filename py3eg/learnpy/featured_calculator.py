Sum = 0
numbers = []
index = 0
while True:
        try:
            line = input("enter a number or Enter to finish: ")
            if not line:
                break
            digit = int(line)
            Sum += digit
            numbers.append(digit)
        except ValueError as err:
            print(err)
for i in range(len(numbers)):
        j = i+1
        while 0 < j < len(numbers) and numbers[j] < numbers[j-1]:
                numbers[j],numbers[j-1] = numbers[j-1],numbers[j]
                j -= 1
index = int(len(numbers)/2)
median = numbers[index]
if index*2 == len(numbers):
        median = (numbers[index-1] + numbers[index])/2

if Sum:
    print("numbers: ", numbers)
    print("count =", len(numbers), "sum =", Sum, "lowest =",
          min(numbers), "highest =", max(numbers), "mean =",
          Sum/len(numbers), "median =", median)



























"""
lowest = None
highest = None
if lowest is None or lowest > number:
    lowest = number
if highest is None or highest < number:
    highest = number
"""
