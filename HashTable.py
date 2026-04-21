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

    if capacity != int(capacity):
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

def validate_table(table: dict):
    if table != dict(table):
        raise TypeError("Invalid table type. It must be a dictionary :)")
    
    # if "capacity" not in table or "size" not in table or "buckets" not in table:
        raise ValueError("Invalid table structure :)")

# Hash function
def hash_fun(key, capacity: int):

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


def insert(table: dict, key, value):

    validate_table(table)
    if check(table, key): 
        raise KeyError("Key already exists in the table :)")  
    
    index = hash_fun(key, table.get("Capacity"))
    bucket = (table.get("buckets"))[index]

    bucket.append((key, value))
    table["Size"] = 1 + table.get("Size")


def get(table: dict, key):

    validate_table(table)

    index = hash_fun(key, table.get("Capacity"))
    bucket = (table.get("buckets"))[index]

    for i, pair in bucket:
        if pair[i] == key:
            return pair[i]
        
    raise KeyError("Game Over! Key not found in the table :)")


def check(table: dict, key):

    validate_table(table)
    
    for i in table.get("buckets"):
        if i == key:
            return True
        
    return False


def size(table: dict):

    validate_table(table)
    return table.get("Size")


def is_empty(table: dict):

    validate_table(table)
    return table.get("Size") == 0


def delete(table: dict, key):

    validate_table(table)
    if is_empty(table):
        raise ValueError("The table is empty, nothing to delete :)")
    
    index = hash_fun(key, table.get("Capacity"))
    bucket = (table.get("buckets"))[index]

    for i, pair in bucket:
        if pair[i] == key:
            del bucket[i]
            table["Size"] = table.get("Size") - 1
            return
        
    raise KeyError("Now, key not found in the table :)")



"""
Usage Section:
Choose any positive number as a capacity, 
then create the table and insert any key-value pair you like :)

    table = create_table(4)         
    insert(table, 1, "Ahmad")
    insert(table, 2, "Osaid")
    insert(table, 2, "Mohammad") --> Error.
    insert(table, 6, "Mohammad")


        
Use any function you want to test the table, for example:

    get(table, 1)     | "Ahmad"
    get(table, 2)     | "Osaid" or "Mohammad" 
    check(table, 1)   | True    
    check(table, 3)   | False
    delete(table, 1)  | remove Ahmad from the table
    size(table)       | 2
    is_empty(table)   | False

        
Time Complexity:

    create_table   : O(1)
    validate_table : O(1)  
    hash_fun       : O(k) when k is the len(key string) 
    insert         : O(1)
    get            : O(1)
    delete         : O(1) 
    check          : O(1) on average
    size           : O(1)
    is_empty       : O(1)

   insert, get, delete and check fun.s: O(n) in the worst case.
   --> when all keys hash to the same index :)

"""


# Test
if __name__ == "__main__":

    print("Hello Mr.Hussien | welcome to the Hash Table :)")
    print("Test #1: create & get | number key")
    table = create_table(4)         
    insert(table, 1, "Ahmad")
    insert(table, 2, "Osaid")
    insert(table, 6, "Mohammad")

    print(get(table, 1))     # Ahmad
    print(get(table, 2))     # Osaid or Mohammad 
    print(check(table, 1))   # True    
    print(check(table, 3))   # False
    delete(table, 1)        # remove Ahmad from the table
    print(size(table))      # 2
    print(is_empty(table))  # False