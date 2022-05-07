from mailbox import NoSuchMailboxError


number_seq = range(0,10)
number_list = list(number_seq)
print(number_list)

world_cup_winners = [[2006, "Italy"], [2010, "Spain"],
                     [2014, "Germany"], [2018, "France"]]
print(world_cup_winners[0][1])

A = [3, 4, 5]
B = [0, 1, 2]

A.insert(0, 9)
print(A)
