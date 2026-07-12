import random

class Posmon :                                                      #포스몬 클래스
    def __init__(self) :
        self.health = 0                                            # 포스몬의 체력 (int)
        self.max_health = 0                                            # 포스몬의 최대(초기) 체력 (int)
        self.attack = 0                                              # 포스몬의 공격력 (int)
        self.defence = 0                                              # 포스몬의 방어력 (int)
        self.max_attack = 0                                             # 포스몬의 최대 공격력 (int)
        self.max_defence = 0                                            # 포스몬의 최대 방어력 (int)
        self.moves = 0                                              # 포스몬이 보유한 기술(Move) 리스트 (list of Move)
        self.name = 0                                              # 포스몬의 이름(str)

    def get_name(self) -> str :                                    # 포스몬의 이름을 반환하는 메서드
        return self.name
    
    def get_health(self) :
        return self.health

    def get_attack(self) :
        if self.attack < 0 :
            self.attack = 0
        return self.attack

    def get_defence(self) :
        if self.defence < 0 :
            self.defence = 0
        return self.defence 
    
    def get_max_health(self) -> int :                              # 포스몬의 최대 체력을 반환하는 메서드
        return self.max_health 
    
    def get_type(self) -> str :                                    # 포스몬의 타입을 반환하는 메서드
        pass

    def reset_status(self, reset_health:bool = False):             # 포스몬의 공격력과 방어력을 생성될 때 값으로 초기화하는 메서드
        if reset_health :
            self.health, self.attack, self.defence = self.max_health, self.max_attack, self.max_defence
        else :
            self.attack, self.defence = self.max_attack, self.max_defence


class Ponix(Posmon) :                                               #Ponix 클래스 (Posmon 클래스를 상속받음)
    def __init__(self) :
        super().__init__()
        self.max_health = 86
        self.max_attack = 20                                         
        self.max_defence = 23
        self.name = "Ponix"
        self.type = "Paper"
        self.skil = [Tackle(), Growl(), SwordDance()]

    def get_type(self) -> str :
        super().get_type()
        return self.type


class Normie(Posmon) :                                              #Normie 클래스 (Posmon 클래스를 상속받음)
    def __init__(self) :
        super().__init__()
        self.max_health = 80
        self.max_attack = 20                                   
        self.max_defence = 20
        self.name = "Normie"
        self.type = "Nothing"
        self.skil = [Tackle(), Swift(), TailWhip()]

    def get_type(self) -> str :
        super().get_type()
        return self.type


class Rocky(Posmon) :                                               #Rocky 클래스 (Posmon 클래스를 상속받음)
    def __init__(self) :
        super().__init__()
        self.max_health = 80
        self.max_attack = 15
        self.max_defence = 25
        self.name = "Rocky"
        self.type = "Rock"
        self.skil = [Tackle(), Growl()]

    def get_type(self) -> str :
        super().get_type()
        return self.type


class Swania(Posmon) :                                              #Swania 클래스 (Posmon 클래스를 상속받음)
    def __init__(self) :
        super().__init__()
        self.max_health = 80
        self.max_attack = 30
        self.max_defence = 10
        self.name = "Swania"
        self.type = "Scissors"
        self.skil = [ScissorsCross(), SwordDance()]

    def get_type(self) -> str :
        super().get_type()
        return self.type


class Move :                                                        #포스몬의 기술(Move) 클래스
    def __init__(self, name) :
        self.name = name

    def get_name(self)->str :                                      # 기술의 이름을 반환하는 메서드
        return self.name 
    
    def get_speed(self)->int :                                     # 기술의 속도를 반환하는 메서드
        pass

    def use(self, our_posmon:Posmon, opponent_posmon:Posmon, is_player_move=True): 
        pass


