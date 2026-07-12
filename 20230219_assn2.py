import os
def clear_screen():   #화면을 지우는 함수
     os.system('cls')
     return

import random     #랜덤 모듈

def print_score_board(score_list) :   #점수판 출력 함수

    score_list[6][0] = 0                                                        
    score_list[6][1] = 0
    score_list[14][0] = 0
    score_list[14][1] = 0

    for i in range(14) :
        if i != 6 :
            score_list[14][0] += int(score_list[i][0])                             #전체 합  
            score_list[14][1] += int(score_list[i][1])

    for i in range(6) :                                                            #1부터 6까지의 합                                                         
        score_list[6][0] += int(score_list[i][0])        
        score_list[6][1] += int(score_list[i][1])

    for i in range(2) :                         # 보너스: 위 항목의 점수 합계가 63 점 이상일 때 보너스 점수 35 점 획득
        if score_list[6][i] >= 63 :
            score_list[7][i] = "+35"
        elif score_list[0][i] != "0" and score_list[1][i] != "0" and score_list[2][i] != "0" and score_list[3][i] != "0" and score_list[4][i] != "0" and score_list[5][i] != "0" : # 1 ~ 6까지의 항목이 모두 채워졌는데 63보다 작은 경우
            score_list[7][i] = 0

    for i in range(15) :                        #"0"인 경우 공백으로 나타나도록 처리
        for j in range(2) :
            if score_list[i][j] == "0" :
                score_list[i][j] = " "

    print("┌───────────────────┬───────────────────┐")
    print("│       Player      │      Computer     │")
    print("├───────────────────┴───────────────────┤")
    print("│ 1:         %2s     │ 1:         %2s     │" %(score_list[0][0], score_list[0][1]))
    print("│ 2:         %2s     │ 2:         %2s     │" %(score_list[1][0], score_list[1][1]))
    print("│ 3:         %2s     │ 3:         %2s     │" %(score_list[2][0], score_list[2][1]))
    print("│ 4:         %2s     │ 4:         %2s     │" %(score_list[3][0], score_list[3][1]))
    print("│ 5:         %2s     │ 5:         %2s     │" %(score_list[4][0], score_list[4][1]))
    print("│ 6:         %2s     │ 6:         %2s     │" %(score_list[5][0], score_list[5][1]))
    print("├───────────────────────────────────────┤")
    print("│ Sub total: %3s/63 │ Sub total: %3s/63 │" %(score_list[6][0], score_list[6][1]))
    print("│ +35 bonus:   %3s  │ +35 bonus:   %3s  │" %(score_list[7][0], score_list[7][1]))
    print("├───────────────────────────────────────┤")
    print("│ C:         %2s     │ C:         %2s     │" %(score_list[8][0], score_list[8][1]))
    print("├───────────────────────────────────────┤")
    print("│ 4K:        %2s     │ 4K:        %2s     │" %(score_list[9][0], score_list[9][1]))
    print("│ FH:        %2s     │ FH:        %2s     │" %(score_list[10][0], score_list[10][1]))
    print("│ SS:        %2s     │ SS:        %2s     │" %(score_list[11][0], score_list[11][1]))
    print("│ LS:        %2s     │ LS:        %2s     │" %(score_list[12][0], score_list[12][1]))
    print("│ Yacht:     %2s     │ Yacht:     %2s     │" %(score_list[13][0], score_list[13][1]))
    print("├───────────────────────────────────────┤")
    print("│ Total:    %3s     │ Total:    %3s     │" %(score_list[14][0], score_list[14][1]))
    print("└───────────────────────────────────────┘")

    for i in range(15) :                         #다시 0으로 바꿔줌 (오류 처리)
        for j in range(2) :
            if score_list[i][j] == " " :
                score_list[i][j] = "0"


def first_roll_dice() :      #첫 번째 주사위 조합 함수
    first_roll = []
    for i in range(1, 6) :
        random_number = random.randint(1,6)             #1부터 6 중에 하나 랜덤으로 생성
        first_roll.append(random_number)
    return first_roll


def roll_dice(dice_set=[], reroll_indices=[]) :   #다시 주사위 굴리는 함수
    if reroll_indices == "" :
        None
    
    else :
        for i in range(len(reroll_indices)) :
            if i == 0 or i % 2 == 0 :                     #스페이스가 아닌 숫자에 대해서만 처리
                if 1 <= int(reroll_indices[i]) <= 5 :     #1부터 5까지의 숫자에 대해서만 처리
                    dice_set[int(reroll_indices[i]) - 1] = random.randint(1, 6)

    return dice_set


