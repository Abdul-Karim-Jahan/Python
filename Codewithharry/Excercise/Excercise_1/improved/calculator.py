from operator import calculate

print("Enter first number", sep=":", end="\n")
firstNumber = float(input("The first number is "))
print("Enter second number", sep=":", end="\n")
secondNumber = float(input("The second number is "))
operator = input("Enter the operation +, -, *, / ")

result = calculate(firstNumber, secondNumber, operator)
print(result)
