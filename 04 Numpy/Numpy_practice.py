#Numpy: Numpy stands for numeric python.
#import numpy as np
#numbers = np.array([10,20,30,40,50])
#print(numbers)
#print(type(numbers))
#result = numbers * 2
#print(result)

#import numpy as np
#data = np.array([
#    [10,20,30],
#    [40,50,60],
#    [70,80,90]
#])
#print(data)
#print(type(data))
#result = data * 2
#print(result)
#print(data[1])
#print(data[:,1])
#print(data + 10)


#Array properties:
#import numpy as np
#X = np.array([
#    [1.5, 2.5, 3.5, 4.5],
#    [5.5, 6.5, 7.5, 8.5],
#    [9.5, 10.5, 11.5, 12.5]
#])

#print(X.shape)
#print(X.ndim)
#print(X.size)
#print(X.dtype)

#import numpy as np
#data = np.array([
#    [[1,2],[3,4],[5,6]],
#    [[7,8],[9,10],[11,12]]
#])
#print("shape:",data.shape)
#print("ndim :",data.ndim)
#print("size :",data.size)
#print("type :",data.dtype)
#print(data[0])
#print(data[:,1])
#print(data[1,2,0])
#reshaped = data.reshape(3,4)
#print(reshaped)

#Arrey Creation:
#import numpy as np
#array = np.zeros((3,4))
#print(array)
#print(array.shape)
#print(array.dtype)
#print("_____new__")
#array = np.ones((2,5))
#print(array)
#print(array.shape)
#print(array.dtype)
#print("----New----")
#array = np.full((4,4),7)
#print(array)
#print(array.shape)
#print(array.dtype)
#print("------New____")
#array = np.arange(2,20,2)
#print(array)
#print(array.shape)
#print(array.dtype)
#array = np.linspace(0,1,6)
#print(array)
#print(array.shape)
#print(array.dtype)
#array = np.eye(5)
#print(array)
#print(array.shape)
#print(array.dtype)

#import numpy as np
#data = np.arange(1,49).reshape(4,3,4)
#print(data)
#print(data.shape)
#print(data.ndim)
#print(data.dtype)
#print(data[1])
#print(data[:,-1,:])
#print(data[:,:,2])
#print(data[3,1,1])
#values = data[(data >= 20) & (data <= 35)]
#print(values)
#new_data = values.reshape(4,4)
#print(new_data)
#print(data.sum())
#print(data.max())
#print(data.min())

#import numpy as np
#x = np.arange(1,25).reshape(6,4)
#print(x)
#print(x.shape)
#print(x.ndim)
#print(x.size)
#print(x.dtype)
#print(x[:,0])
#print(x[-2],x[-1])
#print(x[:,1],x[:,2])
#print(x + 10)
#print(x * 2)
#print(x.mean())
#print(x.max())
#new = x[x>15]
#print(new)
#print(x.reshape(3,8))

#import numpy as np
#print(np.random.rand(3,4))

#import numpy as np
#x = np.arange(10,31).reshape(3,7)
#print(x)
#print(x[0])
#print(x[-1])
#print(x[:,1])
#print(x[:,-1])
#print(x[-2:])
#print(x[:,:3])
##print(x[:,-3:])
#print("NEw")
#print(x[-1,-2])
#print(x[0,::2])
#print(x[1:3,2:6])

#Reshapeing:
#import numpy as np
#data = np.arange(1,13).reshape(3,4)
#print(data)
#print(data.reshape(2,6))
#print(data.reshape(4,3))
#print(data.flatten())
#print(data.ravel())
#result = data.flatten()
#result[0] = 999
#print(result)
#rav = data.ravel()
#rav[0] = 999
#print(rav)

#Array Operations:
#import numpy as np
#a = np.array([10,20,30,40,50])
#b = np.array([2,4,5,8,10])
#print(a + b)
#print(a - b)
#print(a * b)
#print( a / b)
#print(a ** 2)
#print(a > 25)
#print(a <= 30)
#print(a + 10)
#print(b * 3)
#print(a == 5*b)
#result = a *2 - b
#print(result ** 2)

#BRODCASTING:scaler different aray shape and the two rules.

#Aggrigation & Statistics.
#import numpy as np
#x = np.array([12,5,27,9,34,18,3,25])
#print(x.sum())
#print(x.mean())
#print(np.median(x))
#print(x.min())
#print(x.max())
#print(x.std())
#print(x.var())
#print(x.argmin())
#print(x.argmax())
#minimum = x.min()
#index = x.argmin()
#print(minimum)
#print(index)
#maximum = x.max()
#index_max = x.argmax()
#print(maximum)
#print(index_max)

#data = np.arange(10,101,10)
#print(data)
#print(data.sum())
#print(data.mean())
#print(np.median(data))
#minimum = data.min()
#index = data.argmin()
#print(minimum)
#print(index)
#maximum = data.max()
#max_index = data.argmax()
#print(maximum)
#print(max_index)
#print(data.var())
#print(data.std())


#AXIS: axis = 0 works down the columns and axis=1 works across the rows.
#import numpy as np
#x = np.array([
#    [10,20,30,40,],
#    [5,15,25,35],
#    [2,12,22,32]
#])
#print(x.sum(axis=0))
#print(x.sum(axis=1))
#print(x.mean(axis=0))
#print(x.mean(axis=1))
#print(x.max(axis=0))
#print(x.min(axis=1))
#print(x.std(axis=0))
#print(x.var(axis=1))
#print(x.argmax(axis=0))
#print(x.argmin(axis=1))


##print("------New-------")
#data = np.arange(1,25).reshape(4,6)
#print(data)
#print(data.sum(axis=0))
#print(data.sum(axis=1))
#print(data.mean(axis=0))
#print(data.max(axis=1))
#print(data.argmax(axis=1))
#rint(data.argmin(axis=0))

#BOOLIAN MASKING

#import numpy as np
#x = np.array([5,12,18,25,31,42,50,63,70,85])
#print(x>30)
#print(x[x>30])
#print(x[x<25])
#print(x[x>=50])
#print(x[x !=25] )
#print([(x>20) & (x<20)])
#print([(x<20) | (x>20)])
#print(np.sum(x>40))
#print(np.where(x>=40,1,0))
#data = np.array([
#    [10, 25, 40, 55],
#    [15, 30, 45, 60],
#    [20, 35, 50, 65]
#])
#print(data>40)
#print(data[data>40])
#print([(data>25) & (data<60)])
#print(np.where(data>40,999,data))
#print(np.where(data>50))

#import numpy as np

#x = np.array([4, 11, 18, 23, 29, 35, 42, 51, 64, 78, 85, 93])
#print(x>40)
#print(x[x<=29])
#print(x[(x>20) & (x<70)])
#print(x[(x<20) | (x>80)])
#print(np.where([(x>30) | (x<80)]))
#print(x[x != 51])
#print(np.sum(25< x >80))
#print(np.where(x>=50,100,0))
#print(np.where(x>60,999,x))
#print(np.where(x>70))

#data = np.array([
#    [10, 22, 35, 48],
#    [15, 27, 40, 55],
#    [18, 33, 45, 62],
#    [25, 38, 51, 70]
#])
#print(data[data>40])
#print(data[(data>25) & (data<60)])
#print(np.where(data>50,0, data))

#Numpy Mathematical functions:
#import numpy as np
#x = np.array([4,9,16,25,36])
#print(np.sqrt(x))

#x = np.array([0,1,2,3])
#print(np.exp(x))

#x = np.array([1,np.e,np.e**2,np.e**3])
#print(np.log(x))

#x = np.array([-25,-10,-3,0,4,15])
#print(np.abs(x))

