
print("Enter first number",sep=":", end="\n")
firstNumber= float(input("The firstnumber is "))
print("Enter Second number",sep=":", end="\n")
secondNumber= float(input("The secondnumber is "))

add = firstNumber + secondNumber
sub = firstNumber - secondNumber
multiply = firstNumber * secondNumber
div = firstNumber / secondNumber

operator = input("Enter the operation +, -, *, /")

if operator == "+" :
  print(add)
elif operator == "-" :
  print(sub)
elif operator == "*" :
  print(multiply)
elif operator == "/" :
  print(div)
else:
  print("Invalid operator entered.")