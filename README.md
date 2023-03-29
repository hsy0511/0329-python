# 0329-python
# numpy 사용하기
## numpy 패키지
```
pip install numpy
```
cmd 창이나 터미널 창에 입력하면 패키지가 다운로드가 된다.
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/228404766-4be8168c-0cf5-4ff6-ad35-2121545ed667.png)
## numpy 배열
```python
import numpy as np
 
list = [1, 2, 3, 4] 
a = np.array(list) # numpy 배열 생성 (rank는 1 shape는 (4,))
print(a.shape) # (4,) 튜플 문법때문에 하나의 값을 가져오면 뒤에 ,를 붙임
 
b = np.array([[1,2,3],[4,5,6]]) # numpy 배열안에 리스트를 하나밖에 넣지 못하기 때문에 리스트 안에 리스트 2개를 만들어줌.
print(b.shape) # numpy 배열에서 배열의 크기가 2x3이기 때문에 shape는 (2,3)이 됨
print(b[0,0]) # b배열에 0번째 리스트의 0번째 값은 1

```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/228412533-e235b62f-2f1a-4f38-a02f-9a721b0cd2bf.png)

numpy 배열에서 배열의 차원은 rank라고 하고 차원의 크기를 튜플로 나타내는 것을 shape라고 한다.

2차원 배열에서 rank 값은 2가 된다.
## numpy에서 제공하는 함수를 사용하여 배열 만들기
![image](https://user-images.githubusercontent.com/104752580/228414019-75a9d267-e64d-411a-af9d-1e95761e47fa.png)
```python
import numpy as np

a = np.zeros((2,2)) # 2x2 배열의 값을 0으로 만들어 준다. 
print(a)
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/228414305-d4e85e92-6886-4892-9026-6b8ad1e7738e.png)
```python
import numpy as np

a = np.ones((2,3)) # 2x3 배열의 값을 1로 만들어 준다.
print(a)
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/228414582-bd77c9b8-d89e-4cec-bbc9-c27afd205068.png)

```python
import numpy as np

a = np.full((2,3), 5) # 2x3 배열의 값을 5로 지정하여 만들어 준다.
print(a)
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/228414615-b90f4775-16c1-4837-9283-faacbc86e301.png)

```python
import numpy as np

a = np.eye(3) # 3x3 배열의 값을 대각선은 1로 만들고 나머지 값은 0으로 만들어 준다.
print(a)
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/228414662-ce98caca-0252-4d41-9aed-6f097df25bc3.png)

```python
import numpy as np

a = np.array(range(20)).reshape((4,5)) # 0에서 2까지 숫자를 5개씩 끊어 4x5 배열을 만들어 준다.
print(a)

```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/228414702-f4dd81fd-ba31-4e5c-b69a-5f1f2ccdae76.png)
## numpy 슬라이싱
```python
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
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/228414993-a56dbe70-0109-41d3-b1ef-7807a6332316.png)

numpy 배열을 슬라이싱 할 때는 각 차원별로 슬라이스 할 범위를 지정해야한다.
## numpy 정수 인덱싱
```python
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
```
![image](https://user-images.githubusercontent.com/104752580/228431236-a68f2bbe-4a2f-4749-a143-5f7f7dbdb6ba.png)

정수 인덱싱은 각 차원 별로 선택되지 않은 배열 요소의 인덱스들을  일렬로 나열하여 부분 집합을 구하는 방식이다.

예를 들어서 a[[1,2],[3,4]]을 정수 인덱싱하면 a[[1,1],[4,4]]이된다. 

이처럼 정수 인덱싱을 했을때는 배열에 첫번째 요소중에 0번째와 1번째중에서 고정 값으로 있는것은 0번째이고 1번째는 내려간다.

그리고 두번째 배열에서는 1번째가 고정 값이고, 0번째가 1이 올라간다.

## numpy 부울린 인데싱
```python
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

