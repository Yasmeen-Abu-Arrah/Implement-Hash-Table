# Name                  : Yasmeen Abu Arrah
# Student ID            : 202211471
# Date                  : 21 Apr. 2026
# Chosen Data Structure : Hash Table :)

# Attempt #1
# Hash Table --> hash function, index, array and maybe singly linked list
# hash fun. --> capacity and key (%)
# collision --> chaining method --> list :)
# fun.s : create table/ hash/ insert/ get/ delete/ find(t/f)/ size/ ?

# Create the main table "Hash Table" 
def create_table(capacity: int):
    #uncomplete
    return {
        "Capacity" : capacity,
        "Size"     : 0,
    }

# Hash function
def hash_fun(key: object, capacity: int):

    if key is int:
        index = key % capacity 

    if key is str:
        total = 0
        for char in key:
            if 65 <= ord(char) <= 90:
                total += (ord(char) - 65)
            elif 97 <= ord(char) <= 121:
                total += (ord(char) - 97)
        index = total % capacity                

    return index