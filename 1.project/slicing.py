my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# Get elements from index 2 up to (but not including) index 5
print(my_list[2:5])  

# Get elements from the beginning up to index 4
print(my_list[:4])   

# Get elements from index 3 to the end
print(my_list[3:]) 

# Make a full copy of the list
print(my_list[:])    



my_lists = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get every second element
print(my_lists[::2])     

# Get every third element starting from index 1
print(my_lists[1::3])    

# Reverse the list by using a negative step
print(my_lists[::-1])    

# Reverse a sub-section of the list
print(my_lists[7:2:-1]) 


"""
Slicing with a negative step

"""
my_list = [10, 20, 30, 40, 50]

# Get the last two elements
print(my_list[-2:])   # Output: [40, 50]

# Get all elements except the last one
print(my_list[:-1])   # Output: [10, 20, 30, 40]

# Get elements from the third-to-last up to (but not including) the last
print(my_list[-3:-1]) # Output: [30, 40]

"""
Slicing with strings

"""
my_string = "Hello, World!"

# Extract the first 5 characters
print(my_string[:5])  # Output: 'Hello'

# Extract from index 7 to the end
print(my_string[7:])  # Output: 'World!'

# Reverse the entire string
print(my_string[::-1]) # Output: '!dlroW ,olleH'


"""
Outputting withou concatination

"""

def my_Converter(x):
    return x * 0.3048

txt = f" A plance can fly at {my_Converter(30000)} meter altitude"
print(txt)


price = 12.19234
formatted_price = f" The formatted price is ${price:.2f}"
print(formatted_price)


age = 18
message = f"You are {'eligible' if age >=18 else 'not eligible'} to vote."
print(message)

txt = "hello World".capitalize()
txt1 = "hello World".casefold()
txt2 = "hello World".center(30)
txt3 = "hello World".count('o')
txt4 = "hello World".endswith('.')
txt5 = "hello World".expandtabs(2)


print(txt)
print(txt1)
print(txt2)
print(txt3)
print(txt4)
print(txt5)