```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/228426486-b4eff498-674b-4485-8762-fde075136806.png)

##### 조건식으로 하는 방법
```python
import numpy as np
 
lst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
a = np.array(lst) # numpy 배열 생성

bool_indexing = (a % 2 == 0) # a 리스트에서 값이 2로 나누어서 나머지가 0이 나오는 값을 true
b[bool_indexing]
print(b) # True 값만 출력
```
numpy 부울린 인덱싱은 배열 각 요소의 선택여부를 True, False로 표현한다.
## numpy 연산
#### 더하기
```python
import numpy as np
 
a = np.array([1,2,3]) # a라는 numpy 배열 생성
b = np.array([4,5,6]) # b라는 numpy 배열 생성
 
c = a + b # 배열 a와 배열 b를 더한다.
c = np.add(a, b) # add() 함수를 사용하여 배열 a와 배열 b를 더한다.
print(c)
```
![image](https://user-images.githubusercontent.com/104752580/228428741-cab342b8-c1c8-4e69-884c-1dff2912004b.png)

#### 빼기
```python
import numpy as np
 
a = np.array([1,2,3]) # a라는 numpy 배열 생성
b = np.array([4,5,6]) # b라는 numpy 배열 생성

c = a - b # 배열 a와 배열 b를 뺀다.
c = np.subtract(a, b) # subtract() 함수를 사용하여 배열 a와 배열 b를 뺀다.
print(c)
```
![image](https://user-images.githubusercontent.com/104752580/228428760-7236e04b-9f38-4595-a4df-d31acff71456.png)

#### 곱하기
```python
import numpy as np
 
a = np.array([1,2,3]) # a라는 numpy 배열 생성
b = np.array([4,5,6]) # b라는 numpy 배열 생성

c = a * b # 배열 a와 배열 b를 곱한다.
c = np.multiply(a, b) # multiply() 함수를 사용하여 배열 a와 배열 b를 곱한다.
print(c) 
```
![image](https://user-images.githubusercontent.com/104752580/228428790-a0822141-aefa-409c-82dc-c02e7f951657.png)

#### 나누기
```python
import numpy as np
 
a = np.array([1,2,3]) # a라는 numpy 배열 생성
b = np.array([4,5,6]) # b라는 numpy 배열 생성

c = a / b # 배열 a와 배열 b를 나눈다.
c = np.divide(a, b) # divide() 함수를 사용하여 배열 a와 배열 b를 나눈다.
print(c)
```
![image](https://user-images.githubusercontent.com/104752580/228428814-95b30212-ee8c-4216-82d5-791b1158da47.png)

numpy를 사용하면 배열간의 연산이 편리하다.
numpy 연산은 사칙 연산으로도 가능하고 
add(),subtract(),multiply(),divide() 등
함수를 사용하여 연산을 할 수도 있다.
#### dot() 함수
```python
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
```
![image](https://user-images.githubusercontent.com/104752580/228437867-6a59ba43-7cfa-4294-baaf-e005ef34ff3f.png)

dot() 함수는 배열에서 행렬을 곱하는데 쓰인다.
#### sum(), prod(), axis
```python
a = np.array([[1,2],[3,4]])

s = np.sum(a) # 배열의 요소들을 더함
print(s)   

s = np.sum(a, axis=0) # 열끼리 더함
print(s)  
 
s = np.sum(a, axis=1) # 행끼리 더함
print(s)
 
s = np.prod(a) # 배열의 요소들을 곱한다.
print(s)
```
![image](https://user-images.githubusercontent.com/104752580/228438761-b37233b5-bbe5-4cc9-a0bf-65a0166fb07e.png)

sum 함수는 배열의 요소들을 더한다.
prod 함수는 배열의 요소들을 곱한다.
axis 위 함수들의 선택 옵션으로 axis가 0이면 열끼리 연산하고, axis가 1이면 행끼리 연산하는 선택옵션이다.
