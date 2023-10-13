# 개발환경
# Python 3.11.0 (main, Oct 24 2022, 18:26:48)
# vscode 1.73.1 (user setup)
# windows 11 Home 64bit
# 조병하 2021136124

import msvcrt
import random
import time
import copy
import os

grid = list() # 맵
size_list = ["작음", "중간", "큼", "짱큼"]
map_size = {"작음" : 4, "중간" : 5, "큼" : 6, "짱큼" : 7} # 맵 크기 dict
dif = {"쉬움" : 0, "중간" : 1, "어려움" : 2, "극악" : 3} # 난이도 dict
dif_list = ["쉬움", "중간", "어려움", "극악"]

now_x = 0 # 현재위치(시작위치) 초기화
now_y = 0 # 현재위치(시작위치) 초기화

def Create_grid(n: int) -> None: # 크기에 따른 맵 생성
    global grid
    grid = [[" " for _ in range(n)] for _ in range(n)]

def Create_Start(x = 0, y = 0) -> None: # 시작지점 설정
    global grid
    grid[x][y] = "me"

def Create_Goal(n) -> None: # 도착지점 설정
    global grid
    grid[n - 1][n - 1] = "goal"

def Create_Hole(difficult: int, s: int) -> None:
    hole_num = [0.2, 0.3, 0.4, 0.5]
    hole_cnt = 0
    while hole_cnt < int(s*s*hole_num[difficult]):
        x = random.randrange(s)
        y = random.randrange(s)
        if not grid[x][y] == "hole" and not grid[x][y] == "goal" and not grid[x][y] == "me":
            grid[x][y] = "hole"
            hole_cnt += 1

def Delete_Hole(n: int) -> None:
    for x in range(n):
        for y in range(n):
            if grid[x][y] == "hole": grid[x][y] = " "

def find_root(n: int) -> bool:
    visited = []
    visited.append((0, 0))

    grid_test = copy.deepcopy(grid)

    while not len(visited) == 0:
        here = visited.pop()
        (x, y) = here
        if grid_test[x][y] == "goal": return True
        else:
            grid_test[x][y] = "me"
            if (x >= 0 and x < n and y - 1 >= 0 and y - 1 < n) and (grid_test[x][y - 1] == " " or grid_test[x][y - 1] == "goal"): visited.append((x, y - 1))
            if (x - 1 >= 0 and x - 1 < n and y >= 0 and y < n) and (grid_test[x - 1][y] == " " or grid_test[x - 1][y] == "goal"): visited.append((x - 1, y))
            if (x >= 0 and x < n and y + 1 >= 0 and y + 1 < n) and (grid_test[x][y + 1] == " " or grid_test[x][y + 1] == "goal"): visited.append((x, y + 1))
            if (x + 1 >= 0 and x + 1 < n and y >= 0 and y < n) and (grid_test[x + 1][y] == " " or grid_test[x + 1][y] == "goal"): visited.append((x + 1, y))

    return False

def getKey() -> str:
    buf = msvcrt.getch()
    if list(buf) == [224]:
        a = list(msvcrt.getch())[0]
        if a == 72: return "up"
        elif a == 75: return "left"
        elif a == 77: return "right"
        elif a == 80: return "down"
    elif list(buf) == [13]:
        return "enter"

def getKey_random() -> str:
    retValue = ["up", "down", "left", "right"]
    return retValue[random.randrange(0, 4)]

def move(direction: str, n: int) -> None:
    global now_y
    global now_x
    if direction == "up":
        if now_y >= 1: now_y -= 1
    elif direction == "down":
        if now_y < n: now_y += 1
    elif direction == "right":
        if now_x < n: now_x += 1
    elif direction == "left":
        if now_x >= 1: now_x -= 1
    elif direction == None: pass

