goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
board = (7, 2, 4, 5, 0, 6, 8, 3, 1)
res = 0
# The for loop counts the number of tiles out of their target row
for idx in range(9):
  if board[idx] != 0:
    print('Checking if',board[idx],'is in',goal[(idx//3)*3: (idx//3)*3+3])
    if board[idx] not in goal[(idx//3)*3: (idx//3)*3+3]:
      print(board[idx],'is in wrong row')
      res += 1
print('res:',res)