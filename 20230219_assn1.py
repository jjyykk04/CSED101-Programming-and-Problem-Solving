import os
def clear_screen():   #화면을 지우는 함수
     os.system('cls') # Windows 콘솔 창에서 실행 시 주석 해제
     # os.system('clear') # Linux 콘솔 창에서 실행 시 주석 해제
     # clear_output() # jupyter notebook 외 실행 시 주석 처리할 것
     return

import random     #컴퓨터의 선택을 랜덤으로 정하는 함수
def computer_choice() :
    option = ["가위", "바위", "보"]
    result = random.choice(option)
    return result 

def print_stairs(stairs_number, player_state, computer_state):

    global move
    global win1
    global win2
    
    n = (stairs_number + 1) // 2    #계단의 층 수를 의미

    print("총 계단 수: %d" %stairs_number)
    print("PLAYER:   ○ <%d>" %player_state)
    print("COMPUTER: ● <%d>" %(stairs_number-computer_state))
    print("")

    for i in range(n+1) :
        if i == n :   #마지막 줄인 경우(예외 처리)
            if stairs_number % 2 == 0 :  # 짝수인 경우
                if player_state == computer_state == n+1 // 2 :  #중간에서 겹칠 때
                    for j in range(i) :
                        print("▨ ", end="")
                    print("◑ ", end = "") 
                    for j in range(i) :
                        print("▨ ", end="")
                    print("")
                
                elif player_state == n+1 // 2 :   #중간에 player가 있을 때
                    for j in range(i) :
                        print("▨ ", end="")
                    print("○ ", end = "") 
                    for j in range(i) :
                        print("▨ ", end="")
                    print("")

                elif computer_state == n+1 // 2 :   #중간에 computer가 있을 때
                    for j in range(i) :
                        print("▨ ", end="")
                    print("● ", end = "") 
                    for j in range(i) :
                        print("▨ ", end="")
                    print("")

                else :
                    for j in range(i) :      #계단만 있을 때
                        print("▨ ", end="")
                    print("  ", end="")
                    for j in range(i) :
                        print("▨ ", end="")
                    print("")


            else :  #홀수인 경우 (계단만 있음)
                for j in range(i) :
                    print("▨ ", end="")
                for j in range(i) :
                    print("▨ ", end="")
                print("")
        
        else :   #마지막 줄이 아닌 경우
            if player_state == i and computer_state == stairs_number-i :    #왼쪽에 player가 있고 오른쪽에 computer가 있을 때
                for j in range(i) :
                    print("▨ ", end="")
                print("○ ", end = "")
                for j in range(stairs_number-2*i-1):
                    print("  ", end="")
                print("● ", end = "")
                for j in range(i):
                    print("▨ ", end="")
                print("")

            elif player_state == stairs_number-i and computer_state == i :    #왼쪽에 computer가 있고 오른쪽에 player가 있을 때
                for j in range(i) :
                    print("▨ ", end="")
                print("● ", end = "")
                for j in range(stairs_number-2*i-1):
                    print("  ", end="")
                print("○ ", end = "")
                for j in range(i):
                    print("▨ ", end="")
                print("")

            elif player_state == i and computer_state == i :    #왼쪽에서 겹칠 때
                for j in range(i) :
                    print("▨ ", end="")
                print("◑ ", end = "")
                for j in range(stairs_number-2*i):
                    print("  ", end="")
                for j in range(i):
                    print("▨ ", end="")
                print("")

            elif player_state == stairs_number-i and computer_state == stairs_number-i :    #오른쪽에서 겹칠 때
                for j in range(i) :
                    print("▨ ", end="")
                for j in range(stairs_number-2*i):
                    print("  ", end="")
                print("◑ ", end = "")
                for j in range(i):
                    print("▨ ", end="")
                print("")
            
            elif player_state == stairs_number-i and computer_state == stairs_number-i :    #오른쪽에서 겹칠 때
                for j in range(i) :
                    print("▨ ", end="")
                for j in range(stairs_number-2*i):
                    print("  ", end="")
                print("◑ ", end = "")
                for j in range(i):
                    print("▨ ", end="")
                print("")

            elif player_state == i :    #왼쪽에 player가 있을 때
                for j in range(i) :
                    print("▨ ", end="")
                print("○ ", end = "")
                for j in range(stairs_number-2*i):
                    print("  ", end="")
                for j in range(i):
                    print("▨ ", end="")
                print("")

            elif player_state == stairs_number-i :    #오른쪽에 player가 있을 때
                for j in range(i) :
                    print("▨ ", end="")
                for j in range(stairs_number-2*i):
                    print("  ", end="")
                print("○ ", end = "")
                for j in range(i):
                    print("▨ ", end="")
                print("")    

            elif computer_state == i :   #왼쪽에 computer가 있을 때
                for j in range(i) :
                    print("▨ ", end="")
                print("● ", end = "")
                for j in range(stairs_number-2*i):
                    print("  ", end="")
                for j in range(i):
                    print("▨ ", end="")
                print("")

            elif computer_state == stairs_number-i :   #오른쪽에 computer가 있을 때
                for j in range(i) :
                    print("▨ ", end="")
                for j in range(stairs_number-2*i):
                    print("  ", end="")
                print("● ", end = "")
                for j in range(i):
                    print("▨ ", end="")
                print("")

            else :     #계단만 있을 때
                for j in range(i) :
                    print("▨ ", end="")
                for j in range(stairs_number-2*i+1):
                    print("  ", end="")
                for j in range(i):
                    print("▨ ", end="")
                print("")

