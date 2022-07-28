import numpy as np
y=int(input("enter the no of columns"))
p=int(input("enter the no of rows"))
if y>p:
    n=y
else:
    n=p        
h=np.zeros((y,p))
print(h)

m = 1

 
if y==p:  
    for k in range(p):
        
        row = 0
        col = k
        while (col >= 0):
            h[row][col]=m
            print('u',h)
            row += 1
            col -= 1
            m=m+1
    for j in range(1,y):
       
        col = y -1
        row = j
        while (row < y):
            h[row][col]=m
            print('l',h)
            row += 1
            col -= 1
        
            m=m+1
elif(y>p):
    for k in range(p):
        
        row = 0
        col = k
        while (col >= 0):
            h[row][col]=m
            print('u',h)
            row += 1
            col -= 1
            m=m+1
    for j in range(1,y):
       
        col = y -2
        row = j
        while (row < y):
            h[row][col]=m
            print('l',h)
            row += 1
            col -= 1
        
            m=m+1
else:
    for k in range(p):
        
        row = 0
        col = k
        while (col >= 0):
            h[row][col]=m
            print('u',h)
            row += 1
            col -= 1
            m=m+1
    for j in range(1,y):
       
        col = y -2
        row = j
        while (row < y):
            h[row][col]=m
            print('l',h)
            row += 1
            col -= 1
        
            m=m+1

r=np.array(h).transpose()
r=r[:p,:y]
for i in range(r.shape[0]):
    for j in range(r.shape[1]):
    
        print(int(r[i][j]),end='   ')
    print('\n')
      
