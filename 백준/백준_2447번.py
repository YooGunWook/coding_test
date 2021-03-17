n = int(input())
dohwaji = [[' ' for i in range(n)] for _ in range(n)]

def draw(x,y,n):
    if n == 1:
        dohwaji[x][y] = '*'
        return
    div = int(n/3)
    draw(x,y, div)
    draw(x, y+div, div)
    draw(x, y+div+div, div)
    draw(x+div, y, div)
    draw(x+div, y+div+div, div)
    draw(x+div+div, y, div)
    draw(x+div+div, y+div, div)
    draw(x+div+div, y+div+div, div)
draw(0,0,n)
for i in range(n):
    print(''.join(dohwaji[i]))