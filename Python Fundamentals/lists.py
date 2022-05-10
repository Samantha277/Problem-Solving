from mailbox import NoSuchMailboxError


number_seq = range(0,10)
number_list = list(number_seq)
print(number_list)

world_cup_winners = [[2006, "Italy"], [2010, "Spain"],
                     [2014, "Germany"], [2018, "France"]]
print(world_cup_winners[0][1])

A = [3, 4, 5]
B = [0, 1, 2]

### common list operations ###

A.append(4)    ## insert 4 at the end

A.insert(0, 9)   ## insert 9 at position 0

A.pop()   ## delete the last element

A.remove(3)  ## delete the element with value 3

A[0:2]  ### Slice list A. start from position 0 to 2

A[0::2] ## Slice start from position 0 to end. Print every 2nd element

A.index(5)  ## search the index of 5

A.sort()  ## sort list A
print(A)