class PhysicalMove(Move):                                           #PhysicalMove 클래스 (Move 클래스를 상속받음)
    
    def __init__(self, power, name):
        super().__init__(name)
        self.power = power

    def get_power(self) -> int :                                   # 이 기술의 위력을 반환하는 메서드
        return self.power
    
    def use(self, our_posmon:Posmon, opponent_posmon:Posmon, is_player_move=True): 
        if is_player_move :
            if (our_posmon.get_type() == "Scissors" and opponent_posmon.get_type() == "Paper") or (our_posmon.get_type() == "Rock" and opponent_posmon.get_type() == "Scissors") or (our_posmon.get_type() == "Paper" and opponent_posmon.get_type() == "Rock") :
                ratio = 2                                                                                       
            else :
                ratio = 1

            damage = max(0, self.power + our_posmon.get_attack() - opponent_posmon.get_defence())*ratio                #피해 계산식
            before = opponent_posmon.health                                                                        #피해를 입기 전 체력
            opponent_posmon.health -= damage
            after = opponent_posmon.health                                                                         #피해를 입은 후 체력
            print("- %s 포스몬의 [체력] %d 감소 (%d -> %d)" %(opponent_posmon.get_name(), damage, before, after))

        else :
            if (opponent_posmon.get_type() == "Scissors" and our_posmon.get_type() == "Paper") or (opponent_posmon.get_type() == "Rock" and our_posmon.get_type() == "Scissors") or (opponent_posmon.get_type() == "Paper" and our_posmon.get_type() == "Rock") :
                ratio = 2
            else :
                ratio = 1

            damage = max(0, self.power + opponent_posmon.get_attack() - our_posmon.get_defence())*ratio
            before = our_posmon.health
            our_posmon.health -= damage
            after = our_posmon.health
            print("- %s 포스몬의 [체력] %d 감소 (%d -> %d)" %(our_posmon.get_name(), damage, before, after))


class Tackle(PhysicalMove) :                                        #Tackle 클래스 (PhysicalMove 클래스를 상속받음)
    
    def __init__(self) :
        super().__init__(power=25, name="Tackle")

    def get_speed(self) :
        return 0
    

class ScissorsCross(PhysicalMove) :                                 #ScissorsCross 클래스 (PhysicalMove 클래스를 상속받음)
    
    def __init__(self) :
        super().__init__(power=30, name="ScissorsCross")

    def get_speed(self) :
        return 0
    

class Swift(PhysicalMove) :                                         #Swift 클래스 (PhysicalMove 클래스를 상속받음) 
    
    def __init__(self) :
        super().__init__(power=0, name = "Swift")
        

    def get_speed(self) :
        return 3


class StatusMove(Move):                                             #StatusMove 클래스 (Move 클래스를 상속받음)
    pass


class Growl(StatusMove):                                            #Growl 클래스 (StatusMove 클래스를 상속받음)

    def __init__(self, name = "Growl"):
        super().__init__(name)
        self.amount = 5

    def get_speed(self) :
        return 1
    
    def use(self, our_posmon:Posmon, opponent_posmon:Posmon, is_player_move=True) :
        if is_player_move :
            before = opponent_posmon.get_attack()
            opponent_posmon.attack -= self.amount
            after = opponent_posmon.get_attack()
            print("- %s 포스몬의 [공격력] %d 감소 (%d -> %d)" %(opponent_posmon.get_name(), self.amount, before, after))
        
        else :
            before = our_posmon.get_attack()
            our_posmon.attack -= self.amount
            after = our_posmon.get_attack()
            print("- %s 포스몬의 [공격력] %d 감소 (%d -> %d)" %(our_posmon.get_name(), self.amount, before, after))


