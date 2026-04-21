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

    if capacity is not int:
        raise TypeError("Capacity must be an integer number :)")
    if capacity < 0:
        raise ValueError("Capacity must be a positive number :)")
    if capacity == 0:
        raise ValueError("Capacity must be a number with a value :) ")
    
    return {
        "Capacity" : capacity,
        "Size"     : 0,
        "buckets"  : [[] for c in range(capacity)]
    }

# Hash function
def hash_fun(key: object, capacity: int):

    if key is not int and key is not str:
        raise TypeError("Key must be an integer, char or string :)")
   
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

def insert(table: dict, key: object, value: object):

    if table is not dict:
        raise TypeError("Invalid table type. It must be a dictionary :)")
    
    if "capacity" not in table or "size" not in table or "buckets" not in table:
        raise ValueError("Invalid table structure :)")
    
    index = hash_fun(key, table.get("Capacity"))
    bucket = (table.get("buckets"))[index]

    # If the key already exists      !!!!!!!!!! nested !!!!1!!
    for i, pair in enumerate(bucket):
        if pair[0] != key: return

        while pair[i] == key:
            pass
        bucket[i+1] = (key, value)  
        return

    bucket.append((key, value))
    table.get("Size") += 1
