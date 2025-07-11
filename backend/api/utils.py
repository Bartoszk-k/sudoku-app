import copy
import random

def generate_Sudoku():

    class Sudoku:

        def __init__(self):
            self.board = [[0]*9 for _ in range(9)]
            self.hidenboard = [[0]*9 for _ in range(9)]

        """
        def start(self):
            self.fill_board()
            self.show(self.board)
            self.hiding()

            while not self.gameComplite():
                i =  int(input("podaj numer wiersza: "))
                j =  int(input("podaj numer columny: "))
                number =  int(input("podaj liczbe: "))
                if number != self.board[i][j]:
                    #print("zla liczba")
                    continue
                elif i >-1 and i < 9 and j>-1 and j<9:
                    self.hidenboard[i][j] = number
                    #print("poprawna liczba")
                else:
                    continue
                    #print("bledne dane")
                self.show(self.hidenboard)
            print("Brawo! Udało Ci sięrozwiązać sudoku")
        """

        def compatible_in_column(self,j, add, board):
            for rows in board:
                if add == rows[j]:
                    return False
            return True

        def gameComplite(self):
            if self.board!=self.hidenboard:
                return False
            return True

        def compatible_in_row(self,i, add, board):
            return False if add in board[i] else True

        def compatible_in_box(self,i, j, add, board):
            indexes = [[0, 1, 2], [0, 1, 2], [0, 1, 2], [3, 4, 5], [3, 4, 5], [3, 4, 5], [6, 7, 8], [6, 7, 8], [6, 7, 8]]
            for rows in indexes[i]:
                for cols in indexes[j]:
                    if add == board[rows][cols]:
                        return False
            return True

        def fill_board(self, i=0, j=0):
            if i == 9:
                return True  # Board successfully filled

            next_i, next_j = (i, j + 1) if j < 8 else (i + 1, 0)

            numbers = self.numbers(i, j)
            random.shuffle(numbers)

            for number in numbers:
                self.board[i][j] = number
                if self.fill_board(next_i, next_j):
                    return True
                self.board[i][j] = 0  # Backtrack

            return False  # No valid number worked






        def numbers(self,i,j):
            numbers = {1,2,3,4,5,6,7,8,9}

        # removing duplicates from row
            row = {l for l in self.board[i]}
            row.remove(0) if 0 in row else row
            numbers -= row
       #     print(f'row {row}')
        #removing dupllicates from column
            col = set()
            for rows in self.board:
                col.add(rows[j])
            col.remove(0) if 0 in col else col
            numbers -= col
        #    print(f'col {col}')
        #removing duplicates from box
            box = set()
            indexes = [[0,1,2],[0,1,2],[0,1,2],[3,4,5],[3,4,5],[3,4,5],[6,7,8],[6,7,8],[6,7,8]]
            for rows in indexes[i]:
                for cols in indexes[j]:
                    box.add(self.board[rows][cols])

            box.remove(0) if 0 in box else box
            numbers -= box
          #  print(f'zbior liczb {list(numbers)}' )
            return list(numbers)


        """
        def show(self,board):
            def zeroToSpace(ch):
                if ch == 0:
                    return "\u00A0"
                return f'{ch}'
            print("    0 1 2   3 4 5   6 7 8 \n")
            for i in range(9):
                #print(f'{i}   ',end="")
                for j  in range(9):
                    if j%3==0 and j != 0:
                       print("| "+zeroToSpace(board[i][j])+" ",end="")
                    else:
                        print(zeroToSpace(board[i][j])+" ",end="")
                #print("")
                if i==2 or i==5:
                    print("    ---------------------")
        """
        def hiding(self):
            board = copy.deepcopy(self.board)
            attemps = 0
            while attemps < 100:
                random_i = random.randint(0,8)
                random_j = random.randint(0,8)
                if board[random_i][random_j]!=0:
                    board[random_i][random_j] = 0
                    if self.count_solutions(copy.deepcopy(board)):
                        board[random_i][random_j] = self.board[random_i][random_j]
                attemps +=1
            self.hidenboard = board

        def count_solutions(self,board):
            def solve(b):
                count = 0
                for i in range(9):
                    for j in range(9):
                        if b[i][j] == 0:
                            for n in range(1,10):
                                if self.compatible_in_row(j,n,b) and self.compatible_in_row(i,n,b) and self.compatible_in_box(i,j,n,b):
                                    b[i][j]=n
                                    solve(b)
                                return
                count+=1
                if count >1:
                    return


    sudoku1 = Sudoku()
    sudoku1.fill_board()
    sudoku1.hiding()
    return {"completed":sudoku1.board,
            "board": sudoku1.hidenboard}

print(generate_Sudoku())


