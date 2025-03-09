# def goodDay(name,ending):
#     print(f"Good morning, {name}")
#     print(ending)

# goodDay("Siri","Thank you")
# goodDay("Sonu","Thank you")
# goodDay("Haripriya","Thanks")
# goodDay("Kiranmai","Thanks")


# problem
# def greet(name,ending="Thank you"):
#     print("Good morning, "+name)
#     print(ending)

# greet("siri","get out")
# greet("sonu")


# problem
def fact(n):
    if(n==1 or n==0):
        return 1
    return n*fact(n-1)

n=int(input("enter number:"))
print(f"Factorial of {n} is {fact(n)}")