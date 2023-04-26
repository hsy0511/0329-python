# numpy 정수 인덱싱
# 정수 인덱싱은 각 차원 별로 선택되지 않은 배열 요소의 인덱스들을  일렬로 나열하여 부분 집합을 구하는 방식이다.
# 예를 들어서 a[[1,2],[3,4]]을 정수 인덱싱하면 a[[1,1],[4,4]]이된다. 
# 이처럼 정수 인덱싱을 했을때는 배열에 첫번째 요소중에 0번째와 1번째중에서 고정 값으로 있는것은 0번째이고 1번째는 내려간다.
# 그리고 두번째 배열에서는 1번째가 고정 값이고, 0번째가 1이 올라간다.

import numpy as np
 
lst = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
a = np.array(lst) # numpy 배열 생성
 
s = a[[0, 2], [1, 3]] # 배열에서 [0,2]번 값과 [1,3]번 값을 정수 인덱싱 한다.
 
print(s) # 첫번째 인덱싱 값 [0,2]에서는 0이 고정이고 2가 내려가기 때문에 [0,1]이되고,
         # 두번째 인덱싱 값 [1,3]에서는 3이 고정되고 1이 올라가 [2,3]이 된다.

import numpy as np
 
lst1 = [
    [1,2],
    [3,4]
]
 
lst2 = [
    [5,6],
    [7,8]
]
a = np.array(lst1)
b = np.array(lst2)
 
c = np.dot(a, b) # dot()는 행렬을 곱하는 함수 이다.
                 # (1*5+2*7=19, 1*6+2*8=22, 3*5+4*7=43, 3*6+4*8=50)
print(c)

 
a = np.array([[1,2],[3,4]])

s = np.sum(a) # 배열의 요소들을 더함
print(s)   

s = np.sum(a, axis=0) # 열끼리 더함
print(s)  
 
s = np.sum(a, axis=1) # 행끼리 더함
print(s)
 
s = np.prod(a) # 배열의 요소들을 곱한다.
print(s)