#x = np.array([2.3456,4.6789,8.9123,10.5555])
#print(np.round(x,2))

#x = np.array([0,np.pi/2,np.pi])
#print(np.sin(x))

#x = np.array([0,np.pi/2,np.pi])
#print(np.cos(x))

#x = np.array([0,np.pi/4,np.pi/2])
#print(np.tan(x))

#x = np.array([-4,9,-16,25,-36])
#result = np.abs(x)
#print(np.sqrt(result))

#x = np.array([-2.456,4.789,-9.123,16.555])
#print(np.round(np.sqrt(np.abs(x)),2))


#import numpy as np

#x = np.array([
#    [-16.25, -4.5, 0, 2.25],
#    [9.75, -25.5, 36.0, 49.25],
#    [-64.5, 81.75, 100.0, -121.25]
#])

#result = np.round(np.exp(np.log(np.sqrt(np.abs(x)))),2)
#print(result)
#print(np.sin(result))
#print(np.cos(result))
#print(np.tan(result))

#result = (np.abs(x),
#          np.sqrt(np.abs(x)),
#          np.log(np.sqrt(np.abs(x))),
#          np.exp(np.log(np.sqrt(np.abs(x)))),
#          np.round(np.exp(np.log(np.sqrt(np.abs(x)))),2)
#          )
#print(result)


#Linear Algebra:
#import numpy as np


#a = np.array([2,4,6])
#b = np.array([1,3,5])
#print(np.dot(a,b))

#a = np.array([2,3,4])
#b = np.array([5,6,7])
#print(a*b)
#print(a@b)

#A = np.array([
#    [1, 2],
#    [3, 4]
#])

#B = np.array([
#    [5, 6],
#   [7, 8]
#])
#print(A + B)
#print(A @ B)

#A = np.array([
#    [1, 2, 3],
#    [4, 5, 6]
#])
#print(A.shape)
#rint(A.T.shape)
#print(A.T)

#A = np.array([
#    [1, 2],
#    [3, 4]
#])
#inverse = np.linalg.inv(A)
#print(inverse)
#identity_matrix = np.eye(2)
#print(identity_matrix)
#print(A @ inverse)

#A = np.array([
#    [1, 2, 3],
#    [4, 5, 6]
#])

#B = np.array([
#    [2, 1],
#    [3, 2],
#    [4, 3]
#])
#print(A.shape)
#print(B.shape)
#print(A @ B)

#import numpy as np

#X = np.array([
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9],
#    [10, 11, 12]
#])
#W = np.array([
#    [1, 2],
#    [3, 4],
#    [5, 6]
#])
#print(np.dot(X,W))
#transpose1 = X.T
#transpose2 = W.T
#print(transpose1 @ transpose2)

#import numpy as np
#A = np.array([
#    [3,2],
#   [1,4]
#])
#solution = np.linalg.det(A)
#print(solution)

#A = np.array([
#    [5,1],
#    [2,3]
#])
#sol = np.linalg.det(A)
#print(sol)

#Y = np.array([
#    [2, 1, 3],
#    [0, 4, 5],
#    [1, 2, 1]
#])
#print(np.linalg.det(Y))


#import numpy as np

#A = np.array([
#    [2, 1, 3],
#    [4, 2, 6],
#    [1, 0, 2]
#])

#B = np.array([
#    [1, 2, 0],
#    [3, 1, 4],
#    [2, 0, 1]
#])

#V = np.array([2, 3, 1])

#print(A.T.shape)
#print(A + B)
#print(A - B)
#rint(A * B)
#print(A @ B)
#print(B @ A)
#print("-----New-----")
#print(A @ V)

#print(B @ V)
#print(V @ V)
#print(A.T @ V)
#print(A.T)
#print(np.linalg.det(A))

#A = np.array([
#    [2,1,3],
#    [4,2,6],
#    [1,0,2]
#])
#b = np.array([10,20,5])

#sol = np.linalg.solve(A,b)
#print(sol)

#Random Numbers
#import numpy as np
#print(np.random.random())
#print(np.random.random(8))
#rint(np.random.random((2,5)))
#print(np.random.randint(10,50))
#print(np.random.randint(1,7,size=15))

#print(np.random.randint(1,7,size=5))
#print(np.random.randint(1,49,size=6))
#fruits = ("Apple","orange","kiwi","Banana","Pineapple","watermelon","grapes")
#print(np.random.choice(fruits))
#print(np.random.choice(fruits,3,replace=False))
#players = (["Aman","Rishabh","Moni","Pertyush","Aryan","pawan","Manish"])
#np.random.shuffle(players)
#print(players)

#print(np.random.randint(1,50,size=5))
#np.random.seed(42)
#print(np.random.randint(1,50,size=5))
#np.random.seed(50)
#print(np.random.randint(1,50,5))
#np.random.seed(99)
#print(np.random.random((2,3)))
#array = [1,2,3,4,5,6,7,8,9]
#np.random.shuffle(array)
#print("after shuffle :",array)
#new = np.random.permutation(array)
#print("permutation",new)
#print("Original: ",array)

#Combining Arrays:= h.stack v.stack stack and concatenate.
#import numpy as np
#a = [1,2,3]
#b = [4,5,6]
#print(np.concatenate((a,b)))

#a = [1,2]
#b = [3,4]
#c = [5,6]
#print(np.concatenate((a,b,c)))
#print(np.vstack((a,b,c)))
#print(np.hstack((a,b,c)))


#a = np.array([[1,2],[3,4]])
#b = np.array([[5,6],[7,8]])

#print(np.vstack((a,b)))
#print(np.hstack((a,b)))

#Numpy for machine learning:
#import numpy as np
#x = np.array([[2,56],
#            [3,78],
#            [6,90],
#            [7,98],
#            [8,99] ])
#print(x)
#print(x.shape)
#print(x.ndim)
#print(x.shape[0])
#print(x.shape[1])
#y = np.array([1,0,0,1,1])
#print(y)
#print(y.shape)
#print(np.sum(y==1))
#print(np.sum(y==0))

#X = np.array([
#    [2, 60],
#    [4, 70],
#    [6, 80],
#    [8, 90]
#])
#print(np.mean(X,axis=0))
#print(np.max(X,axis=0))
#print(np.min(X,axis=0))
#print(np.mean(X,axis=1))
#print(np.max(X,axis=1))


#import numpy as np
#x = np.array([10,20,30,40,50])

#new = (x-x.min()) / (x.max() - x.min())
#print(new)

#z = (x - x.mean()) / (x.std())
#print(z)
#print(z.mean())
#print(z.std())

#X = np.array([
#    [20, 30000],
#    [25, 40000],
#    [30, 50000],
#    [35, 60000],
#    [40, 70000]
#])
#stand_mean = X.mean(axis=0)
#stand_std = X.std(axis=0)
#new_x = (X -stand_mean)/ stand_std
#print(new_x)
#print(new_x.mean(axis=0))
#print(new_x.std(axis=0))

#x = np.array([10,20,30,40,50])
#print(x *3)

#X = np.array([
#    [10, 20],
#    [20, 30],
#    [30, 40]
#])

#print(X + 5)
#print(X * 2)
#print(X **2)
#print(np.sqrt(X))


#import numpy as np
#A = np.array([2,3])
#B = np.array([5,7])
#distance = np.linalg.norm(A - B)
#print(distance)

#points = np.array([
#    [1, 2],
#    [5, 5],
#    [2, 1],
#    [10, 10]
#])

#query = np.array([2, 2])
#result = []
#for point in points:
#    distance =np.linalg.norm(query - point)
#    result.append(distance)
#print(result)
#print(np.argmin([result]))