class SwordDance(StatusMove):                                       #SwordDance 클래스 (StatusMove 클래스를 상속받음)                               

    def __init__(self, name = "SwordDance"):
        super().__init__(name)
        self.amount = 10

    def get_speed(self) :
        return 0
    
    def use(self, our_posmon:Posmon, opponent_posmon:Posmon, is_player_move=True) :
        if is_player_move :
            before = our_posmon.get_attack()
            our_posmon.attack += self.amount
            after = our_posmon.get_attack()
            print("- %s 포스몬의 [공격력] %d 증가 (%d ->%d)" %(our_posmon.get_name(), self.amount, before, after))

        else :
            before = opponent_posmon.get_attack()
            opponent_posmon.attack += self.amount
            after = opponent_posmon.get_attack()
            print("- %s 포스몬의 [공격력] %d 증가 (%d -> %d)" %(opponent_posmon.get_name(), self.amount, before, after))    


class TailWhip(StatusMove):                                         #TailWhip 클래스 (StatusMove 클래스를 상속받음)

    def __init__(self, name = "TailWhip"):
        super().__init__(name)
        self.amount = 5

    def get_speed(self) :
        return 1
    
    def use(self, our_posmon:Posmon, opponent_posmon:Posmon, is_player_move=True) :
        if is_player_move :
            before = opponent_posmon.get_defence()
            opponent_posmon.defence -= self.amount
            after = opponent_posmon.get_defence()
            print("- %s 포스몬의 [방어력] %d 감소 (%d -> %d)" %(opponent_posmon.get_name(), self.amount, before, after))
        
        else :
            before = our_posmon.get_defence()
            our_posmon.defence -= self.amount
            after = our_posmon.get_defence()
            print("- %s 포스몬의 [방어력] %d 감소 (%d -> %d)" %(our_posmon.get_name(), self.amount, before, after))


def player_choice_error_check(choice) :                                    #사용자로부터 잘못된 입력을 받은 경우 반복하는 함수
    while True :                                                          
        if len(choice) == 1 :
            if choice[0] == "e" :
                break
            else :
                print("잘못된 명령어:", choice)
        
        elif len(choice) == 3 :
            if choice[0] == "s" :
                try :
                    if (int(choice[2]) < 0 or int(choice[2]) > len(p_posmon_list) - 1) or int(choice[2]) == p_index_of_list or p_posmon_list[int(choice[2])].get_health == 0 :
                        print("포스몬을 교대시킬 수 없습니다!")
                    else :
                        break

                except ValueError :
                    print("잘못된 명령어:", choice)

            elif choice[0] == "o" :
                try :
                    if int(choice[2]) < 0 or int(choice[2]) > len(p_posmon_list[p_index_of_list].skil) - 1 :
                        print("선택할 수 없는 기술입니다!")
                    else :
                        break

                except ValueError :
                    print("잘못된 명령어:", choice)

            else :
                print("잘못된 명령어:", choice)

        else :
            print("잘못된 명령어:", choice)

        choice = input("입력: ")

    return choice


def player_skil(p_index_of_list, c_index_of_list, choice) :                #플레이어가 선택한 기술 클래스를 불러오는 함수
    if p_posmon_list[p_index_of_list].skil[int(choice[2])].get_name() == "Tackle" :
        Tackle().use(p_posmon_list[p_index_of_list], c_posmon_list[c_index_of_list])
    
    elif p_posmon_list[p_index_of_list].skil[int(choice[2])].get_name() == "ScissorsCross" :
        ScissorsCross().use(p_posmon_list[p_index_of_list], c_posmon_list[c_index_of_list])

    elif p_posmon_list[p_index_of_list].skil[int(choice[2])].get_name() == "Swift" :
        Swift().use(p_posmon_list[p_index_of_list], c_posmon_list[c_index_of_list])

    elif p_posmon_list[p_index_of_list].skil[int(choice[2])].get_name() == "Growl" :
        Growl().use(p_posmon_list[p_index_of_list], c_posmon_list[c_index_of_list])

    elif p_posmon_list[p_index_of_list].skil[int(choice[2])].get_name() == "SwordDance" :
        SwordDance().use(p_posmon_list[p_index_of_list], c_posmon_list[c_index_of_list])

    elif p_posmon_list[p_index_of_list].skil[int(choice[2])].get_name() == "TailWhip" :
        TailWhip().use(p_posmon_list[p_index_of_list], c_posmon_list[c_index_of_list])


