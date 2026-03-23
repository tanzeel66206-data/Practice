# i =1
# while(i<=10):
#     print("2 x ",i ," = ",2*i)
#     i+=1

# list1 = ["tanzeel",False,"khan","python","developer","java","c++","javascript"]

# i=0
# # for name in list1:    
# while(i<=len(list1)):
#     print(list1[i-1])    
#     i+=1

# for name in list1:
#     print(name)
    
# l1= ["tanzeel","khan","python","developer","java","c++","javascript"]

# for name in l1:
#     if(name.startswith("p")):
# #         print("The name starts with p: \n",name)
# #     else:
# #         print("The name does not start with p: \n",name)

# number = int(input("Enter a number: "))
# product = 1
# for i in range(1,number+1):   
#     product = product * i
    
# print(f"The factorial of {number} is {product}")

'''
   *
  * *
 * * *
* * * *
'''

# n=int(input("Enter number of rows: "))
# for i in range(n):
#     # print(" "*(n-i-1),end="")
#     # print("* "*(i+1))

#     print(" *"*(n-i),end="")
#     print("  "*(2*i-1))    



# n=int(input("Enter number of rows: "))
# for i in range (n):
#     print(" "*(n-i-1),end="")
#     print(" *"*(i+1))
'''


number = int(input("Enter a number: "))    

i= 1
while(i in range(1,11)):
    print(f"{number}x {i} ={number*i} ")
    i+=1

l=["harry", "soham", "shubham", "vishal"]

for name in l:
    if name.startswith("s"):
        print(f"hello {name} ")
            

number = int(input("Enter a number: "))
product = 1
for i in range(1,number+1):
    product= product * i
print(f"The factorial of {number} is {product}")

'''

# num= int(input("Enter a number: "))

# for i in range(1,num+1):
#     print(" "*(num-i),end="")
#     print("*"*(2*i-1),end="")
#     print("")

'''
****
*  *
*  *
****

# '''

# n= int(input("Enter number of rows: "))

# for i in range(n):
#     if(i==0 or i==n-1):
#         print("*"*n)
#     else:
#         print("*"+" "*(n-2)+"*")

# for i in range(n):
#     print("*"*(2*i-1),end="")
#     print("")

n= int(input("Enter number "))
sum = 0
if n>=1:
    for i in range(1,n+1):
        sum= sum + i
    print(f"sum of {n} is {sum}")
        