#import numpy as np

#x = np.array([2, 3, 4])
#w = np.array([0.5, 1.0, 2.0])
#print(np.dot(x,w))

#x = np.array([10, 20, 30])
#w = np.array([0.2, 0.5, 0.1])
#b = 5

#print((np.dot(x,w)+b))

#X = np.array([
#    [1, 2],
#    [3, 4],
#    [5, 6]
#])

#W = np.array([
#    [0.5],
#    [1.0]
#])
#b = 2

#z = (X @ W + b)
#print(z)
#print(z.shape)

#labels = np.array([0, 2, 1, 0, 2])
#result = np.eye(3)
#print(result[labels])

#X = np.array([
#    [10, 20],
#    [30, 40],
#    [50, 60],
#    [70, 80]
#])

#y = np.array([0, 1, 1, 0])
#indices = np.random.permutation(len(X))
#x = X[indices]
#Y = y[indices]
#print(X)
#print(Y)


#y = np.array([10, 20, 30, 40])

#y_pred = np.array([12, 18, 33, 35])

#errr = ((y-y_pred)**2)
#print(np.mean(errr))

#y = np.array([10, 20, 30, 40])
#y_pred = np.array([12, 18, 33, 35])
#error = (y - y_pred)
#abs = np.abs(error)
#print(np.mean(abs))

#X = np.array([
#    [20, 30000],
#    [25, 40000],
##    [30, 50000],
#    [35, 60000],
#    [40, 70000]
#])
#result = X[:,1]>45000
#print(result)
#print(X[result])

#scores = np.array([35, 60, 45, 80, 25, 90])
#print(np.where(scores >= 50,1,0))

#Fancy Indexing: Multiple indices at once.
#import numpy as np

#X = np.array([
#    [10, 20],
#    [30, 40],
#    [50, 60],
#    [70, 80],
#    [90, 100]
#])

#print(X[[1,3,4]])
#indices = np.array([0,2,4])
#result = X[indices]
#print(result)

#X = np.array([
#    [10, 20, 30],
#    [40, 50, 60],
#    [70, 80, 90],
#    [100, 110, 120]
#])

#arr = np.array([5, 10, 15, 20, 25, 30])

#print(arr[[0,2,4]])
#print(arr[[5,3,1]])
#print(arr[[1,1,5,5]])
#print(arr[[4,3,2,1,0]])


#array = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])

#print(array[[0,2,4,6]])
#rint(array[[9,8,7]])
#print(array[[9,8,7,6,5,4,3,2,1,0]])
#print(array[[0,2,4,6,8]])
#print(array[[1,3,5,7,9]])
#print(array[[1,1,1,1]])
#print(array[[5,3,9,4,0]])
#print(array[[7,1,9,0,4,2]])

#numbers = np.array([100,200,300,400,500,600,700,800,900,1000])

#print(numbers[[-1,0,-2,1,-3,2]])
#print(numbers[[2,2,5,5,9,9]])
#print(numbers[[2,3,5,7]])
#print(numbers[[4,3,2,1,0]])
#print(numbers[[1,4,1,4,1]])
#print(numbers[[5,6,7,8,9,0,1,2,3,4]])
#print(numbers[[0,2,4,6,8]])
#print(numbers[[4,4,4,1,1,8,8]])
#print(numbers[[0,9,1,8,2,7,3,6,4,5]])
#print(numbers[[9,7,5,3,1]])

#x = np.arange(1,21)
#print(x)
#print(x[[0,1,2,3,5,8,13]])
#print(x[[19,17,15,13,11,9,7,5,3,1]])
#print(x[[0,19,1,18,3,16,4,15]])
#print(x[[0,0,5,5,10,10,15,15]])
#print(x[[1,2,3,4,5,4,3,2,1]])
#print(x[[4,9,14,19,14,9,4,9,14]])
#result = np.random.randint(1,21,8)
#print(x[result])
#print(x[[10,0,11,2,12,2,13,3,14,4]])
#print(x[[19,18,17,16,16,17,18,19]])
#print(x[[0,4,8,12,16,19,16,11,7,3]])

#Integer Array indexing:
#import numpy as np

#A = np.array([
#    [11, 12, 13, 14, 15],
#    [21, 22, 23, 24, 25],
#    [31, 32, 33, 34, 35],
#    [41, 42, 43, 44, 45],
#    [51, 52, 53, 54, 55]
#])
#row = [0,1,2,3,4]
#columns = [0,3,2,4,1]
#print(A[row,columns])

#row = [0,1,2,3,4]
#columns = [4,3,2,1,0]
#print(A[row,columns])

#row1 = [0,1,2,3,4]
#columns1 = [2,2,2,2,2]
#result1 = A[row1,columns1]
#print(result1)
#row2 = [2,2,2,2,2]
#column2 =[0,1,2,3,4]
#result2 = A[row2,column2]
#print(result2)
#result3 = np.concatenate((result1,result2))
#print(result3)


#row = [0,0,1,1,3,3,4,4]
#columns = [1,3,0,4,0,4,1,3]
#print(A[row,columns])

#row = [0,0,4,4,2]
#column = [0,4,4,0,0]
#print(A[row,column])

#row = [1,1,3,3,1,3,2]
#column = [1,1,3,3,1,3,2]
#print(A[row,column])


#row = [0,1,2,3,4,0,1,3,4]
#columns = [0,1,2,3,4,4,3,1,0]
#print(A[row,columns])

#rows = [0,2,1,4,3,2,0]
#columns = [4,1,3,0,2,4,0]
#print(A[rows,columns])

#rows1 = [0,1,2,3,4]
#columns1 = [4,1,2,3,0]
#results1 = A[rows1,columns1]
#print(results1)
#rows2 = [0,1,2,3,4]
#columns2 = [2,2,2,2,2]
#results2 = A[rows2,columns2]
#print(results2)
#final = np.concatenate((results1,results2))
#print(final)


#Multiple Row and Column selection:
#import numpy as np

#students = np.array([
#    [101, 20, 170, 65, 85],   # ID, Age, Height, Weight, Marks
#    [102, 22, 180, 75, 91],
#    [103, 19, 165, 55, 78],
#    [104, 24, 175, 70, 88],
#    [105, 21, 168, 60, 82],
#    [106, 23, 182, 80, 95]
#])

#print(students[[5,1,4,0]])

##Reverse
#rows = [3,2,1,0]
#print(students[rows])

##Duplecate Rows
#row = [2,2,4,4,5]
#print(students[row])

##Mini- batch sampling
#print(students[[5,2,0]])


#print(students[[0,1,2,1,0]])

#Feature Extraction:

#students = np.array([

#print(students[:,[2,3]])

#print(students[:,[1,2,3]])

#print(students[:,[4,3,2,1,0]])

#print(students[:,[2,2,4,4,1]])

#print(students[:,[0,4,2]])

##FAANG :-13
#rows = [5,2,0]
#columns = [2,4]

#result = np.ix_(rows, columns)
#print(students[result])


#Arbitrary Element selection:
#import numpy as np

#A = np.array([
#    [11, 12, 13, 14, 15],
#    [21, 22, 23, 24, 25],
#    [31, 32, 33, 34, 35],
#    [41, 42, 43, 44, 45],
#    [51, 52, 53, 54, 55]
#])

#rows = [1,2,2,2,3]
#columns = [2,1,2,3,2]
#print(A[rows,columns])

#row = [0,0,3,4,4,3,1]
#columns = [0,4,4,4,0,0,0]
#print(A[row,columns])

#row = [0,1,2,3,4]
#columns = [1,3,4,1,0]
#print(A[row,columns])

