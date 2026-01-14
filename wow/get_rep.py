import time
import TOOLS_COMMON as common
from pynput import mouse


def main():
    print("请输入你的羽毛或者项链的数量")
    count = common.input_digital()
    
    print("5秒钟后开始自动获取声望")
    time.sleep(5)
    
    获取声望(int(count))

    print("执行完成！！")


def 获取声望(yumao_count):
    # 身影重叠NPC

    times = yumao_count // 5

    # print("现在是和人对话的状态：")
    quest_people= (1282, 795)
    kingblood = (247, 700)
    kingblood = (173, 487)

    continue_button = (145, 895)
    complete_button = continue_button

    for i in range(times):
        mouse1 = mouse.Controller()

        common.click_once_right(mouse1, quest_people, 1.5)
        common.click_once(mouse1, kingblood, .5)
        common.click_once(mouse1, continue_button, .5)
        common.click_once(mouse1, complete_button, 3)


if __name__ == '__main__':
    main()