# List [] = mutable, most flexible
# Tuple () = immutable, faster
# Set {} = mutable (add/remove), unordered,
#          No duplicates, best for membership testing

# List --------------
fruits = ["apple", "orange", "banana", "coconut"]

fruits[0] = "pineapple"
fruits.append("mango")
fruits.remove("banana")
fruits.pop(1)
# fruits.clear()

for fruit in fruits:
    print(fruit, end=" ")

print()

# Tuple --------------
fruits1 = ("apple", "orange", "banana", "coconut")

# Set ----------------
fruits2 = {"apple", "orange", "banana", "coconut", "coconut"}

fruits2.add("mango")
fruits2.remove("apple")
for fruit2 in fruits2:
    print(fruit2)

if "orange" in fruits2:
    print("Orange was found")