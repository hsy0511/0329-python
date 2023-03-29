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

a = arr[0:2, 0:2] # 배열의 순서대로 0번째부터 1번째까지 슬라이싱 한다.
print(a)

a = arr[1:, 1:] # 배열의 순서대로 1부터 마지막까지 슬라이싱 한다.
print(a)
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/228414993-a56dbe70-0109-41d3-b1ef-7807a6332316.png)

numpy 배열을 슬라이싱 할 때는 각 차원별로 슬라이스 할 범위를 지정해야한다.
