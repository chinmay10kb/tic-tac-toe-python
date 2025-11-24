l1=[' ',' ',' ']
l2=[' ',' ',' ']
l3=[' ',' ',' ']
print(l1)
print(l2)
print(l3)
while True:
 p1=input('player 1,enter x or o:')
 if p1  in ('x','o','X','O'):
    break
    
if p1=='x':
    p2='o'
else:
    p2='x'
while True:
    row=(input(f'player {p1},enter row number 1,2,3:'))
    if row not in ('1','2','3'):
        print('entered wrong input')
        continue
    col=(input(f'player {p1},enter column number 1,2,3:'))
    if col not in ('1','2','3'):
        print('entered wrong input')
        continue
    if row=='1':
        selected_row=l1
    elif row=='2':
        selected_row=l2
    elif row=='3':
        selected_row=l3
    if selected_row[int(col)-1]!=' ':
        print('position already occupied,enter again')
        continue
    
    if row=='1':
        if col=='1':
            l1[0]=p1
        elif col=='2':
            l1[1]=p1
        elif col=='3':
            l1[2]=p1
    elif row=='2':
        if col=='1':
            l2[0]=p1
        elif col=='2':
            l2[1]=p1
        elif col=='3':
            l2[2]=p1
    elif row=='3':
        if col=='1':
            l3[0]=p1
        elif col=='2':
            l3[1]=p1
        elif col=='3':
            l3[2]=p1
    print(l1)
    print(l2)
    print(l3)
    if (l1[0]==l1[1]==l1[2]!=' ') or (l2[0]==l2[1]==l2[2]!=' ') or (l3[0]==l3[1]==l3[2]!=' ') or (l1[0]==l2[0]==l3[0]!=' ') or (l1[1]==l2[1]==l3[1]!=' ') or (l1[2]==l2[2]==l3[2]!=' ') or (l1[0]==l2[1]==l3[2]!=' ') or (l1[2]==l2[1]==l3[0]!=' '):
        break
    elif (l1[0]!=' ' and l1[1]!=' ' and l1[2]!=' ' and l2[0]!=' ' and l2[1]!=' ' and l2[2]!=' ' and l3[0]!=' ' and l3[1]!=' ' and l3[2]!=' '):
        break
    
    while True:
     row=(input(f'player {p2},enter row number 1,2,3:'))
     if row not in ('1','2','3'):
        print('entered wrong input')
        continue
     col=(input(f'player {p2},enter column number 1,2,3:'))
     if col not in ('1','2','3'):
        print('entered wrong input')
        continue
     if row=='1':
        selected_row=l1
     elif row=='2':
        selected_row=l2
     elif row=='3':
        selected_row=l3
     if selected_row[int(col)-1]!=' ':
        print('position already occupied,enter again')
     if selected_row[int(col)-1]==' ':
        break
     
    if row=='1':
        if col=='1':
            l1[0]=p2
        elif col=='2':
            l1[1]=p2
        elif col=='3':
            l1[2]=p2
    elif row=='2':
        if col=='1':
            l2[0]=p2
        elif col=='2':
            l2[1]=p2
        elif col=='3':
            l2[2]=p2
    elif row=='3':
        if col=='1':
            l3[0]=p2
        elif col=='2':
            l3[1]=p2
        elif col=='3':
            l3[2]=p2
    print(l1)
    print(l2)
    print(l3)
    if (l1[0]==l1[1]==l1[2]!=' ') or (l2[0]==l2[1]==l2[2]!=' ') or (l3[0]==l3[1]==l3[2]!=' ') or (l1[0]==l2[0]==l3[0]!=' ') or (l1[1]==l2[1]==l3[1]!=' ') or (l1[2]==l2[2]==l3[2]!=' ') or (l1[0]==l2[1]==l3[2]!=' ') or (l1[2]==l2[1]==l3[0]!=' '):
        break
    

if (l1[0]==p1 and l1[1]==p1 and l1[2]==p1) or (l2[0]==p1 and l2[1]==p1 and l2[2]==p1) or (l3[0]==p1 and l3[1]==p1 and l3[2]==p1) or (l1[0]==p1 and l2[0]==p1 and l3[0]==p1) or (l1[1]==p1 and l2[1]==p1 and l3[1]==p1) or (l1[2]==p1 and l2[2]==p1 and l3[2]==p1) or (l1[0]==p1 and l2[1]==p1 and l3[2]==p1) or (l1[2]==p1 and l2[1]==p1 and l3[0]==p1):
    print('player 1 wins')      
elif (l1[0]==p2 and l1[1]==p2 and l1[2]==p2) or (l2[0]==p2 and l2[1]==p2 and l2[2]==p2) or (l3[0]==p2 and l3[1]==p2 and l3[2]==p2) or (l1[0]==p2 and l2[0]==p2 and l3[0]==p2) or (l1[1]==p2 and l2[1]==p2 and l3[1]==p2) or (l1[2]==p2 and l2[2]==p2 and l3[2]==p2) or (l1[0]==p2 and l2[1]==p2 and l3[2]==p2) or (l1[2]==p2 and l2[1]==p2 and l3[0]==p2):
    print('player 2 wins')
else:
    print('draw')
