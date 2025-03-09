# program1
# def greatest(a,b,c):
#     if(a>b and a>c):
#         return a
#     elif(b>c):
#         return b
#     else:
#         return c
# a=4
# b=6
# c=12
# print(greatest(a,b,c))


# program2 fahrenheit to celsius
# def f_to_c(f):
#     return 5*(f-32)/9
# f=int(input("Enter temperature in f:"))
# print(f_to_c(f))
# print(f"{f_to_c(f)} °C")
# print(f"{round(f_to_c(f),2)} °C")


# program3---preventing print() function from new line

# print("a")
# print("b")
# print("c",end="")
# print("d",end="")

# program4--calculate sum of first n natural numbers using recursion

# def sum(n):
#     if(n==1):
#         return 1
#     return sum(n-1)+n

# print(sum(5))

# program5
# def pattern(n):
#     if(n==0):
#         return
#     print("*"*n)
#     pattern(n-1)
# pattern(5)

# program
def rem(l,word):
    for item in l:
        l.remove(word)
        return l
l=["siri","sonu","priya","nikita"]

print(rem(l,"sonu"))