def computer_skil(p_index_of_list, c_index_of_list, c_posmon_skil) :       #컴퓨터가 선택한 기술 클래스를 불러오는 함수
    if c_posmon_skil.get_name() == "Tackle" :
        Tackle().use(p_posmon_list[p_index_of_list], c_posmon_list[c_index_of_list], False)
    
    elif c_posmon_skil.get_name() == "ScissorsCross" :
        ScissorsCross().use(p_posmon_list[p_index_of_list], c_posmon_list[c_index_of_list], False)

    elif c_posmon_skil.get_name() == "Swift" :
        Swift().use(p_posmon_list[p_index_of_list], c_posmon_list[c_index_of_list], False)

    elif c_posmon_skil.get_name() == "Growl" :
        Growl().use(p_posmon_list[p_index_of_list], c_posmon_list[c_index_of_list], False)
    
    elif c_posmon_skil.get_name() == "SwordDance" :
        SwordDance().use(p_posmon_list[p_index_of_list], c_posmon_list[c_index_of_list], False)

    elif c_posmon_skil.get_name() == "TailWhip" :
        TailWhip().use(p_posmon_list[p_index_of_list], c_posmon_list[c_index_of_list], False)


while True :                                                               #게임 반복
    print("____     ___    _____ ___ ___   ___   ____")
    print("|    \  /   \  / ___/|   T   T /   \ |    \\")
    print("| o   )Y     Y(   \_ | _   _ |Y     Y|  _  Y")
    print("|   _/ |  O  | \__  T|  \_/  ||  O  ||  |  |")
    print("|  |   |     | / \  ||   |   ||     ||  |  |")
    print("|  |   l     ! \    ||   |   |l     !|  |  |")
    print("l__j    \___/   \___jl___j___j \___/ l__j__j")
    print("============================================")
    print("0. 포스몬 선택")
    print("1. 배틀하기")
    print("2. 종료하기")
    print("============================================")
    selected_menu = input("입력: ")                                       #초기 메뉴 선택 
    while True :                                                          #초기 메뉴에서 잘못된 입력을 받은 경우 다시 입력
        try : 
            if 0 <= int(selected_menu) <= 2 :
                break
            else :
                print("잘못된 입력입니다. 다시 입력하세요.")
                selected_menu = input("입력: ")

        except ValueError :
            print("잘못된 입력입니다. 다시 입력하세요.")
            selected_menu = input("입력: ")

    if int(selected_menu) == 0 :                                           #초기 메뉴에서 0을 입력받은 경우
        print("")

        p_posmon_list = []                                                 #나중에 선택된 포스몬을 넣을 빈 리스트
        p_name_print = ""

        for i in range(3) :
            print("============================================")
            print("당신이 사용할 포스몬을 선택하세요. 현재 %d 마리/최대 3 마리" %len(p_posmon_list))
            print("0. Ponix")
            print("1. Normie")
            print("2. Swania")
            print("3. Rocky")
            if i >= 1 :                                                           #두 번째 입력부터는 "-1.그만두기"를 출력
                print("-1. 그만두기")
            print("============================================")
            selected_posmon = input("입력: ")
            while True :                                                          #입력에서 잘못된 입력을 받은 경우 다시 입력
                try : 
                    if i == 0 :                                                   #첫 번째 입력인 경우, 0~3이 옳은 입력임
                        if 0 <= int(selected_posmon) <= 3 :
                            break
                        else :
                            print("잘못된 입력입니다. 다시 입력하세요.")
                            selected_posmon = input("입력: ")
                    else :
                        if -1 <= int(selected_posmon) <= 3 :
                            break
                        else :                                                   #두 번째 입력부터, -1~3이 옳은 입력임
                            print("잘못된 입력입니다. 다시 입력하세요.")
                            selected_posmon = input("입력: ")

                except ValueError :
                    print("잘못된 입력입니다. 다시 입력하세요.")
                    selected_posmon = input("입력: ")

            if selected_posmon == "0" :                                           #0을 입력받은 경우
                pm = Ponix()

            elif selected_posmon == "1" :                                           #1을 입력받은 경우
                pm = Normie()

            elif selected_posmon == "2" :                                           #2을 입력받은 경우
                pm = Swania()

            elif selected_posmon == "3" :                                           #3을 입력받은 경우
                pm = Rocky()

            elif selected_posmon == "-1" :                                           #-1을 입력받은 경우
                print("")
                break

            pm.reset_status(True)
            p_posmon_list.append(pm)                                                #리스트에 선택된 포스몬을 넣어줌
            p_name_print +=" %s" %pm.get_name()

            print("")

        print("============================================")
        print("당신의 포스몬 목록:%s" %p_name_print)
        print("============================================")
        print("")

    elif int(selected_menu) == 1 :                                           #초기 메뉴에서 1을 입력받은 경우
        print("")

        c_posmon_list = []                                                   #컴퓨터가 랜덤으로 선택한 포스몬을 넣을 빈 리스트
        c_name_print = ""

        for i in range(3) :                                                     #컴퓨터가 랜덤으로 가질 포스몬을 3마리 만들어줌
            c_pm = random.choice([Ponix(), Normie(), Rocky(), Swania()])
            c_pm.reset_status(True)
            c_posmon_list.append(c_pm)                                           #리스트에 컴퓨터가 랜덤으로 선택한 포스몬을 넣어줌
            c_name_print +=" %s" %c_pm.get_name()

        try :
            error_check = p_posmon_list[0].get_name()                                       #p_posmon_list가 정의되어있지 않으면 except의 문장을 수행
            print("============================================")
            print("당신의 포스몬 목록:%s" %p_name_print)
            print("컴퓨터 포스몬 목록:%s" %c_name_print) 
            print("============================================")

        except :
            print("싸울 포스몬이 없습니다! 먼저 포스몬을 선택해 주세요.")
            print("")
            continue

        c_index_of_list = 0                                                      #컴퓨터의 몇 번째 포스몬인가를 나타냄
        p_index_of_list = 0                                                        #플레이어의 몇 번째 포스몬인가를 나타냄
        turn = 1

        while True :
            
            if turn == 1 :                                                       #첫 번째 턴인 경우, "배틀이 시작됩니다."를 출력
                print("")
                print("배틀이 시작됩니다.") 
            turn += 1      

            print("############################################")

            c_Xor0 = ""                                                          #컴퓨터 포스몬의 생사여부를 결정해줄 변수
            c_live_count = 0                                                     #살아있는 컴퓨터 포스몬의 수
            for i in range(3) :
                if c_posmon_list[i].get_health() <= 0 :                          
                    c_Xor0 += "X"                                                #체력이 0이면 X
                else :
                    c_Xor0 += "0"                                                #체력이 0이 아니면 0
                    c_live_count += 1
            print("컴퓨터 포스몬: [%s] %d / 3" %(c_Xor0, c_live_count))

            for i in range(3) :
                if i == c_index_of_list :
                    print(f"{c_posmon_list[i].get_name():20}<|{c_posmon_list[i].get_type()} {c_posmon_list[i].get_health()} / {c_posmon_list[i].get_max_health()}|")
            
            print("                    VS")

            for i in range(len(p_posmon_list)) :
                if i == p_index_of_list :
                    print(f"{p_posmon_list[i].get_name():20}<|{p_posmon_list[i].get_type()} {p_posmon_list[i].get_health()} / {p_posmon_list[i].get_max_health()}|")
            
            p_Xor0 = ""                                                          #플레이어 포스몬의 생사여부를 결정해줄 변수
            p_live_count = 0                                                     #살아있는 플레이어 포스몬의 수
            for i in range(len(p_posmon_list)) :
                if p_posmon_list[i].get_health() <= 0 :
                    p_Xor0 += "X"                                                #체력이 0이면 X
                else :
                    p_Xor0 += "0"                                                #체력이 0이 아니면 0
                    p_live_count += 1
            print("당신의 포스몬: [%s] %d / %d" %(p_Xor0, p_live_count, len(p_posmon_list)))

            print("++++++++++++++++++++++++++++++++++++++++++++")

            p_skil_print = ""                                                     #프린트할 스킬들
            for i in range(len(p_posmon_list)) :
                if i == p_index_of_list :
                    for j in range(len(p_posmon_list[i].skil)) :
                        p_skil_print +=" (%d) %s" %(j, p_posmon_list[i].skil[j].get_name())
            print("기술:%s" %p_skil_print)
            print("############################################")

            if p_Xor0 == "X" or p_Xor0 == "XX" or p_Xor0 == "XXX" or c_Xor0 == "XXX" :                        #어느 한 쪽의 포스몬이 다 쓰러진 경우
                p_posmon_list = []
                print("")
                
                if c_Xor0 == "XXX" :                                                   #컴퓨터의 포스몬이 다 쓰러진 경우
                    print("[배틀 결과] 당신이 이겼습니다.")
                    print("")

                elif p_Xor0 == "X" or p_Xor0 == "XX" or p_Xor0 == "XXX" :              #플레이어의 포스몬이 다 쓰러진 경우
                    print("[배틀 결과] 컴퓨터가 이겼습니다.")
                    print("")

                break
            
            choice = input("입력: ")                                                     #사용자로부터 명령어를 입력 받음
            choice = player_choice_error_check(choice)
            print("############################################")

            while True :                                                          #플레이어나 컴퓨터의 포스몬이 다 죽을 때까지 반복
                if choice[0] == "e" :                                             #입력의 첫 번째 인덱스가 "e"인 경우
                    for i in range(len(p_posmon_list)) :
                        print(f"({i}) {p_posmon_list[i].get_name():8}<|{p_posmon_list[i].get_type()} {p_posmon_list[i].get_health()} / {p_posmon_list[i].get_max_health()}|")

                    print("")
                    choice = input("입력: ")
                    choice = player_choice_error_check(choice)
                    print("############################################")

                elif choice[0] == "o" :                                             #입력의 첫 번째 인덱스가 "o"인 경우
                    c_posmon_skil = random.choice(c_posmon_list[c_index_of_list].skil)
                    
                    if p_posmon_list[p_index_of_list].skil[int(choice[2])].get_speed() >= c_posmon_skil.get_speed() :    #플레이어 포스몬의 스킬이 더 빠른 경우
                        print("당신의 %s: %s 기술 사용" %(p_posmon_list[p_index_of_list].get_name(), p_posmon_list[p_index_of_list].skil[int(choice[2])].get_name()))
                        
                        player_skil(p_index_of_list, c_index_of_list, choice)                       

                        if c_posmon_list[c_index_of_list].get_health() > 0 :                                             #컴퓨터의 포스몬이 쓰러지지 않은 경우
                            print("컴퓨터 %s: %s 기술 사용" %(c_posmon_list[c_index_of_list].get_name(), c_posmon_skil.get_name()))
                            
                            computer_skil(p_index_of_list, c_index_of_list, c_posmon_skil)

                            if p_posmon_list[p_index_of_list].get_health() <= 0 :
                                print("당신의 %s: 쓰러짐" %p_posmon_list[p_index_of_list].get_name())
                                for i in range(len(p_posmon_list)) :
                                    if p_posmon_list[i].get_health() != 0 and p_index_of_list != i :
                                        p_index_of_list = i
                                        break
                                if p_posmon_list[p_index_of_list].get_health() > 0 :
                                    p_posmon_list[p_index_of_list].reset_status()                                 #교대할 포스몬의 공격력, 방어력을 초기화해줌
                                    print("당신의 %s로 교대" %p_posmon_list[p_index_of_list].get_name())

                        else :                                                                                          #컴퓨터 포스몬이 쓰러진 경우
                            print("컴퓨터 %s: 쓰러짐" %c_posmon_list[c_index_of_list].get_name())
                            if c_index_of_list < 2 :
                                c_index_of_list += 1  
                            if c_posmon_list[c_index_of_list].get_health() > 0 :
                                c_posmon_list[c_index_of_list].reset_status()  
                                print("컴퓨터 %s로 교대" %c_posmon_list[c_index_of_list].get_name())    
                    
                    else :                                                                                                #컴퓨터 포스몬의 스킬이 더 빠른 경우
                        print("컴퓨터 %s: %s 기술 사용" %(c_posmon_list[c_index_of_list].get_name(), c_posmon_skil.get_name()))
                        
                        computer_skil(p_index_of_list, c_index_of_list, c_posmon_skil)

                        if p_posmon_list[p_index_of_list].get_health() > 0 :                           #플레이어의 포스몬이 쓰러지지 않은 경우

                            print("당신의 %s: %s 기술 사용" %(p_posmon_list[p_index_of_list].get_name(), p_posmon_list[p_index_of_list].skil[int(choice[2])].get_name()))
                            
                            player_skil(p_index_of_list, c_index_of_list, choice)

                            if c_posmon_list[c_index_of_list].get_health() <= 0 :
                                print("컴퓨터 %s: 쓰러짐" %c_posmon_list[c_index_of_list].get_name())
                                if c_index_of_list < 2 :
                                    c_index_of_list += 1 
                                if c_posmon_list[c_index_of_list].get_health() > 0 :
                                    c_posmon_list[c_index_of_list].reset_status()   
                                    print("컴퓨터 %s로 교대" %c_posmon_list[c_index_of_list].get_name())

                        else :                                                                       #플레이어의 포스몬이 쓰러진 경우
                            print("당신의 %s: 쓰러짐" %p_posmon_list[p_index_of_list].get_name())
                            for i in range(len(p_posmon_list)) :
                                if p_posmon_list[i].get_health() != 0 and p_index_of_list != i :
                                    p_index_of_list = i
                                    break
                            if p_posmon_list[p_index_of_list].get_health() > 0 :
                                p_posmon_list[p_index_of_list].reset_status()
                                print("당신의 %s로 교대" %p_posmon_list[p_index_of_list].get_name())        

                    break

                elif choice[0] == "s" :                                             #입력의 첫 번째 인덱스가 "s"인 경우
                    p_index_of_list = int(choice[2])
                    p_posmon_list[p_index_of_list].reset_status()
                    print("당신의 포스몬 %s 로 교대" %p_posmon_list[p_index_of_list].get_name())

                    c_posmon_skil = random.choice(c_posmon_list[c_index_of_list].skil)
                    print("컴퓨터 %s: %s 기술 사용" %(c_posmon_list[c_index_of_list].get_name(), c_posmon_skil.get_name()))
                        
                    computer_skil(p_index_of_list, c_index_of_list, c_posmon_skil)

                    if p_posmon_list[p_index_of_list].get_health() <= 0 :                                              #플레이어의 포스몬이 쓰러진 경우
                        print("당신의 %s: 쓰러짐" %p_posmon_list[p_index_of_list].get_name())
                        for i in range(len(p_posmon_list)) :
                            if p_posmon_list[i].get_health() != 0 and p_index_of_list != i :
                                p_index_of_list = i
                                break
                        if p_posmon_list[p_index_of_list].get_health() > 0 :
                            p_posmon_list[p_index_of_list].reset_status()
                            print("당신의 %s로 교대" %p_posmon_list[p_index_of_list].get_name())        
                            
                    break

            print("")
                                  
    elif int(selected_menu) == 2 :                                           #초기 메뉴에서 2를 입력받은 경우
        break
    








    