#r = [0,1,2,3,4]
#c = [3,1,4,2,1]
#print(A[r,c])

#A = np.array([
#    [11, 12, 13, 14, 15],
#    [21, 22, 23, 24, 25],
#    [31, 32, 33, 34, 35],
#    [41, 42, 43, 44, 45],
#    [51, 52, 53, 54, 55]
#])

#b = [0,0,2,4,4]
#c = [0,4,2,0,4]
#print(A[b,c])

#x = [0,1,2,3,4]
#y = [2,1,4,3,0]
#print(A[x,y])

#s = [0,1,2,3,4]
#t = [0,1,0,1,2]
#print(A[s,t])

#a = [0,1,2,3,4]
#b = [4,2,0,3,1]
#print(A[a,b])

#t =[1,1,2,2,3,3,4]
#y = [3,3,2,2,1,1,0]
#print(A[t,y])

#g = [0,1,2,3,4,3,2,1,0,0]
#t = [0,3,4,3,2,1,0,1,2,3]
#print(A[g,t])

#BOOLEAN + integer indexing:-
#import numpy as np

#students = np.array([
#    [101,20,170,65,85],
#    [102,22,180,75,91],
#    [103,19,165,55,78],
#    [104,24,175,70,88],
#    [105,21,168,60,82],
#    [106,23,182,80,95],
#    [107,20,172,68,76],
#    [108,22,169,72,89],
#    [109,25,185,85,97],
#    [110,21,174,66,84]
#])

#select = students[:,4]>=90
#print(students[select])

#student = students[:,1]<21
#print(students[student])

#k = students[:,4] != 84
#print(students[k])

#a = students[:,1] == 22
#print(students[a])

#print("New")
#m = students[:,4] >85
#print(students[m][:,[0,4]])

#n = students[:,1] <= 21
#print(students[n][:,[2,3]])

#t = students[:,2] > 170
#print(students[t][:,[1,2,4]])

#students = np.array([
#    [101,20,170,65,85],
#    [102,22,180,75,91],
#    [103,19,165,55,78],
#    [104,24,175,70,88],
#    [105,21,168,60,82],
#    [106,23,182,80,95],
#    [107,20,172,68,76],
#    [108,22,169,72,89],
#    [109,25,185,85,97],
#    [110,21,174,66,84]
#])

#h = students[:,2]>= 174
#print(students[h][:,[2,4]])

#w = students[:,3] == 60
#print(students[w][:,[0,1,4]])

#a = (students[:,1]>=22) & (students[:,4]>=90)
#print(students[a])

#h = (students[:,2]>170) & (students[:,3]<75)
#print(students[h])

#m = (students[:,4]>90) | (students[:,2]>=185)
#print(students[m])

#c = (students[:,1]==20) | (students[:,1] == 21)
#print(students[c])

#v = ~(students[:,4] < 85)
#print(students[v])

#s = (students[:,2]>168) & (students[:,4] > 80)
#print(students[s][:,[0,2,4]])

#j = (students[:,4] >= 88) & (students[:,1]<23)
#print(students[j][:,[0,2,4]])

#m = (students[:,2]>=175) & (students[:,3]<=80) & (students[:,1]>=22)
#print(students[m][:,[0,1,2,3]])

#me = np.mean(students[:,4])
#h = students[:,4]>me
#print(students[h][:,[0,2,4]])

#np.take() :- use to take the value from the matrices.

#import numpy as np

#students = np.array([
#    [101,20,170,65,85],
#    [102,22,180,75,91],
#    [103,19,165,55,78],
#    [104,24,175,70,88],
#    [105,21,168,60,82],
#    [106,23,182,80,95]
#])

#r = np.take(students,[0,2,5],axis=0)
#print(r[:,0])

#t = np.take(students,[2,4],axis=1)
#print(t)

#j = np.take(students,[5,1,4,0],axis=0)
#print(j)

#n = np.take(students,[-1,-2,-3,-4,-5],axis=1)
#print(n)

#m = np.take(students,[2,2,4,4,1], axis=1)
#print(m)

#A = np.array([
#    [11,12,13,14],
#    [21,22,23,24],
#    [31,32,33,34],
#    [41,42,43,44]
#])

#u = np.take(A,[0,2],axis = 0)
#print(u)

#h = np.take(A,[0,3],axis = 1)
#print(h)

#s = np.take(A,[-1,-2,0],axis = 0)
#print(s)

#x = np.array([10,20,30,40])
#print(np.take(x,[0,5,2,8] , mode="clip"))
#print(np.take(x,[0,5,6,7,8] ,mode = "wrap"))


#np.put() used for replace the values. it make the matrices flatten first
#import numpy as np
#arr = np.array([10,20,30,40,50,60,70,80])
#np.put(arr,[1,3,6],[200,400,700])
#print(arr)

#arr = np.array([10,20,30,40,50,60,70,80])
#np.put(arr,[0,2,4,7],999)
#print(arr)

#arr = np.array([10,20,30,40,50,60,70,80])
#np.put(arr,[2,2,2,5,5],[1,2,3,8,9])
#print(arr)

#arr = np.array([10,20,30,40,50,60,70,80])
#np.put(arr,[-1,-2],[500,600])
#print(arr)

#arr = np.array([10,20,30,40,50,60,70,80])
#np.put(arr,[0,-1,3,-2],[100,800,400,700])
#print(arr)


#B = np.array([
#    [11,12,13],
#    [21,22,23],
#    [31,32,33]
#])

#np.put(B,[0,1,2,3,4,5,6,7,8],[11,12,13,21,22,23,31,32,33])
#print(B)

#B = np.array([
#    [11,12,13],
#    [21,22,23],
#    [31,32,33]
#])
#np.put(B,[0,4,8],[100,200,300])
#print(B)

#B = np.array([
#    [11,12,13],
#    [21,22,23],
#    [31,32,33]
#])
#np.put(B,[1,3,4,5,7],999)
#print(B)

#C = np.array([5,10,15,20])
#np.put(C,[0,5,8],[100,200,300],mode="clip")
#print(C)

#C = np.array([5,10,15,20])
#np.put(C,[4,5,6,7],[1,2,3,4],mode="wrap")
#print(C)

#np.put_alog_axis:- helps to change the position according to the given indices.

#import numpy as np

#students = np.array([
#    [101,20,170,65,85],
#    [102,22,180,75,91],
#    [103,19,165,55,78],
#    [104,24,175,70,88],
#    [105,21,168,60,82],
#    [106,23,182,80,95]
#])
#indices = np.array([
#    [4],
#    [4],
#    [4],
#    [4],
#    [4],
#[4]
#])
#values = np.array([
#    [86],
#    [92],
#    [80],
#    [89],
#    [84],
#    [96]
#])
#np.put_along_axis(students,indices,values,axis=1)
#print(students)

#height = np.array([
#    [2],
#    [2],
#    [2],
#    [2],
#    [2],
#    [2],
#])
#change = np.array([
#    [171],
#    [181],
#    [166],
#    [176],
#    [169],
#    [183]
#])
#np.put_along_axis(students,height,change,axis=1)
#print(students)


#new = np.array([
#    [1],
#    [4],
#    [3],
#    [2],
#    [0],
#    [4]
#])

#col = np.array([
#    [25],
#    [99],
#    [58],
#    [177],
#    [999],
#    [100]
#])
#np.put_along_axis(students,new,col,axis=1)
#print(students)



#B = np.array([
#    [1,4],
#    [2,3],
#    [0,4],
#    [2,4],
#    [3,4],
#    [1,2]
#])