def change_position(n: int) -> str:
    global grid
    ret = "None"
    for x in range(n):
        for y in range(n):
            if grid[x][y] == "me": grid[x][y] = " "

    if grid[now_y][now_x] == "hole":
        grid[now_y][now_x] = "die"
        ret = "Game Over"
    elif grid[now_y][now_x] == "goal":
        grid[now_y][now_x] = "clear"
        ret = "Game Clear"
    elif grid[now_y][now_x] == " ":
        grid[now_y][now_x] = "me"

    return ret

def print_grid(diff: str, gm: int, grid_s: int) -> None:
    os.system("cls")
    gm_list = ["직접 플레이", "직접 플레이(시간 측정)", "랜덤 입력"]
    print(f"난이도: {diff} / 게임모드: {gm_list[gm]} / 맵 크기 {grid_s} x {grid_s}")
    print()
    print("  " + "🧱" * (6 * grid_s + 1))
    for x in grid:
        print("  🧱  ", end = "")
        for item in x:
            if item == " ":
                print("      ", end = "")
            elif item == "hole":
                print("      ", end = "")
            elif item == "goal":
                print("      ", end = "")
            elif item == "me":
                print("      ", end = "")
            elif item == "die":
                print("      ", end = "")
            elif item == "clear":
                print("      ", end = "")
            print("  🧱  ", end = "")
        print()
        print("  🧱  ", end = "")
        for item in x:
            if item == " ":
                print("      ", end = "")
            elif item == "hole":
                print("☣    ☣", end = "")
            elif item == "goal":
                print("💊  💊", end = "")
            elif item == "me":
                print("  😷  ", end = "")
            elif item == "die":
                print("  😵  ", end = "")
            elif item == "clear":
                print("  😄  ", end = "")
            print("  🧱  ", end = "")
        print()
        print("  🧱  ", end = "")
        for item in x:
            if item == " ":
                print("      ", end = "")
            elif item == "hole":
                print("  🦠  ", end = "")
            elif item == "goal":
                print("  💉  ", end = "")
            elif item == "me":
                print("👋🥼🤜", end = "")
            elif item == "die":
                print("☠ 🥋 ☠", end = "")
            elif item == "clear":
                print("👋🥼🤳", end = "")
            print("  🧱  ", end = "")
        print()
        print("  🧱  ", end = "")
        for item in x:
            if item == " ":
                print("      ", end = "")
            elif item == "hole":
                print("☣    ☣", end = "")
            elif item == "goal":
                print("💊  💊", end = "")
            elif item == "me":
                print(" 👞👞 ", end = "")
            elif item == "die":
                print(" ☠  ☠ ", end = "")
            elif item == "clear":
                print(" 👞👞 ", end = "")
            print("  🧱  ", end = "")
        print()
        print("  🧱  ", end = "")
        for item in x:
            if item == " ":
                print("      ", end = "")
            elif item == "hole":
                print("      ", end = "")
            elif item == "goal":
                print("      ", end = "")
            elif item == "me":
                print("      ", end = "")
            elif item == "die":
                print("      ", end = "")
            elif item == "clear":
                print("      ", end = "")
            print("  🧱  ", end = "")
        print()
        print("  " + "🧱" * (6 * grid_s + 1))

