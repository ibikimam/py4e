found = None
print('Before', found)
for value in [9,41,12,3,74,15] :
    if value == 3 :
        found = True
        print(True, value)
    elif value != 3 :
        print(False, value)
print('After', found)            