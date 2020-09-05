def pattern(n):
    x=65

    for i in range(0,n):
        ch = chr(x)
        x = x + 1

        for j in range(0,n-i-1):
            print(end=" ")
        for j in range(0,i+1):


            print(ch,end=" ")


        print("\r")
    x=65
    for i in range(n,1,-1):
        ch = chr(x)
        x = x + 1
        for j in range(0, n - i - 1):
            print(end=" ")
        for j in range(0, i+1 ):
            print(ch, end=" ")

        print("\r")
pattern(7)
"C:\Users\SRUTHI\Documents\sruthi.docx"