def print_rock() :
    print("┌────────────────────────────────────────┐")
    print("│          ▩ ▩ ▩ ▩ ▩                     │")
    print("│      ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩                 │") 
    print("│    ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩               │")
    print("│  ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩               │")
    print("│  ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩             │")
    print("│  ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩             │") 
    print("│  ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩             │") 
    print("│  ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩               │") 
    print("│    ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩                 │") 
    print("│      ▩ ▩ ▩ ▩ ▩ ▩ ▩                     │") 
    print("└────────────────────────────────────────┘")

def  print_paper() :

    print("┌────────────────────────────────────────┐")
    print("│        ▩ ▩ ▩ ▩ ▩                       │")
    print("│      ▩ ▩ ▩                             │")
    print("│    ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩         │")
    print("│  ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩                   │")
    print("│  ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩       │")
    print("│  ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩                   │")
    print("│  ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩         │")
    print("│  ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩                   │")
    print("│    ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩             │")
    print("│      ▩ ▩ ▩ ▩ ▩                         │")
    print("└────────────────────────────────────────┘")

def print_scissors() :

    print("┌────────────────────────────────────────┐")
    print("│                              ▩ ▩       │")
    print("│            ▩ ▩           ▩ ▩ ▩ ▩ ▩     │")
    print("│          ▩ ▩ ▩ ▩ ▩     ▩ ▩ ▩ ▩ ▩ ▩ ▩   │")
    print("│        ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩     │")
    print("│    ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩             │")
    print("│  ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩                     │")
    print("│  ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩                 │")
    print("│  ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩             │")
    print("│    ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩       │")
    print("│      ▩ ▩ ▩ ▩ ▩ ▩ ▩   ▩ ▩ ▩ ▩ ▩ ▩ ▩     │")
    print("│        ▩ ▩ ▩ ▩ ▩ ▩       ▩ ▩ ▩ ▩ ▩     │")
    print("│          ▩ ▩ ▩               ▩ ▩       │")
    print("└────────────────────────────────────────┘")


#게임 시작
print("======================")
print("[묵찌빠 계단 오르기]")
print("======================")
print("○                   ●")
print("▨                   ▨")
print("▨ ▨               ▨ ▨")
print("▨ ▨ ▨           ▨ ▨ ▨")
print("▨ ▨ ▨ ▨       ▨ ▨ ▨ ▨")
print("▨ ▨ ▨ ▨ ▨   ▨ ▨ ▨ ▨ ▨")
print("▨ ▨ ▨ ▨ ▨ ▨ ▨ ▨ ▨ ▨ ▨")
print("")

stairs_number = int(input("게임을 위한 계단의 개수를 입력해주세요. <10 ~ 30> >> "))    #계단 개수 입력
while stairs_number < 10 or stairs_number > 30 :    #계단 개수가 10~30이 아니면 반복되도록
    stairs_number = int(input("게임을 위한 계단의 개수를 입력해주세요. <10 ~ 30> >> "))
clear_screen()

player_state = 0                   #palyer 초기 위치 설정
computer_state = stairs_number     #computer 초기 위치 설정

print_stairs(stairs_number,0,stairs_number)
print("")
input("계속하려면 엔터를 눌러주세요...")
clear_screen()

while True : #게임 반복
    