def rerolled_dice_error_processing() :            #rerolled_dice 오류 처리 함수    
    rerolled_dice = input("Which dice to reroll (1~5)?")
    while True :
        if rerolled_dice == "" :
            break

        elif rerolled_dice == "Q" or rerolled_dice == "q" :
            break
            
        else :
            try :                                                    #에러 뜨면 except의 문장을 수행
                for x in range(len(rerolled_dice)) :
                    if x == 0 :                                      
                        a = int(rerolled_dice[x])                    #입력받은 글자가 숫자이면 good
                        inputed_value = "good"
 
                    elif x % 2 == 0 :
                        a = int(rerolled_dice[x])
                       
                    else :
                        if rerolled_dice[x] == " " :                 #스페이스면 good, 아니면 error
                            inputed_value = "good"
                        else :
                            inputed_value = "error"

            except ValueError:
                inputed_value = "error"

            if inputed_value == "error" :                            #error면 다시 입력받음
                print("Wrong Input!")
                rerolled_dice = input("Which dice to reroll (1~5)?")
            else :
                break

    return rerolled_dice 


def calc_score(dice_set, sel) :                   #점수를 반환하는 함수
    
    score = 0
    ss_set = set(dice_set)

    if sel == "1" :                           #선택한 항목이 1일 때
        for i in range(5) :
            if dice_set[i] == 1 :
                score += 1
        sel = 0                             #선택한 항목을 리스트의 인덱스와 맞춰줌

    elif sel == "2" :                           #선택한 항목이 2일 때
        for i in range(5) :
            if dice_set[i] == 2 :
                score += 2
        sel = 1 

    elif sel == "3" :                           #선택한 항목이 3일 때
        for i in range(5) :
            if dice_set[i] == 3 :
                score += 3
        sel = 2 

    elif sel == "4" :                           #선택한 항목이 4일 때
        for i in range(5) :
            if dice_set[i] == 4 :
                score += 4
        sel = 3 

    elif sel == "5" :                           #선택한 항목이 5일 때
        for i in range(5) :
            if dice_set[i] == 5 :
                score += 5
        sel = 4

    elif sel == "6" :                           #선택한 항목이 6일 때
        for i in range(5) :
            if dice_set[i] == 6 :
                score += 6
        sel = 5  
    
    elif sel == "C" or sel == "c" :                      #선택한 항목이 C일 때
        for i in range(5) :
            score += dice_set[i]
        sel = 8

    elif sel == "4K" or sel == "4k" :                    #선택한 항목이 4K일 때
        if dice_set[0] == dice_set[1] == dice_set[2] == dice_set[3] or dice_set[1] == dice_set[2] == dice_set[3] == dice_set[4] :  #동일한 주사위 눈이 4개 이상일 때
            for i in range(5) :
                score += dice_set[i] 
        sel = 9

    elif sel == "FH" or sel == "fh" :                    #선택한 항목이 FH일 때
        if (dice_set[0] == dice_set[1] and dice_set[2] == dice_set[3] == dice_set[4]) or (dice_set[0] == dice_set[1] == dice_set[2] and dice_set[3] == dice_set[4]) : #동일한 주사위가 각각 3 개, 2 개가 있을 때
            for i in range(5) :
                score += dice_set[i]
        sel = 10

    elif sel == "SS" or sel == "ss" :                    #선택한 항목이 SS일 때
        if ss_set == {1,2,3,4} or ss_set == {1,2,3,4,5} or ss_set == {1,2,3,4,6} or ss_set == {2,3,4,5} or ss_set == {2,3,4,5,6} or ss_set == {3,4,5,6} or ss_set == {1,3,4,5,6} :  #연속된 주사위 눈이 4 개이상일 때
            score = 15
        sel = 11

    elif sel == "LS" or sel == "ls" :                    #선택한 항목이 LS일 때
        if dice_set[0] == dice_set[1] - 1 == dice_set[2] - 2 == dice_set[3] - 3 == dice_set[4] - 4 :  #연속된 주사위 눈이 5 개일 때
            score = 30
        sel = 12

    elif sel == "Y" or sel == "y" :                    #선택한 항목이 Y일 때
        if dice_set[0] == dice_set[1] == dice_set[2] == dice_set[3] == dice_set[4] :  #동일한 주사위 눈이 5 개일 때
            score = 50
        sel = 13

    else :                                      #선택한 항목이 없는 항목일 때
        sel = "error"

    return score, sel


