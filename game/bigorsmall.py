# ----游戏----
import random


def roll_result(total):
    isBig = 10 <= total <= 18
    isSmall = 1 <= total <= 9

    if isBig:
        return '大'
    elif isSmall:
        return '小'


def roll_start(numbers=3, points=None):
    print('<<<<<<<<< 摇骰子 >>>>>>>>>')
    if points is None:
        points = []
    while numbers > 0:
        num = random.randint(1, 6)
        points.append(num)
        numbers = numbers - 1
    return points


def game_start(your_money=None):
    print('<<<<<<<<<< 开始玩耍 >>>>>>>>>>')
    if your_money is None:
        your_money = input('你的本金：')
    choices = ['大', '小']
    your_choice = input('买大买小：')
    your_bet = input('你下注：')
    if int(your_bet) <= int(your_money):
        if your_choice in choices:
            points = roll_start()
            total = sum(points)
            youWin = roll_result(total) == your_choice
            if youWin:
                print(f'骰子数为{points},恭喜你！')
                your_money = str(int(your_money) + int(your_bet))
                print(f'你赢了{your_bet},此时有本金{your_money}')
                game_start(your_money)
            else:
                print(f'骰子数为{points},很遗憾！')
                your_money = str(int(your_money) - int(your_bet))
                if int(your_money) > 0:
                    print(f'你输了{your_bet},此时有本金{your_money}')
                    game_start(your_money)
                else:
                    print(f'你没钱了，游戏结束')
        else:
            print('Invalid Words!')
            game_start(your_money)
    else:
        print('你没那么多钱下注')
        game_start(your_money)


game_start()

#
#
# password_list = ['*#*#','12345']
# def account_login():
#     tries = 3
#     while tries > 0:
#         password = input('Password:')
#         password_correct = password == password_list[-1]
#         password_reset = password == password_list[0]
#         if password_correct:
#             print('Login success!')
#         elif password_reset:
#             new_password = input('Enter a new password:')
#             password_list.append(new_password)
#             print('You password has changed successfully')
#             account_login()
#         else:
#             print('Wrong password or invalid input!')
#             tries = tries - 1
#
#     else:
#         print('Your account has been suspended')
#
# account_login()
#
#
#
#
#
#
#
#
# search = '168'
# num_a = '1386-168-0006'
# num_b = '1681-222-0006'
#
# print(num_a.find(search))
# print(str(num_a.find(search) + 1))
#
# print(search + ' is at ' + str(num_a.find(search) + 1) + ' to '+ str(num_a.find(search) + len(search)) + ' of num_a')
#
# print(search + ' is at ' + str(num_b.find(search) + 1) + ' to '+ str(num_b.find(search) + len(search)) + ' of num_b')
#
# help('str')
#
#
#
#
# a = ['apple', 'banana', 'other', 'orange']
# for item in a:
#     print(item)
# else:
#     print('循环结束了')
#
# my_string = "aavvccccddddeee"
# # converting the string to a set
# temp_set = set(my_string)
# # stitching set into a string using join
# new_string = ''.join(temp_set)
# print(new_string)
#
# # 反转字符串
# reversed_string = my_string[::-1]
# print(reversed_string)
#
# # 交换两个变量的值
# c1 = 100
# c2 = 300
# print(c1)
# print(c2)
# c1, c2 = c2, c1
# print(c1)
# print(c2)
#
# # 检查给定字符串是否是回文（Palindrome）
# my_string = "abcba"
# if my_string == my_string[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")
#
#
# import time
# start_time = time.time()
# # Code to check follows
# a, b = 1,2
# c = a+ b# Code to check ends
# end_time = time.time()
# time_taken_in_micro = (end_time-start_time)*(10**6)
# print(" Time taken in micro_seconds: {0} ms".format(time_taken_in_micro))
#
#
#
# print(type((1)))
# print(type((1,)))
#
#
#
