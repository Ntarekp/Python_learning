age, weight, names = 10, 25.5, "John Kagabo"

print (age)
print(weight)
print(names)


x= y=5,10
print(x)

# packaging and unpacking
fruits = ["apple", "banana","cherry"]
x,y,z = fruits
print(x)
print(y)
print(z)

#  outputting variables
x = "Python "
y = "is "
z = "awesome"

print(x,y,z)
print(x+y+z)

x=5
y="John" 
#print(y+x) # shall get an error string can't concatinate with number or the reverse process
print(x,y)

# Global variables
x = "awesome"
def myfunc():
    x = "fantastic"
    print("Python is " + x)
    
myfunc()
print("Python is " +x)
#Global variables with a function use the gloabl keyword

def myfunction():
    global x
    x = "fantastic"
myfunction()
print("Python is " + x)

z = range(6)
print(z)

print(bytes(range(65, 91)).decode('utf-8') + bytes(range(97, 123)).decode('utf-8'))


a = "Hello World!"
print (a[-11])

# for x in "banana":
#     print (x)

# a = "Hello, World!"
# print(len(a))


b = "I must work to be successfull no matter what"
print(b[2:5])

print(b[1:1])