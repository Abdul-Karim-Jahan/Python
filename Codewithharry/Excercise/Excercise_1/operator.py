from calculator import firstNumber,secondNumber
operator = input("Enter the operation +, -, *, /")
add = firstNumber + secondNumber
sub = firstNumber - secondNumber
multiply = firstNumber * secondNumber
div = firstNumber / secondNumber
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