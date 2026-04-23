# Name                   : Yasmeen Abu Arrah
# Student ID             : 202211471
# Date                   : 21 Apr. 2026
# Chosen Data Structure  : Hash Table :)


# Create the main table "Hash Table" 
def create_table(capacity: int):

    if isinstance(capacity, bool):       
        raise TypeError("Capacity must be an integer, not a boolean :)")
    if not isinstance(capacity, int):
        raise TypeError("Capacity must be an integer number :)")
    if capacity < 0:
        raise ValueError("Capacity must be a positive number :)")
    if capacity == 0:
        raise ValueError("Capacity must be a number with a value :) ")
    
    return {
        "Capacity" : capacity,
        "Size"     : 0,
        "Buckets"  : [[] for c in range(capacity)]
    }


# Validate the table type
def validate_table(table: dict):

    if not isinstance(table, dict):
        raise TypeError("Invalid table type. It must be a dictionary :)")
    
    if "Capacity" not in table or "Size" not in table or "Buckets" not in table:
        raise ValueError("Malformed table")


# Hash function to calculate the index for a given key
def hash_fun(key, capacity: int):

    if not isinstance(key, (int, str)):
        raise TypeError("Key must be an integer, char or string :)")
    
    if isinstance(key, int):
        index = key % capacity 

    if isinstance(key, str):
        total = 0
        for char in key:
            if 65 <= ord(char) <= 90:
                total += (ord(char) - 65)
            elif 97 <= ord(char) <= 122:
                total += (ord(char) - 97)
        index = total % capacity                

    return index


# Insert a key-value pair into the table || as a dict :)
def insert(table: dict, key, value):

    validate_table(table)
    if check(table, key): 
        raise KeyError("Key already exists in the table :)")  
    
    index = hash_fun(key, table["Capacity"])
    bucket = table["Buckets"][index]

    bucket.append({key: value})
    table["Size"] += 1


# Get the value associated with a key in the table
def get(table: dict, key):

    validate_table(table)
    index = hash_fun(key, table["Capacity"])
    bucket = table["Buckets"][index]

    for i in bucket:
        if key in i:
            return i[key]
    
    raise KeyError("Game Over! Key not found in the table :)")


# Check if a key exists in the table
def check(table: dict, key):

    validate_table(table)
    index = hash_fun(key, table["Capacity"])
    bucket = table["Buckets"][index]

    for i in bucket:
        if key in i:
            return True
        
    return False


# Get the size of the table (number of key-value pairs)
def size(table: dict):

    validate_table(table)
    return table["Size"]


# Check if the table is empty (size is 0)
def is_empty(table: dict):

    validate_table(table)
    return table["Size"] == 0


# Delete a key-value pair from the table
def delete(table: dict, key):

    validate_table(table)
    if is_empty(table):
        raise ValueError("The table is empty, nothing to delete :)")
    if not check(table, key):                     
        raise KeyError("Key not found in the table :)")
    
    index = hash_fun(key, table["Capacity"])
    bucket = table["Buckets"][index]

    for i in range(len(bucket)):
        if key in bucket[i]:
            del bucket[i]
            table["Size"] -= 1
            return "Now, key not found in the table :)"


# Update the value of an existing key in the table:
def update(table: dict, key, value):

    validate_table(table)
    index = hash_fun(key, table["Capacity"])
    bucket = table["Buckets"][index]

    if check(table, key) == False:
        raise KeyError("Key not found in the table :)")
     
    for i in bucket:
        if key in i:
            i[key] = value
            return "Key updated successfully :)"
        

# Return all keys in the table:
def keys(table: dict):

    validate_table(table)
    all_keys = []
    for bucket in table["Buckets"]:
        for pair in bucket:
            all_keys.extend(pair.keys())
    
    return all_keys 


# Clear the table
def clear(table: dict):

    validate_table(table)
    table["Buckets"] = [[] for c in range(table["Capacity"])]
    table["Size"] = 0

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

    create_table   : O(n)
    validate_table : O(1)  
    hash_fun       : O(k) when k is the len(key string) 
    insert         : O(1)
    get            : O(1)
    delete         : O(1) 
    check          : O(1) on average
    size           : O(1)
    is_empty       : O(1)
    update         : O(1) 
    keys           : O(n) 
    clear          : O(n) 

   insert, get, delete and check fun.s: O(n) in the worst case.
   --> when all keys hash to the same index :)

"""


# Test
if __name__ == "__main__":

    print("\n\nHello Mr.Hussien | welcome to the Hash Table :)")
    print("\nTest #1: Normal usage | happy path ")
    table = create_table(4)         
    insert(table, 1, "Ahmad")
    insert(table, 2, "Osaid")
    insert(table, 6, "Mohammad")
    print(table)  
    print("Size of the table:", size(table))    
    print("The value of key 1 is:", get(table, 1))  
    print("The value of key 2 is:", get(table, 2))     
    print("Is the key 1 exists in the table?", check(table, 1))    
    print("Is the key 3 exists in the table?", check(table, 3))   
    print("Deleted key 1:", delete(table, 1))       
    print("Size of the table now:", size(table))      
    print("Is the table empty?", is_empty(table))  

    print("\nTest #2: Edge cases | empty table")
    empty_table = create_table(2)
    print("Is the table empty?", is_empty(empty_table))   
    print("Size of the table:", size(empty_table))

    print("\nTest #3 : Error validation | try/except blocks")
    try:
        insert(table, 2, "Mohammad") 
    except KeyError as e:
        print(e)

    try:
        get(table, 5)
    except KeyError as e:
        print(e)

    try:
        delete(empty_table, 1)
    except ValueError as e:
        print(e)    
    
    try:
        create_table(-1)
    except ValueError as e:
        print(e)
    
    try:
        create_table(0)
    except ValueError as e:
        print(e)

    try:
        create_table(3.5)
    except TypeError as e:
        print(e)

    try:
        create_table(True)
    except TypeError as e:
        print(e)

    try:
        insert(table, 3.5, "Invalid Key")   
    except TypeError as e:
        print(e)

    try:
        delete(table, 8)
    except KeyError as e:  
        print(e)

    print("\nTest #4 : Colliction demonstrain | same index for different keys")
    table2 = create_table(3)
    insert(table2, "a", "First")
    insert(table2, "d", "Second")
    insert(table2, "n", "Third")
    print(table2["Buckets"])
    print("The value of key 'a' is:", get(table2, "a"))
    print("The value of key 'd' is:", get(table2, "d")) 
    print("The value of key 'n' is:", get(table2, "n"))

    print("\nTest #5 : Additional function | update | return keys | clear")
    print("Before update:", get(table, 2))  
    print(update(table, 2, "Updated Osaid "))
    print("After update:", get(table, 2))

    try:
        update(table, 3, "not working!")   
    except KeyError as e:
        print(e)

    print("All keys in the table:", keys(table))

    clear(table)
    print("Table after clearing:\n",table)


    print("\nThank You! I hope the work is clear and meets your expectations :)\n")

    

