list = [
    "Prince",
    "is",
    "The",
    "best",
    "Candidate",
    "Ever",
    "who",
    "is",
    "going",
    "win",
    "for",
    "president",
]

# list[0] = ["NTARE","KAYITARE"] #it likely gives a complex dsa
print(list)

# inserting an element in a list

list.insert(2, "anelegant")

print(list)


print(list[-20:-14])
# Find the length of the list
list_length = len(list)
print(list_length)


list.sort(key=len)
print(list)


def myFunc(e):
    return len(e) > 4


list.sort(key=myFunc)
print(list)

filtered_list = [item for item in list if len(item) > 4]
print(filtered_list)

turple = (
    "Prince",
    "is",
    "The",
    "best",
    "Candidate",
    "Ever",
    "who",
    "is",
    "going",
    "win",
    "for",
    "president",
)
