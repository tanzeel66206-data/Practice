try:
    # Taking input from user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    # Performing division
    result = num1 / num2
    
    print("Result:", result)

except ValueError:
    print("Invalid input! Please enter numbers only.")

except ZeroDivisionError:
    print("Cannot divide by zero!")

except Exception as e:
    print("Something went wrong:", e)