def computer_pattern(dice_set, score_list) :      #컴퓨터가 선택할 항목과 던질 주사위를 반환하는 함수
    
    p = [-1]
    r = []
    
    score_1 = 0
    if score_list[0][1] == "0" :                  #항목 1이 안 채워져 있을 때
        for i in range(5) :
            if dice_set[i] == 1 :
                score_1 += 1
        p.append(score_1)
        
    score_2 = 0
    if score_list[1][1] == "0" :                  #항목 2가 안 채워져 있을 때
        for i in range(5) :
            if dice_set[i] == 2 :
                score_2 += 2
        p.append(score_2)

    score_3 = 0
    if score_list[2][1] == "0" :                  #항목 3이 안 채워져 있을 때
        for i in range(5) :
            if dice_set[i] == 3 :
                score_3 += 3
        p.append(score_3)

    score_4 = 0
    if score_list[3][1] == "0" :                  #항목 4가 안 채워져 있을 때
        for i in range(5) :
            if dice_set[i] == 4 :
                score_4 += 4
        p.append(score_4)

    score_5 = 0
    if score_list[4][1] == "0" :                  #항목 5가 안 채워져 있을 때
        for i in range(5) :
            if dice_set[i] == 5 :
                score_5 += 5
        p.append(score_5)

    score_6 = 0
    if score_list[5][1] == "0" :                  #항목 6이 안 채워져 있을 때
        for i in range(5) :
            if dice_set[i] == 6 :
                score_6 += 6
        p.append(score_6)

    score_C = 0
    if score_list[8][1] == "0" :                  #항목 C가 안 채워져 있을 때
        for i in range(5) :
            score_C += dice_set[i]
        if score_C >= 20 :
            p.append(score_C)
    
    score_4K = 0
    if score_list[9][1] == "0" :                  #항목 4K가 안 채워져 있을 때
        if dice_set[0] == dice_set[1] == dice_set[2] == dice_set[3] or dice_set[1] == dice_set[2] == dice_set[3] == dice_set[4] :
            for i in range(5) :
                score_4K += dice_set[i]
        p.append(score_4K)

    score_FH = 0
    if score_list[10][1] == "0" :                  #항목 FH가 안 채워져 있을 때
        if (dice_set[0] == dice_set[1] and dice_set[2] == dice_set[3] == dice_set[4]) or (dice_set[0] == dice_set[1] == dice_set[2] and dice_set[3] == dice_set[4]) :
            for i in range(5) :
                score_FH += dice_set[i]
        p.append(score_FH)

    score_SS = 0
    if score_list[11][1] == "0" :                  #항목 SS가 안 채워져 있을 때
        if dice_set[0] == dice_set[1] - 1 == dice_set[2] - 2 == dice_set[3] - 3 or dice_set[1] == dice_set[2] - 1 == dice_set[3] - 2 == dice_set[4] - 3 :
            score_SS = 15
        p.append(score_SS)

    score_LS = 0
    if score_list[12][1] == "0" :                  #항목 LS가 안 채워져 있을 때
        if dice_set[0] == dice_set[1] - 1 == dice_set[2] - 2 == dice_set[3] - 3 == dice_set[4] - 4 :
            score_LS = 30
        p.append(score_LS)

    score_Y = 0
    if score_list[13][1] == "0" :                  #항목 Y가 안 채워져 있을 때
        if dice_set[0] == dice_set[1] == dice_set[2] == dice_set[3] == dice_set[4] : 
            score_Y = 50
        p.append(score_Y)

    p.sort()

    if p[-1] == score_1 :                        #가장 높은 점수를 만들 수 있는 칸이 1일 때
        sel = "1"
        for i in range(5) :
            if dice_set[i] != 1 :
                r.append(i)

    elif p[-1] == score_2 :                        #가장 높은 점수를 만들 수 있는 칸이 2일 때
        sel = "2"
        for i in range(5) :
            if dice_set[i] != 2 :
                r.append(i)
    
    elif p[-1] == score_3 :                        #가장 높은 점수를 만들 수 있는 칸이 3일 때
        sel = "3"
        for i in range(5) :
            if dice_set[i] != 3 :
                r.append(i)

    elif p[-1] == score_4 :                        #가장 높은 점수를 만들 수 있는 칸이 4일 때
        sel = "4"
        for i in range(5) :
            if dice_set[i] != 4 :
                r.append(i)

    elif p[-1] == score_5 :                        #가장 높은 점수를 만들 수 있는 칸이 5일 때
        sel = "5"
        for i in range(5) :
            if dice_set[i] != 5 :
                r.append(i)

    elif p[-1] == score_6 :                        #가장 높은 점수를 만들 수 있는 칸이 6일 때
        sel = "6"
        for i in range(5) :
            if dice_set[i] != 6 :
                r.append(i)

    elif p[-1] == score_C :                        #가장 높은 점수를 만들 수 있는 칸이 C일 때
        sel = "C"
        for i in range(5) :
            if dice_set[i] <= 3 :
                r.append(i)

    elif p[-1] == score_4K :                        #가장 높은 점수를 만들 수 있는 칸이 4K일 때
        sel = "4K"
        if score_Y == 0 :
            for i in range(5) :
                r.append(i)

    elif p[-1] == score_FH :                        #가장 높은 점수를 만들 수 있는 칸이 FH일 때
        sel = "FH"
        if score_Y == 0 :
            for i in range(5) :
                r.append(i)

    elif p[-1] == score_SS :                        #가장 높은 점수를 만들 수 있는 칸이 SS일 때
        sel = "SS"
        if score_Y == 0 :
            for i in range(5) :
                r.append(i)

    elif p[-1] == score_LS :                        #가장 높은 점수를 만들 수 있는 칸이 LS일 때
        sel = "LS"
        if score_Y == 0 :
            for i in range(5) :
                r.append(i)

    elif p[-1] == score_Y :                        #가장 높은 점수를 만들 수 있는 칸이 Y일 때
        sel = "Y"
        if score_Y == 0 :
            for i in range(5) :
                r.append(i)

    elif p == [-1] :
        sel = "C"
    
    if p[-1] == 0 :                              #가장 높은 점수가 0일 때
        zero = []
        if score_list[0][1] == "0" :
            zero.append("1")
        if score_list[1][1] == "0" :
            zero.append("2")
        if score_list[2][1] == "0" :
            zero.append("3")
        if score_list[3][1] == "0" :
            zero.append("4")
        if score_list[4][1] == "0" :
            zero.append("5")
        if score_list[5][1] == "0" :
            zero.append("6")
        if score_list[8][1] == "0" :
            zero.append("C")
        if score_list[9][1] == "0" :
            zero.append("4K")
        if score_list[10][1] == "0" :
            zero.append("FH")
        if score_list[11][1] == "0" :
            zero.append("SS")
        if score_list[12][1] == "0" :
            zero.append("LS")
        if score_list[13][1] == "0" :
            zero.append("Y")

        sel = random.choice(zero)

    return sel, r


