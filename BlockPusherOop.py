class BlockPusher:

    def __setitem__(self,key,value):
        self.PlayBoard[key-1] = value
    
    def __getitem__(self,key):
        return self.PlayBoard[key-1]

    def __init__(self,defboard = None):
        self.gameboard = [
        1,2,3,4,
        5,6,7,8,
        9,10,11,12,
        13,14,15,0
        ]

        self.width = 4
        self.height = 4

        if defboard == None:
            self.PlayBoard = [
            1,2,3,4,
            5,6,7,8,
            9,10,11,12,
            13,14,15,0
            ]

        else:
            self.PlayBoard = defboard
    def ZIndex(self):
        return self.PlayBoard.index(0) +1 

    def HasWon(self):
        if self.gameboard == self.PlayBoard:
            return 1
        else:
            return 0

    def Swap(self,swp,dir = 0):
        if dir:
            dirmap = {"w":-4,"s":4,"a":-1,"d":1}
            swp = self.ZIndex()+dirmap[swp.lower()]
        if swp in self.ValidMoves():
            one = swp
            two = self.ZIndex()
            self[one],self[two] = self[two],self[one]

    def ValidMoves(self, ind = 1):
        Valids = []
        sel = self.ZIndex()

        match (sel)%4:
            case 1:
                # Left Edge
                Valids.append(1+sel)
            case 0:
                # Right Edge
                Valids.append(-1+sel)
            case _:
                # Middle Horizontal
                Valids.append(-1+sel)
                Valids.append(1+sel)

        match (sel-1)//4:  

            case 0:
                # Top Edge
                Valids.append(4+sel)
            case 3:
                # Bottom Edge
                Valids.append(sel-4)
            case _:
                # Vertical Middle
                Valids.append(-4+sel)               
                Valids.append(4+sel)

        if ind:
            return Valids   
        else:
            VMoves = []
            for i in Valids:
                VMoves.append(self[i])
            return VMoves

    def DisplayBoard(self):
        Blank = " "
        Seperator = "|"
        for i in range(self.height):
            for ii in range(self.width):
                char = str(self[(i*4)+(ii+1)])

                if char == "0": char = " " 
                
                print( Blank*(2-len(char)) + char + Seperator   ,end="" )
                if ii == 3:
                    print("\n",end="")

        print()
        
        # print(self.PlayBoard[0:4], "\n",
        #     self.PlayBoard[4:8], "\n",
        #     self.PlayBoard[8:12], "\n",
        #     self.PlayBoard[12:16])

def Playgame():
    board = BlockPusher(
        [
            
        1,2,3,4,
        5,6,7,8,
        9,10,11,12,
        13,15,14,0

        ])

    board.DisplayBoard()
    while board.HasWon() == 0:
        print(board.ValidMoves())
        t = input("Move ")
        try:
            t= int(t)
        except:
            for tt in t:
                board.Swap(tt,1)
        finally:
            board.Swap(t)

        board.DisplayBoard()

    print("Victory")

Playgame()



# def Brute(iter):
#     import random
#     tested = 0
#     vic  = 0
#     Bruted_Board = BlockPusher([
            
#         1,2,3,0,
#         5,6,7,4,
#         9,10,11,8,
#         13,14,15,12

#         ])

    
#     for i in range(iter):
#         Bruted_Board.Swap(random.choice(Bruted_Board.ValidMoves()))
#         if vic == 0:
#             print()
#             Bruted_Board.DisplayBoard()
#             tested += 1

        
#         if Bruted_Board.HasWon():
#             vic = 1
#             print("victory")
#             print("tested:",tested)
#             break


#     print("done")

#Brute(3)
