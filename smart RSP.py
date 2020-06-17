import numpy as np
import matplotlib.pyplot as plt
import random


iteration = 10
x= np.linspace(1,iteration,10)
list_empty = []


'''
바위: 0, 가위: 100, 보: 200

전체 게임은 연습 게임과 실전 게임으로 나뉘어져 있음.

연습게임과 실전 게임은 다른 알고리즘이 적용되어 있음.

연습 게임의 경우, 상대방이 가장 많이 낸 녀석에 대한 대항값을 출력.
(단순 count)

실전 게임의 경우 연습게임에 주어진 데이터를 바탕으로 
해당 데이터가 가위, 바위, 보를 스스로 인식하여 그에 해당하는 대항값을 출력
-> 승률 100%에 근접하도록 시도.

사실상 if 문을 사용하는 것에 비해서 성능이 안좋을 수 있지만

컴퓨터 스스로 입력값을 판단하는 과정을 생각해봤음. -> 교수님 어필 파트
'''

cnt = 0     # 밖에 뺀 이유는 초기화 되기 때문
print("Train Game Start")
for i in range(iteration):
    print("iteration number:", i ,"/", iteration)
    buff = input("가위, 바위, 보\n")

    if buff == "가위":
        buff = 100
    elif buff == "바위":
        buff = 0
    elif buff == "보":
        buff = 200
    else :
        print("입력은 가위, 바위, 보 만 가능합니다")
        buff = 0 # 이거는 임의 선택헀음 -> 그래프 그리는 오타 때문에


    list_empty.append(buff)

    result_list = [list_empty.count(100), list_empty.count(0), list_empty.count(200)]
    result_arr = np.array(result_list)

    result = result_arr.argmax()

    if result == 0:
        print("컴퓨터의 결과: 바위")


        if buff == 100:
            print("You Lose!!")
        elif buff ==0:
            print("Draw~")
        else:
            print("You Win!!")
            cnt+=1


    elif result == 1:
        print('컴퓨터의 결과: 보')

        if buff == 0:
            print("You Lose!!")
        elif buff ==200:
            print("Draw~")
        else:
            print("You Win!!")
            cnt+=1

    elif result == 2:
        print('컴퓨터의 결과: 가위')

        if buff == 200:
            print("You Lose!!")
        elif buff ==100:
            print("Draw~")
        else:
            print("You Win!!")
            cnt += 1



    print("") # 이건 그냥 엔터임
print('연습 게임 승률은 ', cnt/iteration * 100 ,"% 입니다.")

plt.figure(figsize=(6.5,4))
plt.scatter(x,list_empty, alpha=0.75)
plt.title("Result of RSP")
plt.xlabel("Stage Number")
plt.ylabel("Your Choice")
plt.show()

# 임의의 함수(Hyper Plane) 선언
R_beta1 = 0.1
R_beta2 = 1000
R_beta3 = 1000
train_number =10000
# training 시작

# 이 녀석은 주먹과 가위를 구분하는 넘입니다.
for i in range(train_number):
    random_integer = random.randint(0,iteration-1)
    distinguisher_R = R_beta1*x[random_integer] - R_beta2*list_empty[random_integer] - R_beta3

    if (list_empty[random_integer] == 0) and distinguisher_R < 0 :
        R_beta3 -= 100

    elif (list_empty[random_integer] !=0) and distinguisher_R>0:
        R_beta3 += 100

    else:
        pass

S_beta1 = 0.1
S_beta2 = 1000
S_beta3 = 1000
train_number =100000
# training 시작

# 이 녀석은 가위와 보자기를 구분하는 넘입니다.
for i in range(train_number):
    random_integer = random.randint(0,iteration-1)
    distinguisher_S = S_beta1*x[random_integer] - S_beta2*list_empty[random_integer] - S_beta3

    if (list_empty[random_integer] == 100) and distinguisher_S > 0:
        break

    elif (list_empty[random_integer] ==100) and distinguisher_S<0:
        S_beta3 -= 100

    elif (list_empty[random_integer] ==200)  and distinguisher_S<0:
        S_beta3 -=100

    else:
        pass


P_beta1 = 0.1
P_beta2 = 1000
P_beta3 = 1000
train_number =10000
# training 시작

# 이 녀석은 주먹과 보자기를 구분하는 넘입니다.
for i in range(train_number):
    random_integer = random.randint(0,iteration-1)
    distinguisher_P = P_beta1*x[random_integer] - P_beta2*list_empty[random_integer] - P_beta3

    if (list_empty[random_integer] == 200) and distinguisher_P < 0:
        P_beta3 -= 100

    else:
        pass

# 트레이닝된 데이터를 바탕으로 분류 하여 실전에 투입

pan_su = int(input("몇판할래? 애송이 \n"))

cnt = 0

for i in range(pan_su):
    buff = input("뭐낼래? \n")

    if buff == "가위":
        buff = 100
    elif buff == "바위":
        buff = 0
    elif buff == "보":
        buff = 200

    else:
        print("입력은 가위, 바위 보 중에서만 해주시길 바랍니다.")

# vote 수행

    distinguisher_R = R_beta1 * 1 - R_beta2 * buff - R_beta3
    distinguisher_S = S_beta1 * 1 - S_beta2 * buff - S_beta3
    distinguisher_P = P_beta1 * 1 - P_beta2 * buff - P_beta3

    if distinguisher_R>0 :
        print("보")
        if buff == 0:
            print("You Lose!!")

        elif buff == 200:
            print("draw")

        else :
            print("You Win")
            cnt += 1

    elif distinguisher_S>0 and distinguisher_P>0 :
        print("바위")
        print("You Lose!!")

    elif distinguisher_P>0 :
        print("가위")
        if buff == 200:
            print("You Lose!!")

        elif buff == 100:
            print("draw")

        else:
            print("You Win")
            cnt += 1


print("") # 이건 그냥 엔터임
print('진심 게임 승률은 ', cnt/pan_su * 100 ,"% 입니다.")