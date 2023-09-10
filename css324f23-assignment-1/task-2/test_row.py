import eight_puzzle as problem
import math

goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
board = (7, 2, 4, 5, 0, 6, 8, 3, 1)
res = 0
# The for loop counts the number of tiles out of their target row
for idx in range(9):
  if math.ceil(goal[idx]/3) != math.ceil(board[idx]/3):
    print(board[idx],'is in wrong row')
    res += 1
print('res:',res,"")