def file_store(score_list) :                      #파일 저장하는 함수

    for i in range(15) :                          #"0"인 경우 X으로 나타나도록 처리
        for j in range(2) :
            if score_list[i][j] == "0" :
                score_list[i][j] = "x"

    filename = input("Game paused. Enter the filename to save:\n")
    print("File saved")

    with open(filename, "w") as file :                                           #파일을 열고 나중에 자동으로 닫아줌

        file.write("1: %s %s   \n" %(score_list[0][0], score_list[0][1]))        #파일에 점수판 리스트의 값을 한 줄씩 써줌
        file.write("2: %s %s   \n" %(score_list[1][0], score_list[1][1]))
        file.write("3: %s %s   \n" %(score_list[2][0], score_list[2][1]))
        file.write("4: %s %s   \n" %(score_list[3][0], score_list[3][1]))
        file.write("5: %s %s   \n" %(score_list[4][0], score_list[4][1]))
        file.write("6: %s %s   \n" %(score_list[5][0], score_list[5][1]))
        file.write("C: %s %s   \n" %(score_list[8][0], score_list[8][1]))
        file.write("4K: %s %s   \n" %(score_list[9][0], score_list[9][1]))
        file.write("FH: %s %s   \n" %(score_list[10][0], score_list[10][1]))
        file.write("SS: %s %s   \n" %(score_list[11][0], score_list[11][1]))
        file.write("LS: %s %s   \n" %(score_list[12][0], score_list[12][1]))
        file.write("Y: %s %s   \n" %(score_list[13][0], score_list[13][1]))

    for i in range(15) :                        #다시 "0"으로 바꿔줌
        for j in range(2) :
            if score_list[i][j] == "x" :
                score_list[i][j] = "0"


