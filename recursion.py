
# def factorial(n):
#     if(n==1 or n==0):
#         return 1
#     return n * factorial(n-1)

# n = int(input("Enter number: "))
# print(f"The factorial of {n} is {factorial(n)}")

# def sum_of_n(n):
#     if(n==1):
#         return 1
#     return n + sum_of_n(n-1)

# print("Enter a number: ")
# n = int(input())        
# print(f"The sum of first {n} natural numbers is: {sum_of_n(n)}")

def pattern(n):
    if(n==0):
        return
    pattern(n-1)
    print("* "*n)

pattern(5)