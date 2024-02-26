# Nearest stars to Earth
# star1 = 'Sol'
# star2 = 'Alpha Centauri'
# star3 = 'Barnard'
# star4 = 'Wolf 359'

# Highest peak on each tectonic plate
# African = 'Kilimanjaro'
# Antarctic = 'Vinson'
# Australian = 'Puncak Jaya'
# Eurasian = 'Everest'
# North_American = 'Denali'
# Pacific = 'Mauna Kea'
# South_American = 'Aconcagua'



# Task 1: 
# Replace variables with list "stars"
# Create statement that prints the fourth nearest star

stars = ['Sol',
        'Alpha Centauri',
        'Barnard', 
        'Wolf 359',
        ]

print()
print("Fourth nearest star:", stars[3])
print("Fourth nearest star:", stars[-1])

print()

# Task 2:
# Create dictionary "peaks" that stars all values
# Create statement that prints name of highest peak on pacific plate

# Outcome should be like this:
# Wolf 359
# Mauna Kea

peaks = {
    "African":"Kilimanjaro",
    "Antarctic":"Vinson",
    "Australian":"Puncak Jaya",
    "Eurasian":"Everest",
    "North_American":"Denali",
    "Pacific":"Mauna Kea",
    "South_American":"Aconcagua", 
         }

print()

print("The highest peak on pacific plate is: ", peaks["Pacific"])

print()
print(stars[3])
print(peaks["Pacific"])
