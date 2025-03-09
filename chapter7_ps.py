# program1

# n=int(input("enter number: "))

# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")



# # program2
# l=["Siri","Sonu","haripriya","kiranmai"]
# for item in l:
#     print(f"Hii {item}")


# problem3
# i=1
# n=int(input("enter number: "))
# while(i<11):
#     print(f"{n} * {i} = {n*i}")
#     i=i+1


# problem4
# n=int(input("enter number: "))

# for i in range(2,n):
#     if(n%i==0):
#         print("not prime")
#         break
# else:
#     print("prime")


# problem5
# n=int(input("enter number: "))
# i=0
# s=0
# while(i<=n):
#     s+=i
#     i+=1
# print(s)


# problem6
# n=int(input("enter number: "))
# f=1
# for i in range(1,n+1):
#     f=f*i
# print(f"The factorial of {n} is {f}")

# problem7
# n=int(input("enter number: "))

# for i in range(1,n+1):
#     print(" "* (n-i), end="")
#     print("*"*(2*i-1),end="")
#     print("\n")


# n=int(input("enter number: "))

# for i in range(1,n+1):
#     print(" "* (n-i), end="")
#     print("*"*i,end="")
#     print("")


# problem8
# n=int(input("enter number: "))
# for i in range(1,n+1):
#     print("*"*i)
    

# problem9
# n=int(input("enter number: "))
# for i in range(1,n+1):
#     if(i==1 or i==n):
#         print("*"*n,end="")
#     else:
#         print("*",end="")
#         print(" "*(n-2),end="")
#         print("*",end="")
#     print("")

# problem10//multiplication table in reverse order
n=int(input("enter number: "))

for i in range(1,11):
    print(f"{n}*{11-i}={n*(11-i)}")