#가위바위보 시작
    while True : #무승부일 때만 가위바위보 반복
        
        win1 = ""   #일단 빈 문자열을 변수로 받음 (나중에 쓸 예정)
        win2 = ""

        computer_selected1 = computer_choice()    #가위바위보에서 컴퓨터가 랜덤으로 내는 것을 변수로 받음
        
        print("[공격권 결정 가위바위보]")
        player_choice = input("가위, 바위, 보 중 하나 선택: ")
        while not (player_choice == "가위" or player_choice == "바위" or player_choice == "보") :   #가위 or 바위 or 보가 아닐 경우 다시 입력 할 수 있도록
            player_choice = input("가위, 바위, 보 중 하나 선택: ")
        print("")

        print("[컴퓨터 선택]")
        if computer_selected1 == "가위":
            print_scissors()
        elif computer_selected1 == "바위":
            print_rock()
        elif computer_selected1 == "보":
            print_paper()

        print("[플레이어 선택]")
        if player_choice == "가위" :
            print_scissors()
        elif player_choice == "바위" :
            print_rock()
        elif player_choice == "보" :
            print_paper()


        if (player_choice == "가위" and computer_selected1 == "보") or \
        (player_choice == "바위" and computer_selected1 == "가위") or \
        (player_choice == "보" and computer_selected1 == "바위") :   #가위바위보에서 palyer가 이겼을 경우
            print("[결과] 플레이어 공격, 컴퓨터 수비입니다.")
            win1 = "player"       #묵찌빠의 끝났을 때 palyer가 공격권을 가지고 있었다는 것을 나타냄 
            win2 = "player"
            break

        elif (player_choice == "가위" and computer_selected1 == "바위") or \
            (player_choice == "바위" and computer_selected1 == "보") or \
            (player_choice == "보" and computer_selected1 == "가위") :   #가위바위보에서 computer가 이겼을 경우
            print("[결과] 컴퓨터 공격, 플레이어 수비입니다.")
            win1 = "computer"     #묵찌빠의 끝났을 때 computer가 공격권을 가지고 있었다는 것을 나타냄
            win2 = "computer"    
            break

        elif player_choice == computer_selected1 :   #가위바위보에서 무승부 경우
            print("[결과] 무승부입니다.")
            print("")
            input("계속하려면 엔터를 눌러주세요...")
            clear_screen()

    print("")
    input("계속하려면 엔터를 눌러주세요...")
    clear_screen()

    #묵찌빠 시작
    move = 1     # 일단 승리 시 이동 수를 1로 설정
    while True :

        if move == 1 :   # 승리 시 이동 수가 1인 경우 (전 턴이 가위바위보인 경우)
        
            print("[묵찌빠]")
            print("승리 시 이동 칸 수: %d" %move)

            if (player_choice == "가위" and computer_selected1 == "보") or \
            (player_choice == "바위" and computer_selected1 == "가위") or \
            (player_choice == "보" and computer_selected1 == "바위") :   #가위바위보에서 palyer가 이겼을 경우
                print("플레이어 공격, 컴퓨터 수비입니다.")
                victory = "플레이어 승, %d칸 이동합니다."
                win1 = "player"

            elif (player_choice == "가위" and computer_selected1 == "바위") or \
                (player_choice == "바위" and computer_selected1 == "보") or \
                (player_choice == "보" and computer_selected1 == "가위") :   #가위바위보에서 computer가 이겼을 경우
                print("컴퓨터 공격, 플레이어 수비입니다.")
                victory = "컴퓨터 승, %d칸 이동합니다."
                win1 = "computer"

            player_choice = input("가위, 바위, 보 중 하나 선택: ")
            while not (player_choice == "가위" or player_choice == "바위" or player_choice == "보") :
                player_choice = input("가위, 바위, 보 중 하나 선택: ")
            print("")

            computer_selected2 = computer_choice()    #묵찌빠에서 컴퓨터가 랜덤으로 내는 것을 변수로 받음

            print("[컴퓨터 선택]")
            if computer_selected2 == "가위":
                print_scissors()
            elif computer_selected2 == "바위":
                print_rock()
            elif computer_selected2 == "보":
                print_paper()

            print("[플레이어 선택]")
            if player_choice == "가위" :
                print_scissors()
            elif player_choice == "바위" :
                print_rock()
            elif player_choice == "보" :
                print_paper()

            if (player_choice == "가위" and computer_selected2 == "보") or \
            (player_choice == "바위" and computer_selected2 == "가위") or \
            (player_choice == "보" and computer_selected2 == "바위") :   #묵찌빠에서 palyer가 이겼을 경우
                print("[결과] 플레이어 공격, 컴퓨터 수비입니다.")
                move = move + 1    #턴 수가 증가할 때마다 이동 수도 1씩 증가
                print("")
                input("계속하려면 엔터를 눌러주세요...")
                clear_screen()

            elif (player_choice == "가위" and computer_selected2 == "바위") or \
                (player_choice == "바위" and computer_selected2 == "보") or \
                (player_choice == "보" and computer_selected2 == "가위") :   #묵찌빠에서 computer가 이겼을 경우
                print("[결과] 컴퓨터 공격, 플레이어 수비입니다.")
                move = move + 1
                print("")
                input("계속하려면 엔터를 눌러주세요...")
                clear_screen()

            elif player_choice == computer_selected2 :   #묵찌빠에서 무승부 경우
                print("[결과] 묵찌빠 종료")    
                print(victory %move)            
                if win1 == "player" :   ##player가 공격권을 가지고 있었던 경우
                    player_state = player_state + move    
            
                elif win1 == "computer" :  #computer가 공격권을 가지고 있었던 경우
                    computer_state = computer_state - move
                break

        else :   # 승리 시 이동 수 > 1 인 경우 (전 턴이 묵찌빠인 경우)
            print("[묵찌빠]")
            print("승리 시 이동 칸 수: %d" %move)

            if (player_choice == "가위" and computer_selected2 == "보") or \
            (player_choice == "바위" and computer_selected2 == "가위") or \
            (player_choice == "보" and computer_selected2 == "바위") :   #묵찌빠에서 palyer가 이겼을 경우
                print("플레이어 공격, 컴퓨터 수비입니다.")
                victory = "플레이어 승, %d칸 이동합니다."
                win2 = "player"

            elif (player_choice == "가위" and computer_selected2 == "바위") or \
                (player_choice == "바위" and computer_selected2 == "보") or \
                (player_choice == "보" and computer_selected2 == "가위") :   #묵찌빠에서 computer가 이겼을 경우
                print("컴퓨터 공격, 플레이어 수비입니다.")
                victory = "컴퓨터 승, %d칸 이동합니다."
                win2 = "computer"

            player_choice = input("가위, 바위, 보 중 하나 선택: ")
            while not (player_choice == "가위" or player_choice == "바위" or player_choice == "보") :
                player_choice = input("가위, 바위, 보 중 하나 선택: ")
            print("")

            computer_selected2 = computer_choice()

            print("[컴퓨터 선택]")
            if computer_selected2 == "가위":
                print_scissors()
            elif computer_selected2 == "바위":
                print_rock()
            elif computer_selected2 == "보":
                print_paper()

            print("[플레이어 선택]")
            if player_choice == "가위" :
                print_scissors()
            elif player_choice == "바위" :
                print_rock()
            elif player_choice == "보" :
                print_paper()

            if (player_choice == "가위" and computer_selected2 == "보") or \
            (player_choice == "바위" and computer_selected2 == "가위") or \
            (player_choice == "보" and computer_selected2 == "바위") :   #묵찌빠에서 palyer가 이겼을 경우
                print("[결과] 플레이어 공격, 컴퓨터 수비입니다.")
                move = move + 1
                win2 = "player"
                print("")
                input("계속하려면 엔터를 눌러주세요...")
                clear_screen()

            elif (player_choice == "가위" and computer_selected2 == "바위") or \
                (player_choice == "바위" and computer_selected2 == "보") or \
                (player_choice == "보" and computer_selected2 == "가위") :   #묵찌빠에서 computer가 이겼을 경우
                print("[결과] 컴퓨터 공격, 플레이어 수비입니다.")
                move = move + 1
                win2 = "computer"
                print("")
                input("계속하려면 엔터를 눌러주세요...")
                clear_screen()

            elif player_choice == computer_selected2 :   #묵찌빠에서 무승부 경우
                print("[결과] 묵찌빠 종료")    
                print(victory %move)
                if win2 == "player" :   #player가 공격권을 가지고 있었던 경우
                    player_state = player_state + move
        
                elif win2 == "computer" :  #computer가 공격권을 가지고 있었던 경우   
                    computer_state = computer_state - move
                break
        
    print("")            
    input("계속하려면 엔터를 눌러주세요...")
    clear_screen()
    
    if player_state >= stairs_number :    #player가 목적지에 도달한 경우
        print_stairs(stairs_number, stairs_number, computer_state)
        print("")
        print("▨ ▨ ▨ ▨ ▨ ▨ ▨ ▨ ▨ ▨ ▨ ▨ ▨")
        print("   플레이어 최종 승리!!!")
        print("▨ ▨ ▨ ▨ ▨ ▨ ▨ ▨ ▨ ▨ ▨ ▨ ▨")
        print("")
        print("게임을 종료합니다...")

    elif computer_state <= 0 :    #computer가 목적지에 도달한 경우
        print_stairs(stairs_number, player_state, 0)
        print("")
        print("▨ ▨ ▨ ▨ ▨ ▨ ▨ ▨ ▨ ▨ ▨ ▨ ▨")
        print("   컴퓨터 최종 승리!!!")
        print("▨ ▨ ▨ ▨ ▨ ▨ ▨ ▨ ▨ ▨ ▨ ▨ ▨")
        print("")
        print("게임을 종료합니다...")    
        
    else :    
        print_stairs(stairs_number, player_state, computer_state)
        input("계속하려면 엔터를 눌러주세요...")
        clear_screen()

    if player_state >= stairs_number or computer_state <= 0 :  #player 또는 computer가 목적지에 도달했을 때 게임 종료
        break













