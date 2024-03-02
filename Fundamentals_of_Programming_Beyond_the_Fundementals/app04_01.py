value = input('Enter a number: ') # Input always stores value as string

print(value + " is my favourite number!") # Concatenation of two strings
print()

print('When you multiply by 10, this is what you get:')

print(value * 10) # Multiplication or replication of strings is not the same as multiplying by 10 because value is a string, need to be converted to integer before performing mathematical operations
print()
print('When you multiply by 10, this is what you get:')
print(int(value) * 10) # Converting string to integer using int()
print()


# Solution 2: 

value_int = int(value)  # Converting string to a number integer, saved in a variable 
print(value_int * 10)
