class Game:
    def __init__(self):
        self.grid = []
        for y in range(3):
            self.grid.append([])
            for _ in range(3):
                self.grid[y].append("?")

        self.turn = "O"

    def play(self, pos, value):
        x = (pos-1) % 3
        y = (pos-1) // 3
        if (self.grid[y][x] == "?"):
            self.grid[y][x] = value
            
    def unplay(self, pos):
        x = (pos-1) % 3
        y = (pos-1) // 3
        self.grid[y][x] = "?"

    def checkWinner(self, turn):
        for y in range(3):
            if(all(x == turn for x in self.grid[y])): 
                return True
        
        for x in range(3):
            check = True
            for y in range(3):
                if(not self.grid[y][x] == turn): check = False
            if(check):
                 return True
        
        if(all(self.grid[x][x] == turn for x in range(3))): 
                return True
        if(all(self.grid[x][2-x] == turn for x in range(3))): 
                return True

    def possibleMoves(self):
        moves = []
        i = 0
        for y in range(3):
            for x in range(3):
                i += 1 
                if self.grid[y][x] == "?":
                    moves.append(i)
        return moves
    

    def evaluateBoard(self):
        if (game.checkWinner("O")):
            return 20
        elif(game.checkWinner("X")):
            return -20
        else:
            return 0

    def printGame(self):
        for y in self.grid:
            for x in y:
                print(x, end = " ")
            print(" ")
        
    def playGame(self):
        self.printGame()
        win = False
        while(not win):
            if (len(game.possibleMoves()) == 0):
                print("Empate")
                break
            self.turn = "X" if self.turn == "O" else "O"
            if (self.turn == 'X'):
                pos = input("Posição: ")
                self.play(int(pos), self.turn)
                win = self.checkWinner(self.turn)
                self.printGame()
            else:
                pos = findBestMove(self, False)
                print("Posição: " + str(pos))
                self.play(pos, self.turn)
                win = self.checkWinner(self.turn)
                self.printGame()
        if(win):
            print("Victory: " + str(self.turn))



def miniMax(curDepth, maxTurn, game):
    
    score = game.evaluateBoard()
    if (score == 20):
        return score 

    if (score == -20):
        return score 

    if(len(game.possibleMoves()) == 0):
        return 0
    
    if(maxTurn):
        bestVal = float('-inf')
        moves = game.possibleMoves()
        for m in moves:
            game.play(m, 'O')
            value = miniMax(curDepth+1, not maxTurn, game)
            bestVal = max(bestVal, value)
            game.unplay(m)
        return bestVal
    else:
        bestVal = float('+inf')
        moves = game.possibleMoves()
        for m in moves:
            game.play(m, 'X')
            value = miniMax(curDepth+1, not maxTurn, game)
            bestVal = min(bestVal, value)
            game.unplay(m)
        return bestVal

def findBestMove(game, maxTurn):
    moves = game.possibleMoves()
    bestValue = float('-inf')
    for m in moves:
        game.play(m, 'O')
        value = miniMax(0, maxTurn, game)
        if (value > bestValue):
            bestValue = value
            bestMove = m
        game.unplay(m)
    return bestMove 


        
                    

        

game = Game()
game.playGame()