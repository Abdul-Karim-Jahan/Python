def calculate(firstNumber, secondNumber, operator):
    add = firstNumber + secondNumber
    sub = firstNumber - secondNumber
    multiply = firstNumber * secondNumber
    div = firstNumber / secondNumber
    
    if operator == "+" :
        return add
    elif operator == "-" :
        return sub
    elif operator == "*" :
        return multiply
    elif operator == "/" :
        return div
    else:
        return "Invalid operator entered."