#c = np.array([
#    [21,90],
#    [185,77],
#    [555,81],
#    [178,95],
#    [63,85],
#    [24,184]
#])

#np.put_along_axis(students,B,c,axis=1)
#print(students)

#result = np.array([
#    [0, 0, 0, 0, 0],
#    [0, 0, 0, 0, 0],
#    [0, 0, 0, 0, 0],
#    [0, 0, 0, 0, 0],
#    [0, 0, 0, 0, 0],
#    [0, 0, 0, 0, 0]
#])

#r = students[:,4]>=85
#indices = np.full((6,1),4)
#values = r.astype(int).reshape(-1,1)
#np.put_along_axis(result,indices,values,axis=1)
#print(result)


#scores = np.array([
#    [85,90,88,92],
#    [78,80,76,81],
#    [95,94,96,97],
#    [60,65,62,68],
#    [72,75,70,73]
#])

#r = np.argmax(scores, axis=1, keepdims=True)
#np.put_along_axis(scores,r,100,axis=1)
#print(scores)

#f = np.argmin(scores,axis=1)
#h = f.reshape(-1,1)
#np.put_along_axis(scores,h,0,axis=1)
#print(scores)

#n = np.argsort(scores,axis=1,)
#np.put_along_axis(scores,n,100,axis=1)
#print(scores)


#scores = np.array([
#    [85,90,88,92],
#    [78,80,76,81],
#    [95,94,96,97],
#    [60,65,62,68],
#    [72,75,70,73]
#])
#q = np.argmax(scores,axis = 0,keepdims=True)
#np.put_along_axis(scores,q,999,axis=0)
#print(scores)

#result = np.zeros((6,4),dtype=int)
#labels = np.array([2,0,3,1,2,1]).reshape(-1,1)
#np.put_along_axis(result,labels,1,axis=1)
#print(result)

#Copy and View

#VIEW:--> it is the same variable looks at the same memory. it effects the original.

#import numpy as np

#A = np.array([
#    [11,12,13,14],
#    [21,22,23,24],
#    [31,32,33,34],
#    [41,42,43,44]
#])
#B = A.view()
#B[2,2] = 999
#print(A)
#print(B)



#c = A.copy()
#c[1,1] = 555
#print(c)
#print(A)
#print(c.base)


#B = A[1:3]
#print(B)
#print(A) # B is a copy.

#c = A[:,2:]
#print(c)
#print(A) # c is also copy.

#D = A.copy()
#print(D)
#print(A) #it is also copy. slicing always give the copy.

#rows = A[::2]
#rows[0] = 777
#print(rows)
#print(A) # it is a view cause it affects the original.

#cols =A[:,1:3]
#cols[1,1] = 500
#print(cols)

#B = A[[0,2]]
#B[1,0] = 999
#print(B)


#B = A[A>25]
#B[0] = 1000
#print(B)
#print(A) # is also copy

#B = A[[0,3],[1,2]]
#print(B)
#print(A) # also copy


#slice_rows = A[1:3]
#fancy_rows = A[[1,2]]
#slice_rows[0,0]=8900
#fancy_rows[0,0]=8000
#print(slice_rows)
#print(A)
#print(fancy_rows)
#print(A)   # slice is effect the original infect original of index also.

#import numpy as np
#X = np.arange(1,17).reshape(4,4)

#B = X.copy()
#B[1]= 999
#print(B)
#print(X)
#print(X.base)

#C =np.copy(X)
#C[:,2] = 0
#print(X)
#print(C.copy())

#train = X.copy()
#validation = np.copy(X)
#train[:,0]=0
#validation[:,1]=1
#print(train)
#print(validation)
#print(X)

#B = X.copy()
#C = B.copy()
#C[:,0] = 999
#print(B)
#print(C)
#print(X)

#B = X.copy()
#print(B.base)
#print(B.flags.owndata)

#C = X.view()
#print(C.base)
#print(C.flags.owndata)

#D = X[1:3]
#print(D.base)
#print(D.flags.owndata)

#E = X[[1,3]]
#print(E.base)
#print(E.flags.owndata)

#A = np.array([
#    [11,12,13,14],
#    [21,22,23,24],
#    [31,32,33,34],
#    [41,42,43,44]
#])
#B = A[1:3]
#print(np.shares_memory(A,B))
#C = A.copy()
#print(np.shares_memory(A,B))
#D = A[:,2:]
#print(np.shares_memory(A,D))

#B = A[[0,2]]
#print(np.shares_memory(A,B))

#n = A[A>20]
#print(np.shares_memory(A,n))

#D = A[:,1]
#print(np.shares_memory(A,D))

#print("NEw")
#A = np.arange(1,17).reshape(4,4)
#print(A)
#B = A[1:,1:]
#print(B)
#C = B.copy()
#print(C)

#D = A[:,[0,2]]
#print(D)

#E = A[::2]
#print(E)

#B[0,0] = 500
#print(B)
#C[1,1] = 600
#print(C)
#D[0,0] = 700
#print(D)
#E[1,2] = 800
#print(E)

#DataType :--19. Data types & type conversion
#import numpy as np
##INTEGER D.type:------->
#students = np.array([
#    [101,20,170,65,85],
#    [102,22,180,75,91],
#    [103,19,165,55,78],
#    [104,24,175,70,88],
#    [105,21,168,60,82],
#    [106,23,182,80,95]
#])

#A = np.array([10,20,30])
#print(A.dtype)
#B = np.array([10.5,20.8,30.1])
#print(B.dtype)
#C = np.array([True,False,True])
#print(C.dtype)
#D = np.array([1+2j,3+4j])
#print(D.dtype)
#E = np.array(["Ai","ML","DL"])
#print(E.dtype)

#v = np.array([10,20,30,40],dtype=np.int8)
#print(v.dtype)
#print(v.itemsize)

#b = np.array([10,20,30,40],dtype = np.int16)
#print(b.dtype)
#print(b.itemsize)

#h = np.array([10,20,30,40],dtype = np.int32)
#print(h.dtype)
#print(h.itemsize)

#k = np.array([10,20,30,40],dtype=np.int64)
#print(k.dtype)
#print(k.itemsize)

##FLOAT D.type:------->

#f = np.array([3.14159265,2.71828182],dtype = np.float16)
#print(f.dtype)
#print(f.itemsize)
#print(f)

#p = np.array([3.14159265,2.71828182],dtype = np.float32)
#print(p.dtype)
#print(p.itemsize)
#print(p)

#n = np.array([3.14159265,2.71828182],dtype = np.float64)
#print(n.dtype)
#print(n.itemsize)
#print(n)


#u = np.array(students,dtype = np.int16)
#print(u.dtype)
#print(u.itemsize)
#print(u)

#x = np.array(students,dtype = np.int32)
#print(x.dtype)
#print(x.itemsize)
#print(x)

#g = np.array(students,dtype = np.float64)
#print(g.dtype)
#print(g.itemsize)
#print(g)     # float use the less memory.

#pixels = np.array([0,64,128,192,255],dtype=np.uint8)
#print(pixels.dtype)
#print(pixels.itemsize)
#print(pixels.nbytes)
#pixels = np.array([0,64,128,192,255],dtype=np.int64)
#print(pixels)

#BOOlEAN :------->
#a = students[:,[4]]>= 90
#b = students[:,[1]]<= 20
#n = students[:,[2]]>=175
#d = students[:,[3]]< 70
#print(a)
#print(b)
#print(n)
#print(d)
#print(a.dtype)
#print(b.dtype)
#print(n.dtype)
#print(d.dtype)

#io=a.astype(int)
#print(io)
#print(io.dtype)

