color = {'black':[0,1], 'brown' :[1,10],'red':[2,100],'orange':[3,1_000],
'yellow':[4,10_000], 'green':[5,100_000],
'blue':[6,1_000_000],'violet':[7,10_000_000],
'grey':[8,100_000_000],'white':[9,1_000_000_000]}

if __name__ == "__main__":
    a = input().rstrip()
    b = input().rstrip()
    c = input().rstrip()
    print((color[a][0]*10 + color[b][0])*color[c][1])