import numpy as np
 
list = [1, 2, 3, 4] 
a = np.array(list) # numpy 배열 생성 (rank는 1 shape는 (4,))
print(a.shape) # (4,) 튜플 문법때문에 하나의 값을 가져오면 뒤에 ,를 붙임
 
b = np.array([[1,2,3],[4,5,6]]) # numpy 배열안에 리스트를 하나밖에 넣지 못하기 때문에 리스트 안에 리스트 2개를 만들어줌.
print(b.shape) # numpy 배열에서 배열의 크기가 2x3이기 때문에 shape는 (2,3)이 됨
print(b[0,0]) # b배열에 0번째 리스트의 0번째 값은 1
# numpy 배열에서 배열의 차원은 rank라고 하고 차원의 크기를 튜플로 나타내는 것을 shape라고 한다.
# 2차원 배열에서 rank 값은 2가 된다.

# numpy에서 제공하는 함수를 사용하여 배열 만들기
import numpy as np

a = np.zeros((2,2)) # 2x2 배열의 값을 0으로 만들어 준다. 
print(a)

a = np.ones((2,3)) # 2x3 배열의 값을 1로 만들어 준다.
print(a)

a = np.full((2,3), 5) # 2x3 배열의 값을 5로 지정하여 만들어 준다.
print(a)

a = np.eye(3) # 3x3 배열의 값을 대각선은 1로 만들고 나머지 값은 0으로 만들어 준다.
print(a)

a = np.array(range(20)).reshape((4,5)) # 0에서 2까지 숫자를 5개씩 끊어 4x5 배열을 만들어 준다.
print(a)




'''
numpy에서 제공하는 함수 zeros(), ones(), full(), eye(), range(n), reshape() 등이있다.
zeros()함수는 해당 배열에 다 0 을 집어넣는다.
ones()함수는 해당 배열에 다 0 을 집어넣는다.
full()함수는 해당 배열에 사용자가 지정한 값을 넣는다.
eye()함수는 대각선으로는 1 나머지는 0으로 2차원 배열을 만든다. 
range()함수는 0부터 n-1까지의 숫자를 생성한다.
reshape()함수는 배열을 다차원으로 생성한다.

'''
