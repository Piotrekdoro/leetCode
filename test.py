#rows=[{},{},{}]
#rows=[{}]*3
rows=[{} for sub in range(3)]
print(rows)
print('****************************************')

for i in range(len(rows)):
    rows[i][i]=i+1
    print(rows)
    print('****************************************')

test=[0]*6
print(test)