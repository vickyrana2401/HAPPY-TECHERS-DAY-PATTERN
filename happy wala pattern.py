
for i in range(5):
    for j in range(5):          # H
        if j==0 or j==4 or i==2:
            print('0',end='')
        else :
            print(' ',end='')
    for j in range(1):          #one line
        print(' ',end='')
    for j in range(5):          #A
        if j==0 or j==4 or i==0 or i==2:
            print('0',end='')
        else :
            print(' ',end='')
    for j in range(1):          #one line
        print(' ',end='')
    for j in range(5):          #P
        if j==0 or i==0 or i==2 or (j==4 and i==1):
            print('0',end='')
        else :
            print(' ',end='')
    for j in range(1):          #one line
        print(' ',end='')
    for j in range(5):          #P
        if j==0 or i==0 or i==2 or (j==4 and i==1):
            print('0',end='')
        else :
            print(' ',end='')
    for j in range(1):          #one line
        print(' ',end='')
    for j in range(5):          #Y
        if (i==j and i<3) or (j==2 and i>2) or (i==0 and j==4) or (i==1 and j==3) :
            print('0',end='')
        else :
            print(' ',end='')   
    print()
print()
print()
print()

for i in range(5):          #T
    for j in range(5):
        if i==0 or j==2:
            print('0',end='')
        else :
            print(' ',end='')
    for j in range(1):          #one line
        print(' ',end='')

    for j in range (5):     #E
        if i in [0,2,4] or j==0:
            print('0',end='')
        else :
            print(' ',end='')
    for j in range(1):          #one line
        print(' ',end='')
    for j in range(5):          #A
        if j==0 or j==4 or i==0 or i==2:
            print('0',end='')
        else :
            print(' ',end='')
    for j in range(1):          #one line
        print(' ',end='')
    for j in range (5):     #C
        if i in [0,4] or j==0:
            print('0',end='')
        else :
            print(' ',end='')
    for j in range(1):          #one line
        print(' ',end='')
    for j in range(5):          # H
        if j==0 or j==4 or i==2:
            print('0',end='')
        else :
            print(' ',end='')
    for j in range(1):          #one line
        print(' ',end='')
    for j in range (5):     #E
        if i in [0,2,4] or j==0:
            print('0',end='')
        else :
            print(' ',end='')
    for j in range(1):          #one line
        print(' ',end='')
    for j in range (5):     #R
        if i in [0,2] or j==0 or(i==3 and j==2)or(i==4 and j==3) or (i==1 and j==4):
            print('0',end='')
        else :
            print(' ',end='')
    for j in range(1):          #one line
        print(' ',end='')
    for j in range (5):     #S
        if i in [0,2,4] or i+j==1 or i+j==7:
            print('0',end='')
        else :
            print(' ',end='')
    for j in range(1):          #one line
        print(' ',end='')
    for j in range (3):     #'
        if i in [0,1] or ((i+j==4)and j!=0):
            print('0',end='')
        else :
            print(' ',end='')
    for j in range(1):          #one line
        print(' ',end='')        
    print()
            
print()
print()
print()

for i in range(5):          #D
    for j in range(5):
        if i in [0,4] or j in [1,4]:
            print('0',end='')
        else :
            print(' ',end='')
    for j in range(1):          #one line
        print(' ',end='')
    for j in range(5):          #A
        if j==0 or j==4 or i==0 or i==2:
            print('0',end='')
        else :
            print(' ',end='')
    for j in range(1):          #one line
        print(' ',end='')
    for j in range(5):          #Y
        if (i==j and i<3) or (j==2 and i>2) or (i==0 and j==4) or (i==1 and j==3) :
            print('0',end='')
        else :
            print(' ',end='') 
    print()
