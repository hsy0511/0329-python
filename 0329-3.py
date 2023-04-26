# numpy 부울린 인덱싱
# numpy 부울린 인덱싱은 배열 각 요소의 선택여부를 True, False로 표현한다.
import numpy as np
 
lst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
a = np.array(lst) # numpy 배열 생성
 
bool_indexing_array = np.array([
    [False,  True, False], # 1은 false, 2는 true, 3은 false
    [True, False,  True], # 4은 true, 5는 false, 6은 true
    [False,  True, False] # 7은 false, 8는 true, 9은 false
])
 
n = a[bool_indexing_array] # ture와 false로 값을 지정한 것들 중에 true만 나오게 한다.
print(n)    

# 조건식 사용
import numpy as np
 
lst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
a = np.array(lst) # numpy 배열 생성

bool_indexing = (a % 2 == 0) # a 리스트에서 값이 2로 나누어서 나머지가 0이 나오는 값을 true
print(bool_indexing) # True 값만 출력

 