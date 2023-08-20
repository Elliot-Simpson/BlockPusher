class BlockPusher:

    def __setitem__(self,key,value):
        self.PlayBoard[value-1] = value
    
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

    def HasWon(self):
        if self.gameboard == self.PlayBoard:
            return 1
        else:
            return 0

    def Swap(self,swp):

        if swp in self.ValidMoves():
            one = swp - 1
            two = self.PlayBoard.index(0)
            self.PlayBoard[one],self.PlayBoard[two] = self.PlayBoard[two],self.PlayBoard[one]
        # else:
        #     print("nope",swp,self.PlayBoard.index(0))
        # sel = sel - 1
        # match (sel+1)%4:
        #     case 1:
        #         # print("ledge")
        #         self.CheckZero(1,sel)

        #     case 0:
        #         # print("redge")
        #         self.CheckZero(-1,sel)

        #     case _:
        #         # print("h middle")
        #         self.CheckZero(-1,sel)
        #         self.CheckZero(1,sel)

        # match (sel-1)//4+1:  

        #     case 0:
        #         # print("top")
        #         self.CheckZero(4,sel)
        #     case 4:
        #         # print("bottom")
        #         self.CheckZero(-4,sel)
        #     case _:
        #         # print("v middle")
        #         self.CheckZero(-4,sel)               
        #         self.CheckZero(4,sel)

    def ValidMoves(self, pure = 0):

        Valids = []
        sel = self.PlayBoard.index(0) + 1
        # print("sel",sel)
        match (sel)%4:
            case 1:
                # print("ledge")
                Valids.append(1+sel)
            case 0:
                # print("redge")
                Valids.append(-1+sel)
            case _:
                # print("medge")
                Valids.append(-1+sel)
                Valids.append(1+sel)

        match (sel-1)//4:  

            case 0:
                # print("top")
                Valids.append(4+sel)
            case 3:
                # print("bottom")
                Valids.append(sel-4)
            case _:
                # print("middle")
                Valids.append(-4+sel)               
                Valids.append(4+sel)
        if pure == 0:
            return Valids   
        else:
            VMoves = []
            for i in Valids:
                VMoves.append(self.PlayBoard[i-1])
            return VMoves

    def DisplayBoard(self):
        print(self.PlayBoard[0:4], "\n",
            self.PlayBoard[4:8], "\n",
            self.PlayBoard[8:12], "\n",
            self.PlayBoard[12:16])



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
        t = int(input("Move "))
        board.Swap(t)
        board.DisplayBoard()

    print("Victory")

def Brute(iter):
    import random
    tested = 0
    vic  = 0
    Bruted_Board = BlockPusher([
            
        1,2,3,0,
        5,6,7,4,
        9,10,11,8,
        13,14,15,12

        ])

    
    for i in range(iter):
        Bruted_Board.Swap(random.choice(Bruted_Board.ValidMoves()))
        if vic == 0:
            print()
            Bruted_Board.DisplayBoard()
            tested += 1

        
        if Bruted_Board.HasWon():
            vic = 1
            print("victory")
            print("tested:",tested)
            break


    print("done")
    

Brute(3)

#Playgame()


# threads = []

# for i in range(12):
# 	print('registering thread')
# 	threads.append(Thread(target=Brute, args=([20000000000000])))

# for thread in threads:
# 	thread.start()

# for thread in threads:
# 	thread.join()