def load_file2list(filename, score_list) :                    #파일 불러오는 함수
    x_num = 0
    
    with open(filename, "r") as file :
        
        for i in range(12) :
            line = file.readline()                            #한 줄 읽어서 변수에 할당해줌
            splited_line = line.split()                    #띄어쓰기를 기준으로 놔눠서 리스트에 넣어줌
            
            if splited_line[0] == "1:" :                      #맨 첫 글자가 "1:"인 경우
                score_list[0][0] = splited_line[1]
                score_list[0][1] = splited_line[2]

            elif splited_line[0] == "2:" :
                score_list[1][0] = splited_line[1]
                score_list[1][1] = splited_line[2]

            elif splited_line[0] == "3:" :
                score_list[2][0] = splited_line[1]
                score_list[2][1] = splited_line[2]

            elif splited_line[0] == "4:" :
                score_list[3][0] = splited_line[1]
                score_list[3][1] = splited_line[2]

            elif splited_line[0] == "5:" :
                score_list[4][0] = splited_line[1]
                score_list[4][1] = splited_line[2]

            elif splited_line[0] == "6:" :
                score_list[5][0] = splited_line[1]
                score_list[5][1] = splited_line[2]

            elif splited_line[0] == "C:" or splited_line[0] == "c:" :
                score_list[8][0] = splited_line[1]
                score_list[8][1] = splited_line[2]

            elif splited_line[0] == "4K:" or splited_line[0] == "4k:" :
                score_list[9][0] = splited_line[1]
                score_list[9][1] = splited_line[2]

            elif splited_line[0] == "FH:" or splited_line[0] == "fh:" :
                score_list[10][0] = splited_line[1]
                score_list[10][1] = splited_line[2]

            elif splited_line[0] == "SS:" or splited_line[0] == "ss:" :
                score_list[11][0] = splited_line[1]
                score_list[11][1] = splited_line[2]

            elif splited_line[0] == "LS:" or splited_line[0] == "ls:" :
                score_list[12][0] = splited_line[1]
                score_list[12][1] = splited_line[2]

            elif splited_line[0] == "Y:" or splited_line[0] == "y:" :
                score_list[13][0] = splited_line[1]
                score_list[13][1] = splited_line[2]

    for i in range(12) :
        if i <= 5 :
            if score_list[i][0] == "x" :       #"x"인 경우 변수의 값을 +1 해줘서 x의 개수를 세줌
                x_num += 1
        else :
            if score_list[i+2][0] == "x" :
                x_num += 1

    for i in range(15) :                        #"0"인 경우 int 0으로 나타나도록 처리 (bonus는 제외하고)
        for j in range(2) :
            if i != 7 :
                if score_list[i][j] == "0" :
                    score_list[i][j] = 0

    for i in range(15) :                        #"x"인 경우 "0"으로 나타나도록 처리
        for j in range(2) :
            if score_list[i][j] == "x" :
                score_list[i][j] = "0"

    return x_num