#yo = b.astype(int)
#print(yo)
#print(io.dtype)

#sx = n.astype(int)
#print(sx)
#print(sx.dtype)

#bo = n.astype(int)
#print(bo)
#print(bo.dtype)



#Complex Numbers:-------->

#Z = np.array([
#    2+3j,
#    5+1j,
#    -1+4j,
#    3-2j
#])

#print(Z.dtype)
#print(Z.real)
#print(Z.imag)
#mo = np.abs(Z)
#print(mo)

#import numpy as np

#x = np.array([
#    [ 2+3j,   5-1j,  -4+2j],
#    [ 7+0j,  -2+6j,   1-5j],
#    [-3-4j,   8+2j,   0+9j]
#])

#print(x.dtype)
#vo =x.real
#print(vo)
#print(x.imag)
#fo = vo.astype(np.float32)
#print(fo)
#print(fo.dtype)


#signal = np.array([
#    1+0j,
#    0+1j,
#    -1+0j,
#    0-1j
#])
#print(signal.dtype)
#print(np.abs(signal))
#print(signal.real)
#print(signal.imag)


# ASTYPE:-------->

#data = np.array([
#    ["101", "85.5", "1"],
#    ["102", "91.2", "0"],
#    ["103", "78.8", "1"],
#    ["104", "88.0", "0"]
#])
#v = data[:,[0]]
#nu = v.astype(np.int32)
#print(nu)
#print(nu.dtype)

#b = data[:,[1]]
#mu = b.astype(np.float32)
#print(mu)
#print(mu.dtype)

#j = data[:,[2]]
#hu = j.astype(np.bool)
#print(hu)
#print(hu.dtype)

#TYPE CONVERSION:----->
#A = np.array([0, 1, -3, 5, 10])
#vu = A.astype(np.bool)
#print(vu.dtype)

#bn = vu.astype(np.int8)
#print(bn.dtype)

#hj = bn.astype(np.float16)
#print(hj.dtype)

#A = np.array([10, 20.5, 30])
#float8
#B = np.array([True, 5, False])
#int8
#C = np.array([2.5, 1+3j])
#complex
#D = np.array([100, "AI", 50])
#string

#O = np.array([126, 127], dtype=np.int8)
#bn = O + 2
#print(bn)
#O = np.array([126, 127], dtype=np.int16)
#bn = O + 2
#print(bn)

#a = np.array([0.1])
#b = np.array([0.2])
#c = np.array([0.3])
#gh = a+ b
#print(gh)
#print(gh == c)
#print(np.isclose(gh,c)) #this comparison is used in the machine learning.

#nm = np.arange(1000000,dtype= np.int64)
#uo = np.arange(1000000,dtype= np.int16)
#print(nm.dtype)
#print(uo.dtype)
#print(nm.itemsize)
#print(uo.itemsize)
#print(nm.size)
#print(uo.size)
#print(nm.nbytes)
#print(uo.nbytes)


#NAN and INFINITY:---->
#import numpy as np

#students = np.array([
#    [101, 85.0],
#    [102, np.nan],
#    [103, 91.0],
#    [104, np.nan],
#    [105, 88.0],
#    [106, 95.0]
#])


#A = np.array([10, 20, np.nan, 40, np.nan, 60])
#print(A)
#print(A.dtype)

#marks = np.array([78,82,91,88,95], dtype=float)
#marks[[1,4]] = np.nan
#print(marks)

#vb = np.isnan(students)
#print(vb)
#print(vb.dtype)

#print(np.isnan(students).sum())
#nb = np.sum(np.isnan(students[:,1]))
#print(nb)
#po = np.sum(~np.isnan(students[:,1]))
#print(po)

#k = np.array([15, np.inf, 25, -np.inf, 35])
#print(np.isinf(k))
#print(np.sum(np.isinf(k)))

#v = np.array([10, np.inf, np.nan, 30, -np.inf, 50])
#bn = np.isfinite(v)
#print(v[bn])


#b = np.nan_to_num(students,nan = 0)
#print(b)

#n = np.nanmean(students)
#print(n)
#d = np.nan_to_num(students,nan = n)
#print(d)

#A = np.array([10, np.inf, -np.inf, np.nan, 25])
#m = np.nan_to_num(A,neginf=-999,posinf=999,nan = 0 )
#print(m)

#scores = np.array([
#    [1,85],
#    [2,np.nan],
#    [3,91],
#    [4,np.inf],
#    [5,88],
#    [6,-np.inf]
#])

#y = np.isfinite(scores[:,1])
#print((scores[y]).reshape(-1,1))


#marks = np.array([75,np.nan,80,95,np.nan,90])
#print(np.mean(marks))
#print(np.nanmean(marks))
# output is different cause in first we get nan and in second we get average it is because in second it ignores the nan.

#values = np.array([10,np.nan,30,20,np.nan,50])
#print(np.nanmedian(values))

#data = np.array([
#    [21,np.nan,170],
#    [22,75,180],
#    [np.nan,68,175],
#    [20,70,np.nan],
#    [23,72,182]
#])

#y = np.sum(np.isnan(data),axis=0)
#print(y)
#n = (np.nanmean(data,axis=0))
#print(n)
#i = np.nan_to_num(data,nan=n)
#print(i)

#sensor = np.array([
#    20.5,
#    np.nan,
#    19.8,
#    np.inf,
#    21.1,
#    -np.inf,
#    20.2
#])

#o = np.sum(np.isnan(sensor))
#print(o)
#e = np.sum(np.isinf(sensor))
#print(e)
#b = np.isfinite(sensor)
#print(sensor[b])
#print(np.nan_to_num(sensor,nan= 20,neginf = 20,posinf = 20))


#marks = np.array([
#    [85,np.nan,91],
#   [88,92,np.nan],
#    [np.nan,95,90],
#    [87,91,89]
#])

#print(np.nanmean(marks,axis=0))
#print(np.nanmedian(marks,axis=0))
#print(np.nansum(marks,axis=0))
#print(np.nanmin(marks,axis=0))
#print(np.nanmax(marks,axis=0))

#predictions = np.array([
#    0.85,
#    np.nan,
#    0.91,
#    np.inf,
#    0.77,
#    -np.inf,
#    0.66
#])
#print(np.isnan(predictions))
#print(np.isinf(predictions))
#print(np.nan_to_num(predictions,nan = 0,posinf=0,neginf=0).reshape(-1,1))
#g =(np.sum(np.isfinite(predictions)))
#print(g)
#print(np.mean(g))


#students = np.array([
#    [101,85],
#    [102,np.nan],
#    [103,91],
#    [104,np.nan],
#    [105,88],
#    [106,95],
#    [107,np.nan]
#], dtype=float)

#g = np.isnan(students[:,1])
#print(g)
#n  = np.nanmean(students[:,1])
#students[g,1]=n
#print(students)


#prices = np.array([
#    120.5,
#    np.nan,
#    118.2,
#    np.inf,
#    121.7,
#    119.9,
#    -np.inf,
#    np.nan
#])
#av = np.isfinite(prices)
#print(av)
#print(prices[av])
#sd = np.mean(prices[av])
#print(sd)
#kl = np.nan_to_num(prices,nan=sd,posinf=sd,neginf=sd)
#print(np.max(kl))
#print(np.min(kl))


#DIMENSION MANIPULATion;--___>
# EXPAND DIMENSION:----->
#A = np.array([1,2,3,4,5])
#print(np.expand_dims(A,axis = 0))
#print(np.expand_dims(A,axis=1))
#n = np.array([
#   [1,2,3,4],
#    [5,6,7,8],
#   [9,10,11,12]
#])
#print(np.expand_dims(n,axis=0))
#print(np.expand_dims(n,axis=1))
#print(np.expand_dims(n,axis=2))

