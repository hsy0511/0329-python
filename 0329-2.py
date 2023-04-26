# numpy 슬라이싱
# numpy 배열을 슬라이싱 할 때는 각 차원별로 슬라이스 할 범위를 지정해야한다.
import numpy as np
 
lst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
arr = np.array(lst) # numpy 배열 생성

a = arr[0:2, 0:2] # 0번째 배열에서 부터 인덱스의 0번째부터 1번째까지 슬라이싱 한다.
print(a)

a = arr[1:, 1:] # 1번째 배열에서 부터 인덱스의 1부터 마지막까지 슬라이싱 한다.
print(a)