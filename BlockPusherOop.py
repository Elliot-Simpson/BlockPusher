class BlockPusher:

    def __setitem__(self,key,value):
        self.PlayBoard[key-1] = value
    
    def __getitem__(self,key):
        return self.PlayBoard[key-1]

    def __init__(self,defboard = None,wid=4,hei=4,winboard=None):

        self.width = wid
        self.height = hei

        def makeboard():
            t = [i for i in range(1,self.width*self.height)]
            t.append(0)
            return t


        if winboard == None:
            t = makeboard()

            self.vicboard = t
            del t
        else:
            self.vicboard = winboard


        t = makeboard() 
        self.PlayBoard = t


        if defboard[0:2] == "-s":

            import random
            for i in range(int(defboard[3:])):                                               
                self.Swap(random.choice(self.ValidMoves()))

#       elif defboard == "-r":
#           import random
#           c1 = random.choice(t)
#           c2 = c1
#           while c2 == c1:
#               c2 = random.choice(t)
#           print(c1)
#           print(c2)
#           self.PlayBoard = t
#           self.PlayBoard[c1],self.PlayBoard[c2] = self.PlayBoard[c2],self.PlayBoard[c1]

        else:
            self.PlayBoard = defboard




    def ZIndex(self):
        return self.PlayBoard.index(0) +1 

    def HasWon(self):
        if self.vicboard == self.PlayBoard:
            return 1
        else:
            return 0

    def Swap(self,swp,dir = 0):
        if dir:
            dirmap = {"w":self.width*-1,"s":self.width,"a":-1,"d":1}
            try:
                swp = self.ZIndex()+dirmap[swp.lower()]
            except:
                pass
        if swp in self.ValidMoves():
            one = swp
            two = self.ZIndex()
            self[one],self[two] = self[two],self[one]

    def ValidMoves(self, ind = 1):
        Valids = []
        sel = self.ZIndex()
        self.realheight = self.height - 1
        match (sel)%self.width:
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

        match (sel-1)//self.width:  

            case 0:
                # Top Edge
                Valids.append(self.width+sel)
            case self.realheight:
                # Bottom Edge
                Valids.append(sel-self.width)
            case _:
                # Vertical Middle
                Valids.append(sel-self.width)               
                Valids.append(self.width+sel)

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
                char = str(self[(i*self.width)+(ii+1)])
                maxl = len(str(self.width*self.height))
                if char == "0": char = " " 
                
                print( Blank*(maxl-len(char)) + char + Seperator   ,end="" )
                if ii == self.width-1:
                    print("\n",end="")

        print()



def Widegame():
    board = BlockPusher(
                        wid=5,hei=5,
                        defboard="-s:10000"
                        )
    

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

Widegame()

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