#x = np.zeros((224,224,3))
#print(x)
#print(np.expand_dims(x,axis=0))

#d = np.zeros((28,28))
#print(d.shape)
#print(np.expand_dims(d,axis = 2))

#h = np.zeros((768,))
#print(h)
#print(np.expand_dims(h,axis = 0))

#g = np.array([1,2,3,4])
#print(A.shape)
#b = np.expand_dims(g,axis=0)
#result = np.expand_dims(b,axis=2)
#print(result)

#n = np.zeros((2,3,4))
#print(np.expand_dims(n,axis=0))
#print(np.expand_dims(n,axis=1))
#print(np.expand_dims(n,axis=2))
#print(np.expand_dims(n,axis=3))

#np.squeeze:------> it remove one dimension of singleton(any axis with size one).
#import numpy as np
#A = np.zeros([128,1]).reshape(1,-1)
#print(A.shape)
#B = np.squeeze(A)
#print(B.shape)

#C = np.ones([1,224,224,1])
#print(C)
#O = np.squeeze(C)
#print(O)
#print(O.shape)
#print(O.ndim)

#U = np.full((1,64,1,512),8)
#print(U)
#print(U.squeeze(axis=0))
#print(U.squeeze(axis=2))

#n = np.full((1,32,1,14,14,1),7)
#print()

#m = np.full((1,8,1,128,1,64),9)
#print(np.squeeze(m,axis=0))

#np.newaxis:-----> it increase the new axis along with the index.
#import numpy as np

#A = np.array([5, 10, 15, 20])
#P = A[np.newaxis, :]
#print(P)

#Q = A[:, np.newaxis]
#print(Q)

#R = A[np.newaxis, :, np.newaxis]
#print(R)

#B = np.array([
#    [1,2,3],
#    [4,5,6]
#])
#print("new")
#A = B[np.newaxis,:]
#print(A)
#print("new")
#C = B[:,np.newaxis,:]
#print(C)
#print("new")
#D = B[:,:,np.newaxis]
#print(D)
#print("new")
#E = B[np.newaxis,:,np.newaxis,:]
#print(E)

#x = np.array([1,2,3,4])
#y = np.array([10,20,30])
#A = x[:,np.newaxis]
#print(A)
#B = y[np.newaxis,:]
#print(y)
#c = A*B
#print(c)
#D = x[np.newaxis,:,np.newaxis]
#print(D)
#E = y[:,np.newaxis,np.newaxis]
#print(E)

#NONE IS SAME AS THE np.newaxis. adding the dimension according to the index.

#.T and np.transpose():------> both work same but transpose() is used in 3D tensors.
#import numpy as np
#A = np.array([
#    [1,2,3],
#    [4,5,6]
#])
#print(A.shape)
#print(np.transpose(A))

#m = np.arange(1,9).reshape(4,2)
#print(m)
#print(m.T)
#print(np.transpose(m))

#A = np.arange(24).reshape(2,3,4)
#print(A)
#h= np.transpose(A,(1,0,2))
#print(h)
#print(h.shape)

#Q = np.random.rand(16,8,128,64)
#print(Q.shape)
#p = np.transpose(Q,(0,2,1,3))
#print(p.shape)

#SWAPAXIS:_____> swap the axis with np.swapaxis.
#import numpy as np
#A = np.arange(60).reshape(3,4,5)
#print(A.shape)
#b = np.swapaxes(A,0,2)
#print(b.shape)

#print(b[0])

#T = np.random.rand(8,16,196,14,14,64)
#t = np.swapaxes(T,1,5)
#n = np.swapaxes(t,2,3)
#h = np.swapaxes(n,3,4)
#d = np.swapaxes(h,4,5)
#print(d.shape)

#np.atleast1d,2d,3d:------->
import numpy as np


#x = 100
#n = np.atleast_1d(x)
#print(n)
#print(n.shape)

#a = 10
#b = np.array([1,2,3,4])
#c = np.array([[5,6],[7,8]])
#print(np.atleast_1d(a))
#print(np.atleast_1d(b))
#print(np.atleast_1d(c))
#a change and the rest one are same. cause b has one dimension and the c is 2d matrix.

#inputs = [5, np.array([10,20]), np.array([[1,2],[3,4]])]
#for x in inputs:
#    result = np.atleast_1d(x)
#    print(result)
#    print(result.shape)

#scalar = 7
#vector = np.array([1,2,3])
#matrix = np.array([[1,2],[3,4]])
#print(np.atleast_2d(scalar))
##print(np.atleast_2d(vector))
#print(np.atleast_2d(matrix))


#sample = np.random.rand(128)
#n = np.atleast_2d(sample)
#print(np.shape(sample))
#print(n.shape)
#print(n[0])


#image = np.array([
#    [1,2,3],
#    [4,5,6],
#    [7,8,9]
#])

#o = np.atleast_3d(image)
#print(np.shape(image))
#print(o.shape)
#print(o[:,:,0])


#SHORTING:---->
#np.short:----->

#A = np.array([18,4,25,11,7,30])
#b =np.sort(A)
#print(b)

#A = np.array([
#    [12, 5, 9, 1],
#    [8, 15, 3, 10],
#    [20, 2, 18, 6]
#])

#print(np.sort(A,axis=1))

#T = np.array([
#    [[9,2,5],[8,1,7]],
#    [[4,6,3],[10,12,11]]
#])

#print(np.sort(T,axis=1))
#
#A = np.array([
#    [5,1,9],
#    [8,3,6]
#])

#print(np.short(A[::-1]))

#A = np.array([40,15,70,25,10])
#print(np.argsort(A))

#A = np.array([23,18,35,12,27])

#idx = np.argsort(A)

#print(A[idx])

#confidence = np.array([0.42,0.97,0.35,0.81,0.56,0.99])
#b = np.argsort(confidence)
#print(b[3::])

#X = np.random.randint(0,100,size=(8,3,224,224))
#b = np.argmax(X,axis=1)
#print(b)

#probability = np.random.rand(16,5,128,128)
#print(np.argmin(probability))

#A = np.array([14,3,9,1,20,8,5])
#n =np.partition(A,3)
#print(n)

#A = np.array([30,12,7,45,18,25,10])

#d =np.partition(A,1)
#print(d)


#salary = np.array([52,38,61,29,74,48,55,41,67])
#median = np.partition(salary,4)[4]
#print(median)

#distance = np.array([8.2,1.5,3.9,6.1,0.8,2.4,5.7,1.9])
#print(np.partition(distance,4)[:4])

#A = np.array([
#    [12,5,18,2,9],
#    [20,1,15,8,11],
#    [7,14,3,16,10]
#])

#argpartition():--------> give the indices index value of partition.

#3scores = np.array([88, 95, 73, 99, 91, 84, 97])
#n = np.argpartition(scores,-2)[-2:]
#print(n)

#X = np.array([
#    [18, 5, 22, 9, 14],
#    [7, 30, 12, 25, 10],
#    [40, 3, 15, 8, 20]
#])

#idx = np.argpartition(X, 1, axis=1)
#n = (X[np.arange(3)][:,None],idx[:,:2])
#print(n)

#np.searchsorted:---->

#prices = np.array([100,120,120,120,150,180,180,200,200,200,250])
#lest = np.searchsorted(prices, 120,side='left')
#right = np.searchsorted(prices, 120,side='right')
#count = right - lest
#print(count)

#np.unique ______>
#colors = np.array([
#    "red","blue","red","green",
#    "blue","red","green","green","blue"
#])
#value,count = np.unique(colors, return_counts=True)
#print((value,count))

