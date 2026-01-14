import subprocess, sys, time
from pynput import mouse
from pynput.mouse import Controller
import win32api


# --------------------------------------fgo---------------------------------------------

def run_shell_cmn(x_location,y_location,delay):
    cmd = f'adb shell input tap {x_location} {y_location}'
    run_shell(cmd)
    time.sleep(delay)


def servant_buff(servant_num,skill_num,delay=3.5):
    # 因为3个从者的9个技能都是在一个y轴上的，都是700，所以只需要保留x坐标就行了
    y_location = 700
    servant_buff_x_location = [
        ['这个主要是为了让num不是从0开始。。。。'],
        [0,270,360,480],
        [0,660,760,880],
        [0,1070,1160,1270]
    ]
    x_location = servant_buff_x_location[servant_num][skill_num]

    run_shell_cmn(x_location,y_location,delay)


def servant_buff_target(servant_num,skill_num,target_num,delay=3.5):
    # 点击的哪个技能会有目标指向？
    servant_buff(servant_num,skill_num,delay=1)

    y_location = 500
    servant_target_x_location = [
        0,
        800,
        1150,
        1550
    ]
    x_location = servant_target_x_location[target_num]

    run_shell_cmn(x_location,y_location,delay)
    

def master_buff(buff_number,delay=3.5):

    y_location = 400
    # 御主技能的菱形按钮是2040
    master_buff_x_location = [2040,1685,1785,1885]
    run_shell_cmn(master_buff_x_location[0],y_location,.8)

    x_location = master_buff_x_location[buff_number]
    run_shell_cmn(x_location,y_location,delay)
    

def master_buff_target(buff_number,target_num,delay=3.5):
    # 点击的哪个技能会有目标指向？
    master_buff(buff_number,1)

    y_location = 500
    servant_target_x_location = [
        0,
        800,
        1150,
        1550
    ]
    x_location = servant_target_x_location[target_num]

    run_shell_cmn(x_location,y_location,delay)


def master_buff_sub_off(qian3,hou3):
    
    master_buff(3,.8)
    y_location = 450
    servant_6_location = [
        # 为了从1开始
        0,
        # servant 1
        540,
        # servant 2
        780,
        # servant 3
        1040,
        # servant 4
        1260,
        # servant 5
        1560,
        # servant 6
        1800
    ]

    run_shell_cmn(servant_6_location[qian3],y_location,.8)
    run_shell_cmn(servant_6_location[hou3],y_location,.8)

    sub_off_button = (1150,780)
    run_shell_cmn(sub_off_button[0],sub_off_button[1],4.5)


def push_attack_button():
    # 按攻击按钮
    attck_location = (1950,750)
    run_shell_cmn(attck_location[0],attck_location[1],.8)


def baoju_card(baoju_num,delay=.8):

    y_location = 240
    baoju_x_location = [0,870,1160,1470]
    x_locaiton = baoju_x_location[baoju_num]
    run_shell_cmn(x_locaiton,y_location,delay)


def rbg_card(card_num,delay=.8):

    y_location = 600

    cards_x_location = [
        0,
        # 第1张卡
        520,
        # 第2张卡
        870,
        # 第3张卡
        1160,
        # 第4张卡
        1470,
        # 第5张卡
        1820
    ]

    # 点击那5张攻击的红蓝绿卡
    run_shell_cmn(cards_x_location[card_num],y_location,delay)


def score_screen(if_continue):
    
    # 点击下一步，如果升级的画，也点这个就行，10秒循环点
    next_step_location = (1732,820)

    for i in range(13):
        run_shell_cmn(next_step_location[0],next_step_location[1],1)

    if if_continue:
    # 连续出击的情况
        # 点击连续出击
        continue_attack_button = (1420,740)
        run_shell_cmn(continue_attack_button[0],continue_attack_button[1],2)

        # 选择助战，就选当前画面的第一个
        zhuzhan = (1100,350)
        run_shell_cmn(zhuzhan[0],zhuzhan[1],10)
    else:
    # 回到home的情况
        # 点击关闭
        close_button = (900,740)
        run_shell_cmn(close_button[0],close_button[1],.5)


def main_method(rounds,rounds_name):

    print(f'请输入一个这次脚本使用多少体力？，如果直接回车，不算体力了，默认循环7次。')
    Energys_use = input()

    if Energys_use == '':
        times = 7
    elif not Energys_use.isdigit():
        print('您输入的不是数字，程序结束')
        sys.exit(1)
    else:
        print(f'此本单次的体力消耗是多少？')
        count_total = input_digital()
        
        if count_total == '' or not count_total.isdigit():
            print('您输入的不是数字，程序结束')
            sys.exit(1)

        times = int(int(Energys_use) / int(count_total))

    exe_frame(fgo_main_method,rounds_name,rounds,times)


def fgo_main_method(rounds,times):

    if_continue = True
    for i in range(times):
        # 如果只跑一次的话，不需要循环
        if times == 1:
            if_continue = False
        
        # 最后一个循环的时候，也不需要再来了
        if i == times - 1:
            if_continue = False
        
        print(f'现在进度：{i+1}/{times}')
            
        rounds(if_continue)

# --------------------------------------wow---------------------------------------------

def click_once(mouse1,position,delay):
    win32api.SetCursorPos(position)
    time.sleep(.5)
    mouse1.click(mouse.Button.left, 1)
    time.sleep(delay)

def click_once_right(mouse1,position,delay):
    win32api.SetCursorPos(position)
    time.sleep(.5)
    mouse1.click(mouse.Button.right, 1)
    time.sleep(delay)


# --------------------------------------auto---------------------------------------------




# --------------------------------------common---------------------------------------------


# 执行batch的方法
def run_shell(cmd_list, if_thread=False):
    if isinstance(cmd_list, str):
        cmd = cmd_list
    else:
        cmd = " && ".join(cmd_list)
    rw = None
    if if_thread:
        subprocess.run(cmd, shell=True)
    else:
        # For interactive scripts (with input()), use subprocess.run to allow real-time output and input
        # This ensures print statements and input() work correctly
        result = subprocess.run(cmd, shell=True)
        rw = str(result.returncode)

    return rw


# 这个方法只能输入数字
def input_digital():
    while True:
        select = input()
        if select.isdigit():
            return select
        print("请输入数字～～")
        time.sleep(1)
        print("请重新输入")


# 这个方法可以输入数字或直接回车返回空字符串
def input_digital_or_none():
    select = input()
    if select == '' or select.isdigit():
        return select
    print("请输入数字或直接回车～～")
    time.sleep(1)
    print("请重新输入")
    return input_digital_or_none()


# 获取鼠标位置（持续打印）
def get_mouse_position():
    mouse_controller = Controller()
    try:
        while True:
            print(f"{mouse_controller.position}")
            time.sleep(1)
    except KeyboardInterrupt:
        print("程序已退出。")


def exe_frame(method,script_name,rounds,times):

    print(f'{script_name}脚本开始运行！')
    time_start = time.perf_counter()

    # 执行方法代码
    method(rounds,times)

    print(f'{script_name}自动化脚本运行结束')
    time_end = time.perf_counter()

    time_cost = time_end - time_start
    cost_min = int(time_cost//60)
    cost_sec = time_cost % 60

    avg_cost_min = int(cost_min / times)
    avg_cost_sec = cost_sec % times
    print(f'花费时间：{cost_min}分{cost_sec:.2f}秒')
    print(f'平均每个rounds的时间：{avg_cost_min}分{avg_cost_sec:.2f}秒')
