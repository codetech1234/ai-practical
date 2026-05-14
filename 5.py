import random

b = [' '] * 9

def show():
    print(b[0], b[1], b[2])
    print(b[3], b[4], b[5])
    print(b[6], b[7], b[8], "\n")

def win(p):
    w = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(b[a]==b[b1]==b[c]==p for a,b1,c in w)

while True:
    show()
    
    m = int(input("Enter 1-9: ")) - 1
    if b[m] == ' ':
        b[m] = 'X'
    if win('X'):
        show(); print("You Win"); break
    
    empty = [i for i in range(9) if b[i]==' ']
    if not empty:
        print("Draw"); break
    c = random.choice(empty)
    b[c] = 'O'
    if win('O'):
        show(); print("Computer Wins"); break