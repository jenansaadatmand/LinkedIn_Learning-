value = input('Enter a number: ') # input always stores value as string

print(value + " is my favourite number!") # concatenation of two strings
print()

print('When you multiply by 10, this is what you get:')

print(value * 10) # multiplication or replication of strings not the same as multiplying by 10 because value is a string, need to be converted to integer before performing mathematical operations
print()
print('When you multiply by 10, this is what you get:')
print(int(value) * 10) # converting string to integer using int()
print()


# solution 2: 

value_int = int(value)  # converting strin gto a number integer, saved in a variable 
print(value_int * 10)