def check_error(filename) :
    check_error = "True"
    line_num = 0 

    x = ["0","0"]                                         #이 함수 안에서만 사용할 리스트를 따로 생성해줌   
    score_list = []
    for i in range(15) :
        score_list.append(x.copy())
    
    with open(filename, "r") as file :
        for line in file :
            line_num += 1                                 #줄마다 변수를 +1 해주어 줄 개수를 세줌

    with open(filename, "r") as file :
        for i in range(12) :
            line = file.readline()
            splited_line = line.split()

            if splited_line[0] == "1:" :                      #맨 첫 글자가 "1:"인 경우
                score_list[0][0] = splited_line[1]
                score_list[0][1] = splited_line[2]

            elif splited_line[0] == "2:" :
                score_list[1][0] = splited_line[1]
                score_list[1][1] = splited_line[2]

            elif splited_line[0] == "3:" :
                score_list[2][0] = splited_line[1]
                score_list[2][1] = splited_line[2]

            elif splited_line[0] == "4:" :
                score_list[3][0] = splited_line[1]
                score_list[3][1] = splited_line[2]

            elif splited_line[0] == "5:" :
                score_list[4][0] = splited_line[1]
                score_list[4][1] = splited_line[2]

            elif splited_line[0] == "6:" :
                score_list[5][0] = splited_line[1]
                score_list[5][1] = splited_line[2]

            elif splited_line[0] == "C:" or splited_line[0] == "c:" :
                score_list[8][0] = splited_line[1]
                score_list[8][1] = splited_line[2]

            elif splited_line[0] == "4K:" or splited_line[0] == "4k:" :
                score_list[9][0] = splited_line[1]
                score_list[9][1] = splited_line[2]

            elif splited_line[0] == "FH:" or splited_line[0] == "fh:" :
                score_list[10][0] = splited_line[1]
                score_list[10][1] = splited_line[2]

            elif splited_line[0] == "SS:" or splited_line[0] == "ss:" :
                score_list[11][0] = splited_line[1]
                score_list[11][1] = splited_line[2]

            elif splited_line[0] == "LS:" or splited_line[0] == "ls:" :
                score_list[12][0] = splited_line[1]
                score_list[12][1] = splited_line[2]

            elif splited_line[0] == "Y:" or splited_line[0] == "y:" :
                score_list[13][0] = splited_line[1]
                score_list[13][1] = splited_line[2]

    for i in range(15) :                        #"x"인 경우 "-1"으로 나타나도록 처리
        for j in range(2) :
            if score_list[i][j] == "x" :
                score_list[i][j] = "-1"
           
    for i in range(2) :                        #점수판 리스트의 값들이 그 항목에 불가능한 점수일 경우 변수에 "False"를 할당해줌
        if int(score_list[0][i]) != -1 and int(score_list[0][i]) != 0 and int(score_list[0][i]) != 1 and int(score_list[0][i]) != 2 and int(score_list[0][i]) != 3 and int(score_list[0][i]) != 4 and int(score_list[0][i]) != 5 :
            check_error = "False"

        if int(score_list[1][i]) != -1 and int(score_list[1][i]) != 0 and int(score_list[1][i]) != 2 and int(score_list[1][i]) != 4 and int(score_list[1][i]) != 6 and int(score_list[1][i]) != 8 and int(score_list[1][i]) != 10 :
            check_error = "False"

        if int(score_list[2][i]) != -1 and int(score_list[2][i]) != 0 and int(score_list[2][i]) != 3 and int(score_list[2][i]) != 6 and int(score_list[2][i]) != 9 and int(score_list[2][i]) != 12 and int(score_list[2][i]) != 15 :
            check_error = "False"

        if int(score_list[3][i]) != -1 and int(score_list[3][i]) != 0 and int(score_list[3][i]) != 4 and int(score_list[3][i]) != 8 and int(score_list[3][i]) != 12 and int(score_list[3][i]) != 16 and int(score_list[3][i]) != 20 :
            check_error = "False"

        if int(score_list[4][i]) != -1 and int(score_list[4][i]) != 0 and int(score_list[4][i]) != 5 and int(score_list[4][i]) != 10 and int(score_list[4][i]) != 15 and int(score_list[4][i]) != 20 and int(score_list[4][i]) != 25 :
            check_error = "False"

        if int(score_list[5][i]) != -1 and int(score_list[5][i]) != 0 and int(score_list[5][i]) != 6 and int(score_list[5][i]) != 12 and int(score_list[5][i]) != 18 and int(score_list[5][i]) != 24 and int(score_list[5][i]) != 30 :
            check_error = "False"

        if int(score_list[8][i]) != -1 and (int(score_list[8][i]) < 5 or int(score_list[8][i]) > 30):
            check_error = "False"

        if int(score_list[9][i]) != -1 and int(score_list[9][i]) != 0 and (int(score_list[9][i]) < 5 or int(score_list[9][i]) > 30):
            check_error = "False"

        if int(score_list[10][i]) != -1 and int(score_list[10][i]) != 0 and int(score_list[10][i]) != 5 and int(score_list[10][i]) != 30 and (int(score_list[10][i]) < 7 or int(score_list[10][i]) > 28):
            check_error = "False"

        if int(score_list[11][i]) != -1 and int(score_list[11][i]) != 0 and int(score_list[11][i]) != 15 :
            check_error = "False"

        if int(score_list[12][i]) != -1 and int(score_list[12][i]) != 0 and int(score_list[12][i]) != 30 :
            check_error = "False"

        if int(score_list[13][i]) != -1 and int(score_list[13][i]) != 0 and int(score_list[13][i]) != 50 :
            check_error = "False"
        

        if line_num >= 13 :                       #줄 개수가 13 이상인 경우 변수에 "False"를 할당해줌
            check_error = "False"

    return check_error


