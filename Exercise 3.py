a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

#create a new list with the required condition
a_1 = [ i for i in a if i<5 ]

#whats difference between for and while
for i in a:
    if i <5:
        print(i)

print(a_1)
        
'''What is the meaning of this code
for i in a:
    a_1 = [ i|i<5 ]'''