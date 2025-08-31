import math

def calculator():
    print("Advanced Calculator")
    print("You can use +, -, *, /, ** (power), sqrt(), sin(), cos(), log() etc.")
    print("Type 'exit' to quit\n")

    while True:
        expr = input("Enter expression: ")
        if expr.lower() == "exit":
            print("Exiting calculator...")
            break
        try:
            result = eval(expr, {"__builtins__": None}, math.__dict__)
            print("Result:", result)
        except Exception as e:
            print("Error:", e)

calculator()