def print_clear():
    print('''              
                                                  
                           .                                                                                                                            .                    
                ~          . :     ~                                                                                                         ~          . :     ~            
                           . :    .                                                                                                                     . :    .             
               . *      .! . -   *$                                                                                                         . *      .! . -   *$             
                  ,      ~ , .   .,                                                                                                            ,      ~ , .   .,             
                , * ,      -    ~:                                                                                                           , * ,      -    ~:              
                 = ~       ~    ==                                                                                                            = ~       ~    ==              
                 !!=       !~   ,     ;                                                                                                       !!=       !~   ,     ;         
                  $ ,    .-:;  ;:    $                                                                                                         $ ,    .-:;  ;:    $          
                  .$*    !;;!  =!   ! .                                                                                                        .$*    !;;!  =!   ! .         
         -         *~    $::*  -.  ,-        ~                                                                                        -         *~    $::*  -.  ,-        ~  
          *~       -*;   =*,! .;   $      .!;                                                                                          *~       -*;   =*,! .;   $      .!;   
            #     . !;   :;,! ;;  *      =$                                                                                              #     . !;   :;,! ;;  *      =$     
          .  !:     !;;, .:~~ ;. -~.   :=~                                                                                             .  !:     !;;, .:~~ ;. -~.   :=~      
      ;:. . ...=     =!--~~~~ :  *    *=                                                                                           ;:. . ...=     =!--~~~~ :  *    *=        
         *$   $.=    .;; ~~:. ; ~    *=                                                                                               *$   $.=    .;; ~~:. ; ~    *=         
           ,$- -!;..  !;  ~: ,, :  .*-      ;!-                                                                                         ,$- -!;..  !;  ~: ,, :  .*-      ;!- 
             .*, !-,  .*~ ;- : ~  =!:    ;*~        _____   ___  ___  ___ _____   _____  _      _____   ___  ______  _  _                 .*, !-,  .*~ ;- : ~  =!:    ;*~    
                ;.~-,  -=.~- -.  *;,  ~=;          |  __ \ / _ \ |  \/  ||  ___| /  __ \| |    |  ___| / _ \ | ___ \| || |                   ;.~-,  -=.~- -.  *;,  ~=;       
                  - ;~,~#;,~ .. !,.=**,            | |  \// /_\ \| .  . || |__   | /  \/| |    | |__  / /_\ \| |_/ /| || |                     - ;~,~#;,~ .. !,.=**,         
   ;!*==;-.        ..-,-:$--,-,:,*::,  .           | | __ |  _  || |\/| ||  __|  | |    | |    |  __| |  _  ||    / | || |      ;!*==;-.        ..-,-:$--,-,:,*::,  .        
           ,;;*;*=*, ,.--!,-. ~-:--                | |_\ \| | | || |  | || |___  | \__/\| |____| |___ | | | || |\ \ |_||_|              ,;;*;*=*, ,.--!,-. ~-:--             
                -~.-:~ ..,~, ,-.-:*$#$*$=;          \____/\_| |_/\_|  |_/\____/   \____/\_____/\____/ \_| |_/\_| \_|(_)(_)                   -~.-:~ ..,~, ,-.-:*$#$*$=;      
       -!$#$$#=!!~-,,.,,.,--:*,::!:.,..                                                                                             -!$#$$#=!!~-,,.,,.,--:*,::!:.,..         
     .-.          , ---.-,-~= :~::;;;*##:                                                                                         .-.          , ---.-,-~= :~::;;;*##:       
             -;*!;:::=*;:~,-!$.                                                                                                           -;*!;:::=*;:~,-!$.                 
         .**~.  ;=:,* -=~:: ;*=!                                                                                                      .**~.  ;=:,* -=~:: ;*=!                
        !     $!    -!#.*-!  $ ~#                                                                                                    !     $!    -!#.*-!  $ ~#               
             ,    ,$=.,# $.   = .#                                                                                                        ,    ,$=.,# $.   = .#              
                 ;#: *#  #    ;.  =                                                                                                           ;#: *#  #    ;.  =             
                =$   ~  .-~    @                                                                                                             =$   ~  .-~    @                
               !=    :  ~      .                                                                                                            !=    :  ~      .                
               :        #       -                                                                                                           :        #       -               
                        =                                                                                                                            =                       
    ''')

