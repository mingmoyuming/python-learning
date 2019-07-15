# -*- coding: utf-8 -*-
import random


def girl_result(probality_of_girl):
    probality = random.random()
    if probality < probality_of_girl:
        return "正面"
    else:
        return "反面"


def boy_result(probility_of_boy):
    probality = random.random()
    #    print(probality)
    if probality < probility_of_boy:
        return "正面"
    else:
        return "反面"


def game_gambing(times, probility_of_boy, probality_of_girl):
    money = 0
    for i in range(times):
        temp_result = girl_result(probality_of_girl)
        if temp_result == boy_result(probility_of_boy):
            if temp_result == "正面":
                money += 3
            else:
                money += 1
        else:
            money += -2
    return money


if __name__ == '__main__':
    for j in range(1, 10):
        game_times = 20000000
        probality_of_girl = round(0.9, 2)
        result_money = game_gambing(game_times, round(0.1 * j, 2), probality_of_girl)
        print("女人出正面的概率为 " + str(probality_of_girl) + ",第" + str(j) + "个男人出正面的概率为" + str(
            round(0.1 * j, 2)) + ",博弈次数为: " + str(game_times) + " 他赢得的钱为: " + str(result_money))
