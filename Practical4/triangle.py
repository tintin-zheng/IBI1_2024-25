"""
pseudocode:
    assign a origin value to a
    create a loop, to present the triangle from T1 to T10
    add the value of i to a
    print the value of T{i}
"""
#assign a value to a
a = 0
#creat a loop，to present the triangle from T1 to T10
for i in range (1,11) :
    #add the value of i to a
    a += i
    print(f"The value for the T{i} is {a}")