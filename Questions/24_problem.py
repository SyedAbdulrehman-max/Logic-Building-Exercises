# 24. Find the smallest number in a list of 5 numbers.
l = [2,52,42,3]
smaler = l[0]
for i in l:
    if i < smaler:
        smaler = i

print(smaler)