def print_die():
    print('''
                uuuuuuu                                                                                                      uuuuuuu                    
             uu$$$$$$$$$$$uu                                                                                              uu$$$$$$$$$$$uu               
          uu$$$$$$$$$$$$$$$$$uu                                                                                        uu$$$$$$$$$$$$$$$$$uu            
         u$$$$$$$$$$$$$$$$$$$$$u                                                                                      u$$$$$$$$$$$$$$$$$$$$$u           
        u$$$$$$$$$$$$$$$$$$$$$$$u                                                                                    u$$$$$$$$$$$$$$$$$$$$$$$u          
       u$$$$$$$$$$$$$$$$$$$$$$$$$u                                                                                  u$$$$$$$$$$$$$$$$$$$$$$$$$u         
       u$$$$$$$$$$$$$$$$$$$$$$$$$u                                                                                  u$$$$$$$$$$$$$$$$$$$$$$$$$u         
       u$$$$$$"   "$$$"   "$$$$$$u                                                                                  u$$$$$$"   "$$$"   "$$$$$$u         
       "$$$$"      u$u       $$$$"                                                                                  "$$$$"      u$u       $$$$"         
        $$$u       u$u       u$$$            __   __ _____  _   _  ______  _____  _____ ______                       $$$u       u$u       u$$$          
        $$$u      u$$$u      u$$$            \ \ / /|  _  || | | | |  _  \|_   _||  ___||  _  \                      $$$u      u$$$u      u$$$          
         "$$$$uu$$$   $$$uu$$$$"              \ V / | | | || | | | | | | |  | |  | |__  | | | |                       "$$$$uu$$$   $$$uu$$$$"           
          "$$$$$$$"   "$$$$$$$"                \ /  | | | || | | | | | | |  | |  |  __| | | | |                        "$$$$$$$"   "$$$$$$$"            
            u$$$$$$$u$$$$$$$u                  | |  \ \_/ /| |_| | | |/ /  _| |_ | |___ | |/ /  _  _  _                  u$$$$$$$u$$$$$$$u              
             u$"$"$"$"$"$"$u                   \_/   \___/  \___/  |___/   \___/ \____/ |___/  (_)(_)(_)                  u$"$"$"$"$"$"$u               
  uuu        $$u$ $ $ $ $u$$       uuu                                                                         uuu        $$u$ $ $ $ $u$$       uuu     
 u$$$$        $$$$$u$u$u$$$       u$$$$                                                                       u$$$$        $$$$$u$u$u$$$       u$$$$    
  $$$$$uu      "$$$$$$$$$"     uu$$$$$$                                                                        $$$$$uu      "$$$$$$$$$"     uu$$$$$$    
u$$$$$$$$$$$uu    """""    uuuu$$$$$$$$$$                                                                    u$$$$$$$$$$$uu    """""    uuuu$$$$$$$$$$  
$$$$"""$$$$$$$$$$uuu   uu$$$$$$$$$"""$$$"                                                                    $$$$"""$$$$$$$$$$uuu   uu$$$$$$$$$"""$$$"  
 """      ""$$$$$$$$$$$uu ""$"""                                                                              """      ""$$$$$$$$$$$uu ""$"""           
           uuuu ""$$$$$$$$$$uuu                                                                                         uuuu ""$$$$$$$$$$uuu            
  u$$$uuu$$$$$$$$$uu ""$$$$$$$$$$$uuu$$$                                                                       u$$$uuu$$$$$$$$$uu ""$$$$$$$$$$$uuu$$$   
  $$$$$$$$$$""""           ""$$$$$$$$$$$"                                                                      $$$$$$$$$$""""           ""$$$$$$$$$$$"  
   "$$$$$"                      ""$$$$""                                                                        "$$$$$"                      ""$$$$""   
     $$$"                         $$$$"                                                                           $$$"                         $$$$"    
    ''')

def print_start():
    print('''

       _      _____ ______  _____ ______   _    _  _____ ______ ______   _____   ___  ___  ___ _____      _    
    /\| |/\  |  __ \| ___ \|_   _||  _  \ | |  | ||  _  || ___ \|  _  \ |  __ \ / _ \ |  \/  ||  ___|  /\| |/\ 
    \ ` ' /  | |  \/| |_/ /  | |  | | | | | |  | || | | || |_/ /| | | | | |  \// /_\ \| .  . || |__    \ ` ' / 
   |_     _| | | __ |    /   | |  | | | | | |/\| || | | ||    / | | | | | | __ |  _  || |\/| ||  __|  |_     _|
    / , . \  | |_\ \| |\ \  _| |_ | |/ /  \  /\  /\ \_/ /| |\ \ | |/ /  | |_\ \| | | || |  | || |___   / , . \ 
    \/|_|\/   \____/\_| \_| \___/ |___/    \/  \/  \___/ \_| \_||___/    \____/\_| |_/\_|  |_/\____/   \/|_|\/ 
                                                                                                            


    ''')

