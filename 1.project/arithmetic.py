def arithmetic_operations(x, y):
    print("Arithmetic Operations:")
    print(f"{x} / {y} = {x / y}")
    print()

def logical_operations(x):
    print("Logical Operations:")
    print(f"x < 5 or x < 4: {x < 5 or x < 4}")
    print(f"not(x < 5 and x < 10): {not(x < 5 and x < 10)}")
    print()

def identity_vs_equality():
    print("Identity vs Equality:")
    x = ["apple", "banana"]
    y = ["apple", "banana"]
    z = x
    print(f"x is z: {x is z}")  # True
    print(f"x is y: {x is y}")  # False
    print(f"x == y: {x == y}")  # True
    print()

def list_operations():
    print("List Operations:")
    thislist = ["apple", "banana", "cherry"]
    print(f"Original list: {thislist}")
    print(f"thislist[1]: {thislist[1]}")
    print(f"thislist[-1]: {thislist[-1]}")
    print(f"thislist[1:2]: {thislist[1:2]}")
    thislist[1] = "avocado"
    print(f"After changing index 1: {thislist}")
    thislist[1:3] = ["blackcurrant", "watermelon"]
    print(f"After slice assignment: {thislist}")
    print()

def advanced_slicing():
    print("Advanced Slicing:")
    thislist2 = ["apple", "banana", "cherry", "orange", "kiwi", "melon"]
    print(f"Original list: {thislist2}")
    print(f"thislist2[2:5]: {thislist2[2:5]}")
    print(f"thislist2[:4]: {thislist2[:4]}")
    print()

def main():
    arithmetic_operations(5, 3)
    logical_operations(5)
    identity_vs_equality()
    list_operations()
    advanced_slicing()

if __name__ == "__main__":
    main()