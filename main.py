# Inna Kirian

"""
Simple Calculator
"""
# Provide your solution here

def calculate(a: int, b: int, operator: str) -> int:
    if operator == "-":
        print(a - b)
    elif operator == "+":
        print(a + b)
    elif operator == "*":
        print(a * b)
    elif operator == "/" and b != 0:
        print(a / b)
    elif operator == "/" and b == 0:
        print("Division by 0 is not allowed.")
    else:
        print("Invalid operator.")

# Test

calculate(3, 4, "+")
calculate(2, 8, "-")
calculate(5, 5, "*")
calculate(10, 0, "/")
calculate(3, 5, "/")
calculate(9, 4, "?")


"""
Reverse Word
"""
# Provide your solution here
def reverse_word(word: str) -> str:
    for i in range(len(word) -1, -1, -1):
    #for i in range(-1, -1-len(word), -1): # solution with negative indeces :)
        word = word.capitalize() # spent half an hour on this part, no idea how to make the other letter capitalized :(
        print(word[i], end="")

# Test

reverse_word("hello")
# reverse_word("WORLD")
# reverse_word("lEOn")


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print("Test your functions by calling them here. Use different parameter values to test them with different scenarios.")

