## difference between tuples and list is that its contents cannot be changed  ####
'''  tuple is immutable. However it can contain mutable elements like list 
    All lists and tuples start with index 0 '''

car = ("Ford", 5, 34.4, "Raptor")

print(len(car))

### Merging Tuples ####

car2 = ("Second",)

carMerge = car + car2

### Nested tuples ####

carMerge = (car, car2)

print(carMerge)
### search using the in operator ###
print("Ford" in carMerge)

## index of a particular value ###

car.index("Ford")
