x = [
    [1,2,3],
    [4,6,7],
    [1,6,4]]

y = [
    [3,2,4],
    [2,4,5],
    [7,5,5]]
result = [[0,0,0],
          [0,0,0],
          [0,0,0]]
for i in range (len(x)):
   for j in range (len(x[0])):
       result[i][j] = x[i][j] + y[i][j]
for r in result:
    print(r)