while True :                                      #게임 반복

    x = ["0","0"]               #점수판에 쓸 이차원 리스트 생성
    y = []
    for i in range(15) :
        y.append(x.copy())

    print("[Yacht Dice]")                            #초기 메뉴 화면
    print("----------------------------------")
    print("1. New Game 2. Load Game 3. Exit")
    print("----------------------------------")

    while True :
        try :                                                       #입력 받은 값이 숫자가 아닌 경우 except의 문장을 실행함
            selected_menu = int(input("Select a menu: "))           #초기 메뉴 선택
            while selected_menu < 1 or selected_menu > 3 :          #1~3의 값이 아니면 반복함
                print("Wrong Input!")
                selected_menu = int(input("Select a menu: "))
            print("")
            break

        except :
            print("Wrong Input!")

    if selected_menu == 1 :                                 #메뉴에서 1을 선택한 경우
        print("Starting a game...")

        print_score_board(y)
        print("")

        for turn in range(1, 13) :

            print("[Player's Turn (%d/12)]" %turn)                           #플레이어 순서
            player_roll = first_roll_dice()                  
            print("Roll:", player_roll)                             #플레이어가 첫 번째 던진 주사위 출력
            
            Rerolled_dice = rerolled_dice_error_processing()

            if Rerolled_dice == "Q" or Rerolled_dice == "q" :           #Q 입력 시 현재까지의 점수판을 파일에 저장
                print("")
                file_store(y)
                print("")
                break
            
            if Rerolled_dice != "" :                                    #엔터를 입력받지 않은 경우
                player_roll = roll_dice(player_roll, Rerolled_dice)
                print("Roll:", player_roll)                             #플레이어가 두 번째 던진 주사위 출력

                Rerolled_dice = rerolled_dice_error_processing()

                if Rerolled_dice == "Q" or Rerolled_dice == "q" :       
                    print("")
                    file_store(y)
                    print("")
                    break

                if Rerolled_dice != "" :
                    player_roll = roll_dice(player_roll, Rerolled_dice)
                    print("Roll:", player_roll)                             #플레이어가 세 번째 던진 주사위 출력

            print("")
            player_roll.sort()                                      
            print("Sorted roll:", player_roll)                      #정렬된 최종 주사위 출력
            choosed_category = input("Choose a category: ")        #점수판에서 원하는 항목 선택

            if choosed_category == "Q" or choosed_category == "q" :           #Q 입력 시 현재까지의 점수판을 파일에 저장
                print("")
                file_store(y)
                print("")
                break
            
            Score, Choosed_category = calc_score(player_roll, choosed_category)        #점수 계산
            while True :
                try :
                    if y[Choosed_category][0] == "0" : 
                        break
                
                except TypeError :
                    None
                
                print("Wrong Input!")
                choosed_category = input("Choose a category: ")        
                Score, Choosed_category = calc_score(player_roll, choosed_category)
                


            y[Choosed_category][0] = Score                          #점수판 이차원 리스트에 점수 반영
            print("")
            print_score_board(y)
            print("")




            print("[Computer's Turn (%d/12)]" %turn)                   #컴퓨터 순서
            com_roll = first_roll_dice()                  
            print("Roll:", com_roll)                             #컴퓨터가 첫 번째 던진 주사위 출력

            com_choose_category, com_reroll_dice = computer_pattern(com_roll, y)               #컴퓨터 패턴 함수 반환값을 변수로 받음
            for i in range(len(com_reroll_dice)) :
                com_roll[com_reroll_dice[i]] = random.randint(1, 6)                            #주사위 다시 돌림
                com_reroll_dice[i] += 1
            com_reroll_dice.sort()
            print_reroll = " ".join(map(str, com_reroll_dice))                                
            print("Which dice to reroll (1~5)? %s" %print_reroll)
            
            if com_reroll_dice != [] :                                                         #엔터를 입력받지 않은 경우
                print("Roll:", com_roll)

                com_choose_category, com_reroll_dice = computer_pattern(com_roll, y)
                for i in range(len(com_reroll_dice)) :
                    com_roll[com_reroll_dice[i]] = random.randint(1, 6)
                    com_reroll_dice[i] += 1
                com_reroll_dice.sort()
                print_reroll = " ".join(map(str, com_reroll_dice))
                print("Which dice to reroll (1~5)? %s" %print_reroll)
                
                if com_reroll_dice != [] :
                    print("Roll:", com_roll)
                    
            print("")
            com_roll.sort()
            print("Sorted roll:", com_roll)
            print("Choose a category: %s" %com_choose_category)
            print("")

            Score, Choosed_category = calc_score(com_roll, com_choose_category)
            
            y[Choosed_category][1] = Score
            print_score_board(y)
            print("")

            if turn == 12 :                                   #마지막 턴인 경우
                if y[14][0] > y[14][1] :                      #player 점수 총합이 computer 점수 총합부터 높은 경우 
                    print("You win!")
            
                elif y[14][0] < y[14][1] :
                    print("computer win!")

                elif y[14][0] == y[14][1] :
                    print("draw!")


    
    
    elif selected_menu == 2 :                                         #메뉴에서 2를 선택한 경우
        while True :
            try :                                                     #존재하지 않은 파일 이름을 입력받은 경우 except의 문장을 수행함   
                Filename = input("Enter filename to load: ")
                
                error_check = check_error(Filename)

                if error_check == "False" :
                    print("Invalid file content.")
                    print("")
                
                else :
                    break

            except FileNotFoundError:
                print("File does not exist.")
                print("")

        turn_num = load_file2list(Filename, y)                         #파일을 받아서 점수판 리스트에 값을 반영해줌

        print("")
        print("Starting a game...")
        
        print_score_board(y)
        print("")

        for turn in range(turn_num) :

            print("[Player's Turn (%d/12)]" %(12 - turn_num + turn + 1))                           #플레이어 순서
            player_roll = first_roll_dice()                  
            print("Roll:", player_roll)                             #플레이어가 첫 번째 던진 주사위 출력
            
            Rerolled_dice = rerolled_dice_error_processing()

            if Rerolled_dice == "Q" or Rerolled_dice == "q" :           #Q 입력 시 현재까지의 점수판을 파일에 저장
                print("")
                file_store(y)
                print("")
                break

            if Rerolled_dice != "" :                                    #엔터를 입력받지 않은 경우
                player_roll = roll_dice(player_roll, Rerolled_dice)
                print("Roll:", player_roll)                             #플레이어가 두 번째 던진 주사위 출력

                Rerolled_dice = rerolled_dice_error_processing()

                if Rerolled_dice == "Q" or Rerolled_dice == "q" :       
                    print("")
                    file_store(y)
                    print("")
                    break

                if Rerolled_dice != "" :
                    player_roll = roll_dice(player_roll, Rerolled_dice)
                    print("Roll:", player_roll)                             #플레이어가 세 번째 던진 주사위 출력
                    
            print("")
            player_roll.sort()                                      
            print("Sorted roll:", player_roll)                      #정렬된 최종 주사위 출력
            choosed_category = input("Choose a category: ")        #점수판에서 원하는 항목 선택

            if choosed_category == "Q" or choosed_category == "q" :           #Q 입력 시 현재까지의 점수판을 파일에 저장
                print("")
                file_store(y)
                print("")
                break
            
            Score, Choosed_category = calc_score(player_roll, choosed_category)        #점수 계산
            while Choosed_category == "error" :                                       #없는 항목을 입력한 경우
                print("Wrong Input!")
                choosed_category = input("Choose a category: ")        
                Score, Choosed_category = calc_score(player_roll, choosed_category)
            while y[Choosed_category][0] != "0" :                                     #이미 채워진 항목을 입력한 경우
                print("Wrong Input!")
                choosed_category = input("Choose a category: ")        
                Score, Choosed_category = calc_score(player_roll, choosed_category)


            y[Choosed_category][0] = Score                          #점수판 이차원 리스트에 점수 반영
            print("")
            print_score_board(y)
            print("")




            print("[Computer's Turn (%d/12)]" %(12 - turn_num + turn + 1))                   #컴퓨터 순서
            com_roll = first_roll_dice()                  
            print("Roll:", com_roll)                             #컴퓨터가 첫 번째 던진 주사위 출력

            com_choose_category, com_reroll_dice = computer_pattern(com_roll, y)               #컴퓨터 패턴 함수 반환값을 변수로 받음
            for i in range(len(com_reroll_dice)) :
                com_roll[com_reroll_dice[i]] = random.randint(1, 6)                            #주사위 다시 돌림
                com_reroll_dice[i] += 1
            com_reroll_dice.sort()
            print_reroll = " ".join(map(str, com_reroll_dice))                                
            print("Which dice to reroll (1~5)? %s" %print_reroll)
            
            if com_reroll_dice != [] :                                                         #엔터를 입력받지 않은 경우
                print("Roll:", com_roll)

                com_choose_category, com_reroll_dice = computer_pattern(com_roll, y)
                for i in range(len(com_reroll_dice)) :
                    com_roll[com_reroll_dice[i]] = random.randint(1, 6)
                    com_reroll_dice[i] += 1
                com_reroll_dice.sort()
                print_reroll = " ".join(map(str, com_reroll_dice))
                print("Which dice to reroll (1~5)? %s" %print_reroll)
                
                if com_reroll_dice != [] :
                    print("Roll:", com_roll)
                    
            print("")
            com_roll.sort()
            print("Sorted roll:", com_roll)
            print("Choose a category: %s" %com_choose_category)
            print("")

            Score, Choosed_category = calc_score(com_roll, com_choose_category)
            
            y[Choosed_category][1] = Score
            print_score_board(y)
            print("")

            if 12 - turn_num + turn + 1 == 12 :
                if y[14][0] > y[14][1] :
                    print("You win!")
            
                elif y[14][0] < y[14][1] :
                    print("computer win!")

                elif y[14][0] == y[14][1] :
                    print("draw!")


    elif selected_menu == 3 :                               #메뉴에서 3을 선택한 경우
        print("Program ended. Bye!")
        break

    enter = input("Press Enter to continue...")             #엔터를 입력받으면 화면을 지우고 다시 메뉴 화면으로 돌아감
    clear_screen()


