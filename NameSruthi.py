str="SRUTHI"
print_S=[[" " for i in range(5)] for j in range(5)]
print_R=[[" " for i in range(5)] for j in range(5)]
print_U=[[" " for i in range(5)] for j in range(5)]
print_T=[[" " for i in range(5)] for j in range(5)]
print_H=[[" " for i in range(5)] for j in range(5)]
print_I=[[" " for i in range(5)] for j in range(5)]


for row in range(5):
    for col in range(5):
        if ((row==0 or row==2 or row==4) and (col>0 and col<4)) or ((row==1 or row==4) and col==0) or ((row==0 or row==3) and col==4):
            print_S[row][col]="*"

for row in range(5):
    for col in range(5):
        if col==0 or ((row==0 or row==2)and (col>0 and col<4)) or (col==4 and (row!=0 and row!=2)):
            print_R[row][col]="*"

for row in range(5):
    for col in range(5):
        if ((col==0 or col==4) and (row!=4)) or (row==4 and (col>0 and col<4)):
            print_U[row][col]="*"


for row in range(5):
    for col in range(5):
        if row==0 or (col==2 and row!=0):
            print_T[row][col]="*"

for row in range(5):
    for col in range(5):
        if (col==0 or col==4) or (row==2 and (col>0 and col<4)):
            print_H[row][col]="*"

for row in range(5):
    for col in range(5):
        if (row==0 or row==4) or (col==2 and (row>0 and row<4)):
            print_I[row][col]="*"





for i in range(5):
    for j in range(5):
        print(print_S[i][j],end=" ")
    print(end=" ")
    for j in range(5):
        print(print_R[i][j],end=" ")
    for j in range(5):
        print(print_U[i][j],end=" ")
    print(end=" ")
    for j in range(5):
        print(print_T[i][j],end=" ")
    for j in range(5):
        print(print_H[i][j],end=" ")
    print(end=" ")
    for j in range(5):
        print(print_I[i][j],end=" ")
    print()