

gameboard = [0,
1,2,3,4,
5,6,7,8,
9,10,11,12,
13,14,15,0
]

width = 4
height = 4

playboard = [0,
1,2,3,4,
5,6,7,8,
9,10,11,12,
13,14,15,0
]

oloc = None

def edg(sel):
    edge = None
    match sel%4:
        case 1:
            # print("ledge")
            tzero(1)


        case 0:
            # print("redge")
            tzero(-1)

        case _:
            # print("else")
            tzero(-1)
            tzero(1)
    if oloc == None:
        lims(edge,sel)

def lims(ed,inp):
    hits = None
    match inp//4:
        
        case 0:
            hits = "T"
            # print("top")
            tzero(4)
        case 4:
            hits = "B"
            # print("bottom")
            tzero(-4)
        case _:
            hits = "N"
            # print("middle")
            tzero(-4)
            tzero(4)

def tzero(offset):
    # print(inpy,offset,playboard[inpy + offset])
    if playboard[inpy + offset] == 0:
        # print("set oloc",inpy+offset)
        oloc = inpy + offset
        swap(inpy,oloc)

def swap(one,two):
    playboard[one],playboard[two] = playboard[two],playboard[one]


def formalboard(board):
    print(board[1:5])
    print(board[5:9])
    print(board[9:13])
    print(board[13:17])





def loop():
    while True:
        global inpy
        print("\n"*3)
        formalboard(playboard)
        inpy = int(input("Space to move: "))
        global oloc
        # print("set oloc nun")
        oloc = None
        print()
        print()
        edg(inpy)
        if playboard == gameboard:
            return "win"


print(loop())



