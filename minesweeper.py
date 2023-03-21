import random
import math
import re


class board:
    def __init__(self,dim,num_bombs):
        self.dim=dim
        self.boared = [[' ' for _ in range(9)] for _ in range(9)]
        self.num_bombs = num_bombs
        self.dug = set()

    # let's what the board looks like
    def create_board(self):


       while self.num_bombs > 0:
           val = random.randint(0,self.dim**2 -1)
           row = val//self.dim
           col = val%self.dim

           if self.boared[row][col] != '*':
               self.boared[row][col] = '*'
               self.num_bombs -= 1

    def dig(self,row,col):

        # there are three values 1. there is a boamb 2. there is a boamb in nebor squres 3.no  bomb in nebhor squres
        if self.boared[row][col] == '*':
            return False
        if self.value_calculator(row,col) > 0:
            self.dug.add((row,col))
            return True
        else:
            self.dug.add((row, col))
            for x in range(max(0, row - 1), min(self.dim-1, row + 1)+1):
                for y in range(max(0, col - 1), min(self.dim-1, col + 1)+1):

                    if (x, y) == (row, col):
                        continue
                    if not((x,y) in self.dug):
                        self.dug.add((x,y))
                        self.dig(x,y)
        return True

    

    def value_calculator(self,row,col):
        # here we calculate how many squres around our squre have bombs
        count = 0
        for x in range(max(0,row-1),min(self.dim-1,row+1)+1):
            for y in range(max(0,col-1),min(self.dim-1,col+1)+1):
                if (x,y) == (row,col):
                    continue
                if self.boared[x][y] == '*':
                    count += 1

        return count

    def show_time(self):

        view_board= [[' ' for _ in range(self.dim)] for _ in range(self.dim)]
        for x in self.dug:
            row,col = x
            view_board[row][col] = str(self.value_calculator(row,col))

        for rows in view_board:
            print('|' + '|'.join(rows)+'|')




    def controll(self):
        
        row, col = 0,0
        safe = True
        self.create_board()
        while len(self.dug) < (self.dim)**2 - self.num_bombs:
            value = input('enter a row and column').split()
            row,col = int(value[0].strip()),int(value[-1].strip())

            if not self.dig(row,col):
                safe = False
                break

            self.show_time()


        if safe:
            print('you have succesfully completed the game')
        else:
            print('sorry you have failed')













    # let's plant some bombs




b = board(9,20)
b.controll()
