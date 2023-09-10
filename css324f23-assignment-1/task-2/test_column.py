goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
board = (7, 2, 4, 5, 0, 6, 8, 3, 1)
res = 0
# The for loop counts the number of tiles out of their target column
for idx in range(9):
  if (goal[idx]-1)%3+1 != (board[idx]-1)%3+1:
    print(board[idx],'is in wrong column')
    res += 1
print('res:',res,"")