#A = np.array([20,10,20,30,10,40,30,50])
#value,idx =np.unique(A,return_index = True)
#print((value,idx))

#fruits = np.array([
#    "apple","banana","apple","orange",
#    "banana","apple","grape","orange","banana"
#])
#print(np.unique(fruits))
#print(np.unique(fruits,return_index=True))


#ratings = np.array([5,4,5,3,5,2,4,4,5,3,2,5])
#print(np.unique(ratings))
#print(np.unique(ratings,return_counts=True))


#SET OPERATIONS:--->
#customer_ids = np.array([
#    105,102,108,105,101,
#    102,109,110,108,101,111
#])
#v = np.unique(customer_ids)
#print(v)
#value,count =np.unique(customer_ids, return_counts=True)
#print(value)
#print(count)
#idx = np.argmax(count)
#print(value[idx])
#print(count[idx])

#candidate_A = np.array([
#    "Python","SQL","PyTorch",
#    "Docker","Git","AWS"
#])

#candidate_B = np.array([
#    "Python","Git","TensorFlow",
#    "Kubernetes","AWS","Linux"
#])
#print(np.intersect1d(candidate_A,candidate_B))
#print(np.union1d(candidate_A,candidate_B))
#print(np.setdiff1d(candidate_A,candidate_B))
#print(np.setxor1d(candidate_A,candidate_B))

#train_labels = np.array([
#    "cat","dog","bird","horse","fish"
#])

#test_labels = np.array([
#    "dog","bird","lion","fish","tiger"
#])
#print(np.intersect1d(train_labels,test_labels))
#print(np.setdiff1d(train_labels,test_labels))
#print(np.setdiff1d(test_labels,train_labels))
#print(np.union1d(train_labels,test_labels))

#transaction_ids = np.array([
#    1001,1002,1003,1004,1005,
#    1006,1007,1008
#])

#flagged_ids = np.array([
#    1002,1005,1008
#])

#n = np.isin(transaction_ids,flagged_ids)
#print(n)
#h = transaction_ids[n]
#print(h)
#print(transaction_ids[~n])

#tokens = np.array([
#    "AI","ML","AI","Python","NumPy",
#    "LLM","Python","RAG","AI","RAG","VectorDB"
#])
#print(np.unique(tokens))
#values,counts =np.unique(tokens,return_counts=True)
#print(counts)
#print(values[np.argmax(counts)])
#print(values[counts==counts.min()]) # gives all the values.

#embedding_A = np.array([
#    101,102,103,104,105,106,107
#])

#embedding_B = np.array([
#    104,105,106,108,109
#])
#print(np.intersect1d(embedding_A,embedding_B))
#print(np.setdiff1d(embedding_A,embedding_B))
#3rd?
#print(np.union1d(embedding_A,embedding_B))
#print(np.setdiff1d(embedding_A,embedding_B))# unique in A
#print(np.setdiff1d(embedding_B,embedding_A))# unique in B

#languages = np.array([
#    "English","French","German",
#    "Hindi","Spanish","Japanese",
#    "English","Hindi","Chinese"
#])

#supported = np.array([
#    "English","Hindi","Japanese"
#])
#b = np.isin(languages,supported)
#print(b)
#print(languages[b])
#print(languages[~b])
#print(np.unique(languages[~b]))

#ADVANCE LINEAR ALGEBRA :------->
#import numpy as np

#A = np.array([
#    [3, 1],
#    [1, 3]
#])

#U, S, Vt = np.linalg.svd(A)
#print(U)
#print(S)
#print(Vt)
#sigma = np.diag(S)
#print(sigma)
#A_re = U @ sigma @ Vt
#error = np.linalg.norm(A-A_re)
#print(error)
#print(np.allclose(A, A_re))

#A = np.array([
#    [4, 2],
#    [2, 4]
#])

#U, S, Vt = np.linalg.svd(A)
#print(U)
#print(S)
#print(Vt)
#v =S[0]
#print(np.argmax(v))
#print(Vt[0,:])
#print(U[:,0])

#G = np.array([
#    [5, 4, 3],
#    [4, 5, 4],
#    [3, 4, 5]
#])


#def low_rank_approximation(G,k):
#    U, S, Vt = np.linalg.svd(G)
#    U_k = U[:,:k]
#    S_k = S[:k]
#    vt_k = Vt[:k,:]
#    G_approx = U_k @ np.diag(S_k) @ vt_k
#    error = np.linalg.norm(G-G_approx)
#    return error,G_approx
#G_approx = low_rank_approximation(G,k=1)
#print(G)
#print(G_approx)
#print(error)


#import numpy as np

#A = np.array([
#    [1, 2],
#    [3, 4]
#])
#Q,R = np.linalg.qr(A)
#print(Q)
#print(R)

#A_recon = Q @ R
#print(A_recon)
#print(np.allclose(A, A_recon))

#A = np.array([
#    [1, 2],
#    [3, 4],
#    [5, 6]
#])
#Q,R = np.linalg.qr(A)
#new = np.allclose(Q.T@Q,np.eye(Q.shape[1]))
#print(new)

#A = np.array([
#    [2, 1, 3],
#    [4, 5, 6],
#    [7, 8, 9]
#])
#Q,R = np.linalg.qr(A)
#print(Q)
#print(R)
#print(np.allclose(R,np.triu(R)))

#A = np.array([
#    [1, 2],
#    [3, 4],
#    [5, 6],
#    [7, 8]
#])

#Q,R = np.linalg.qr(A,mode = "reduced")
#print(Q)
#print(R)

#A = np.array([
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 10]
#])
#Q,R = np.linalg.qr(A)
#print(Q)
#print(R)
#recon = Q @ R
#print(recon)
#error = np.linalg.norm(A-recon)
#print(error)
#print(np.allclose(Q.T @ Q,np.eye(Q.shape[1])))
#print(np.allclose(R,np.triu(R)))

#CONDITIONAL OPERATION:----->

marks = np.array([35, 72, 49, 88, 95, 21, 67])
h = np.where(marks >= 50,"pass","Fail")
print(h)

temperature = np.array([15, -2, 22, -10, 30, 5, -1])
temperature[temperature<1] = 0
print(temperature)

arr = np.array([10, 15, np.nan, 25, 30])
print(np.any(np.isnan(arr)))

prob = np.array([0.2, 0.8, 0.5, 1.0, 0.9])
u = np.all((prob > 0) & (prob < 1))
print(u)

score = np.array([95, 82, 67, 49, 30, 77, 89])
h = [
    score >=90,
    score >=75,
    score >=50
]
con = ["A","B","C"]
print(np.select(h,con,default="f"))

salary = np.array([25000, 50000, 85000, 120000, 45000, 99000])
n = [
    salary < 40000,
    (salary > 40000)  & (salary <= 80000),
    salary >80000
]
j = ["low","medium","high"]
nm = np.select(n,j,default = "unknown")
print(nm)

weights = np.array([35, 55, 82, 140, 95, 200, 60])
print(np.clip(weights,40,120))

activation = np.array([-5, 3, -2, 8, 0, -1])
print(np.maximum(0,activation))


scores = np.array([
    0.8, 0.1, 0.4, 0.95, 0.02, 0.7
])
print(np.where(scores >=0.5,1,0))

image = np.array([
    [-20, 30, 120],
    [280, 255, 90],
    [60, -5, 310]
])
clip = np.clip(image,0,255)
print(clip)
print(np.where(clip>127,1,0))
print(np.all((clip>=0)&(clip<=255)))
print(np.any((image<0)| (image>255)))




