os.system("cls")

start_idx = 1

while True:

    list_1 = ["> start", "  quit"]
    list_2 = ["  start", "> quit"]
    get_list = [list_2, list_1]

    print_start()
    print(f'''
                                                     {get_list[start_idx][0]}
                                                     {get_list[start_idx][1]}
    ''')

    key_buf = getKey()
    if key_buf == "down":
        if start_idx == 1: start_idx = 0
        os.system("cls")
    elif key_buf == "up":
        if start_idx == 0: start_idx = 1
        os.system("cls")
    elif key_buf == "enter":
        break
    else:
        os.system("cls")

while start_idx:

    os.system("cls")

    now_x = 0
    now_y = 0

    while True:
        input_mapSize = 0

        while True:
            print_start()
            print("맵 크기 선택)")
            list_1 = ["> 작음", "  중간", "  큼", "  짱큼"]
            list_2 = ["  작음", "> 중간", "  큼", "  짱큼"]
            list_3 = ["  작음", "  중간", "> 큼", "  짱큼"]
            list_4 = ["  작음", "  중간", "  큼", "> 짱큼"]
            get_list = [list_1, list_2, list_3, list_4]

            print(f'''
{get_list[input_mapSize][0]}
{get_list[input_mapSize][1]}
{get_list[input_mapSize][2]}
{get_list[input_mapSize][3]}
            ''')

            key_buf = getKey()
            if key_buf == "down":
                input_mapSize += 1
                os.system("cls")
            elif key_buf == "up":
                input_mapSize -= 1
                os.system("cls")
            elif key_buf == "enter":
                break
            else:
                os.system("cls")

            if input_mapSize < 0: input_mapSize = 0
            elif input_mapSize > 3: input_mapSize = 3

            os.system("cls")

        input_mapSize = size_list[input_mapSize]
        Create_grid(map_size[input_mapSize])
        break

    os.system("cls")

    while True:

        input_dif = 0

        while True:
            print_start()
            print(f"난이도를 입력하시오. (현재 맵 크기: {input_mapSize})")
            list_1 = ["> 쉬움", "  중간", "  어려움", "  극악"]
            list_2 = ["  쉬움", "> 중간", "  어려움", "  극악"]
            list_3 = ["  쉬움", "  중간", "> 어려움", "  극악"]
            list_4 = ["  쉬움", "  중간", "  어려움", "> 극악"]
            get_list = [list_1, list_2, list_3, list_4]

            print(f'''
{get_list[input_dif][0]}
{get_list[input_dif][1]}
{get_list[input_dif][2]}
{get_list[input_dif][3]}
            ''')

            key_buf = getKey()
            if key_buf == "down":
                input_dif += 1
                os.system("cls")
            elif key_buf == "up":
                input_dif -= 1
                os.system("cls")
            elif key_buf == "enter":
                break
            else:
                os.system("cls")

            if input_dif < 0: input_dif = 0
            elif input_dif > 3: input_dif = 3

            os.system("cls")

        n = input_dif
        break

    os.system("cls")

    while True:

        gameMode = 0

        while True:
            print_start()
            print(f"게임 모드를 선택하시오. (맵 크기: {input_mapSize} / 난이도: {dif_list[input_dif]})")
            list_1 = ["> 직접 플레이", "  직접 플레이(시간 측정)", "  랜덤 입력"]
            list_2 = ["  직접 플레이", "> 직접 플레이(시간 측정)", "  랜덤 입력"]
            list_3 = ["  직접 플레이", "  직접 플레이(시간 측정)", "> 랜덤 입력"]
            get_list = [list_1, list_2, list_3]

            print(f'''
{get_list[gameMode][0]}
{get_list[gameMode][1]}
{get_list[gameMode][2]}
            ''')

            key_buf = getKey()
            if key_buf == "down":
                gameMode += 1
                os.system("cls")
            elif key_buf == "up":
                gameMode -= 1
                os.system("cls")
            elif key_buf == "enter":
                os.system("cls")
                print('''
2019년 겨울....
한 바이러스가 나타나 전 세계를 뒤흔드는데....
그 이름은 COVID-19 !!!
COVID-19의 위험이 가득한 도시에서 백신을 찾아 떠나는 사람들...
과연 무사히 백신을 찾을 수 있을까...?
                ''')
                time.sleep(1)
                print("다음(아무 키 입력)")
                os.system("pause > null")
                break
            else:
                os.system("cls")

            if gameMode < 0: gameMode = 0
            elif gameMode > 2: gameMode = 2

            os.system("cls")

        break

    os.system("cls")

    Create_Start()
    Create_Goal(map_size[input_mapSize])
    while True:
        Delete_Hole(map_size[input_mapSize])
        Create_Hole(n, map_size[input_mapSize])
        if find_root(map_size[input_mapSize]): break

    os.system("cls")
    print_grid(dif_list[input_dif], gameMode, map_size[input_mapSize])

    ret_val = None
    start_time = None
    end_time = None
    
    while True:
        if gameMode == 0:
            move(getKey(), map_size[input_mapSize])
        elif gameMode == 2:
            move(getKey_random(), map_size[input_mapSize])
            time.sleep(0.5)
        elif gameMode == 1:
            if start_time == None: start_time = time.time()
            move(getKey(), map_size[input_mapSize])

        val = change_position(map_size[input_mapSize])
        print_grid(dif_list[input_dif], gameMode, map_size[input_mapSize])
        if val == "Game Over":
            
            if end_time == None: end_time = time.time()
            print_die()
            if gameMode == 1: print(f"기록: {round(end_time - start_time, 3)}s")
            os.system("pause")
            os.system("cls")
            
            while True:

                end_val = 0

                while True:
            
                    print("다시 시작하시겠습니까?")
                    list_1 = ["> 네 ", "  아니요"]
                    list_2 = ["  네 ", "> 아니요"]
                    get_list = [list_1, list_2]

                    print(f'''
{get_list[end_val][0]}
{get_list[end_val][1]}
                    ''')

                    key_buf = getKey()
                    if key_buf == "down":
                        end_val += 1
                        os.system("cls")
                    elif key_buf == "up":
                        end_val -= 1
                        os.system("cls")
                    elif key_buf == "enter":
                        os.system("cls")
                        break
                    else:
                        os.system("cls")

                    if end_val < 0: end_val = 0
                    elif end_val > 1: end_val = 1

                    os.system("cls")

                re = ["네", "아니요"]
                re_val = re[end_val]
                break
            break
        elif val == "Game Clear":

            if end_time == None: end_time = time.time()
            print_clear()
            if gameMode == 1: print(f"기록: {round(end_time - start_time, 3)}s")
            os.system("pause")
            os.system("cls")
            while True:
                end_val = 0

                while True:
            
                    print("새로운 게임을 시작하시겠습니까?")
                    list_1 = ["> 네 ", "  아니요"]
                    list_2 = ["  네 ", "> 아니요"]
                    get_list = [list_1, list_2]

                    print(f'''
{get_list[end_val][0]}
{get_list[end_val][1]}
                    ''')

                    key_buf = getKey()
                    if key_buf == "down":
                        end_val += 1
                        os.system("cls")
                    elif key_buf == "up":
                        end_val -= 1
                        os.system("cls")
                    elif key_buf == "enter":
                        os.system("cls")
                        break
                    else:
                        os.system("cls")

                    if end_val < 0: end_val = 0
                    elif end_val > 1: end_val = 1

                    os.system("cls")

                re = ["네", "아니요"]
                re_val = re[end_val]
                break
            break
    
    if re_val == "아니요": start_idx = 0