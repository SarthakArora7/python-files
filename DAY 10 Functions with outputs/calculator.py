from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide,
}

def calculator():
  should_continue = True
  print(logo)
  operand1 = float(input("Enter the number : "))
  for symbol in operations:
    print(symbol)
  
  while should_continue:
    operation_symbol = input("Enter the operation to be done : ")
    operand2 = float(input("Enter the next number : "))
    operation_function = operations[operation_symbol]
    answer = operation_function(operand1, operand2)
    print(f"{operand1} {operation_symbol} {operand2} = {answer}")
    choice = input("Want to add another operation ?'y' for yes, 'n' for no and 'a' to start another calculation.")
    if choice == "y":
      operand1 = answer
    elif choice == "n":
      should_continue = False
    elif choice == "a":
      calculator()


calculator()