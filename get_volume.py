# <20.06.18> by KH
# 수정 필요

import numpy as np
import random
import math

# x, y, z 좌표 생성
x = np.linspace(-1,1,100)
y = np.linspace(-1,1,100)
z = np.linspace(-1,1,100)

# 충분히 많은 수의 의 random한 좌표 선택
point_number = 10000
point_list = []     # 전체 좌표를 모을 list 선언

for i in range(point_number):
    buff_list = []  #임시 저장용 list 선언 (좌표용)
    buff_list.append(x[random.randint(0,99)])
    buff_list.append(y[random.randint(0,99)])
    buff_list.append(z[random.randint(0,99)])

    point_list.append(buff_list.copy())    # random하게 선언한 임의의 한 점을 전체 좌표 list에 저장, 중복 방지를 위해 복사


cnt = 0     # 원하는 조건에 해당하는지 여부 파악 카운터 선언

for i in range(point_number):
    constraints =  math.sqrt((point_list[i][0]**2 + point_list[i][1]**2 + point_list[i][2]**2)) - 1   # 각 점에 구의 공식 사용

    if constraints<0: # 구의 안쪽에 있을 경우 cnt 증가
        cnt +=1

print("구의 넓이는", cnt/point_number * 2*2*2, "입니다")


