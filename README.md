<div align="center">

```
        ██╗  ██╗ █████╗ ███████╗██╗  ██╗    ████████╗ █████╗ ██████╗ ██╗     ███████╗
        ██║  ██║██╔══██╗██╔════╝██║  ██║    ╚══██╔══╝██╔══██╗██╔══██╗██║     ██╔════╝
        ███████║███████║███████╗███████║       ██║   ███████║██████╔╝██║     █████╗  
        ██╔══██║██╔══██║╚════██║██╔══██║       ██║   ██╔══██║██╔══██╗██║     ██╔══╝  
        ██║  ██║██║  ██║███████║██║  ██║       ██║   ██║  ██║██████╔╝███████╗███████╗
        ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝       ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝
```

###  Python · Procedural · Pure · No Imports

---

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Paradigm](https://img.shields.io/badge/Paradigm-Procedural%20%2F%20Functional-FF6B35?style=for-the-badge)
![OOP](https://img.shields.io/badge/OOP-Zero%20Classes-red?style=for-the-badge)
![Imports](https://img.shields.io/badge/Imports-None%20Whatsoever-black?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Assignment%20Complete-28A745?style=for-the-badge)

</div>

---

## 📌 About This Repository

> **This is the solution to a university programming assignment** focused on implementing a fundamental data structure **from scratch** in Python.

The assignment required:
- ✅ Choosing **one** data structure and researching it deeply
- ✅ Implementing it using a **strictly procedural / functional style** — functions only, no OOP
- ✅ Writing **zero import statements** — not even `sys`, `math`, or `collections`
- ✅ Covering all standard operations with **robust error handling**
- ✅ Adding full **documentation, type hints, and a usage guide**
- ✅ Proving correctness with **5+ distinct test scenarios**

**Chosen Data Structure → `Hash Table` 🗂️**

---

## 🗂️ What Is a Hash Table?

A **Hash Table** is a data structure that maps **keys to values** using a **hash function** to compute an index into an array of buckets, from which the desired value can be found.

```
Key ──► [ hash_fun(key) ] ──► index ──► Bucket [ {key: value}, ... ]
```

It is one of the most powerful and widely used data structures in computer science — the backbone of Python dictionaries, database indexing, caching systems, and compilers.

---

## 🏗️ Internal Structure

The hash table is represented as a plain Python `dict` — **no classes, no objects**:

```python
table = {
    "Capacity" : 4,           # Number of buckets
    "Size"     : 0,           # Active key-value pairs
    "Buckets"  : [[], [], [], []]   # Lists of {key: value} dicts
}
```

Every function receives this dictionary **explicitly** as its first argument — true to the procedural paradigm.

---

## ⚡ Collision Handling

This implementation uses **Separate Chaining**:

- Each bucket is a **list** of `{key: value}` pairs
- Multiple keys that hash to the same index are **chained** in that bucket's list
- Lookup traverses the chain linearly — still O(1) average when load is low

```
Bucket[0] → [{1: "Ahmad"}, {5: "Khaled"}]   ← collision! keys 1 and 5 both hash to 0
Bucket[1] → [{2: "Osaid"}]
Bucket[2] → []
Bucket[3] → [{6: "Mohammad"}]
```

---

## 📁 File Structure

```
📦 Hash-Table-Python
 ┗ 📜 HashTable.py        ← The complete implementation + tests
 ┗ 📜 index.html          ← AI generation page to present the idea
 ┗ 📜 README.md           ← You are here :)
```

## 🚀 Live Demo
https://yasmeen-abu-arrah.github.io/Implement-Hash-Table/

---


<div align="center">

*</> Built with Python · Pure Logic*

</div>
