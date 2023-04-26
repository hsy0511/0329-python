# numpy 연산
# numpy를 사용하면 배열간의 연산이 편리하다.
'''
numpy 연산은 사칙 연산으로도 가능하고 
add(),subtract(),multiply(),divide() 등
함수를 사용하여 연산을 할 수도 있다.
'''
import numpy as np
 
a = np.array([1,2,3]) # a라는 numpy 배열 생성
b = np.array([4,5,6]) # b라는 numpy 배열 생성
 
c = a + b # 배열 a와 배열 b를 더한다.
c = np.add(a, b) # add() 함수를 사용하여 배열 a와 배열 b를 더한다.
print(c)
 
c = a - b # 배열 a와 배열 b를 뺀다.
c = np.subtract(a, b) # subtract() 함수를 사용하여 배열 a와 배열 b를 뺀다.
print(c)

c = a * b # 배열 a와 배열 b를 곱한다.
c = np.multiply(a, b) # multiply() 함수를 사용하여 배열 a와 배열 b를 곱한다.
print(c) 
 
c = a / b # 배열 a와 배열 b를 나눈다.
c = np.divide(a, b) # divide() 함수를 사용하여 배열 a와 배열 b를 나눈다.
print(c)