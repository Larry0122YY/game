import time

import TOOLS_COMMON as common
from pynput import mouse

def main():
    
    print("附魔前，要打开附魔栏，鼠标放到附魔按钮上(这个脚本本质上只是点鼠标左键)")
    print()
    print("请输入你要附魔做多少个魔杖")
    print("\t※次级魔法杖，可以到95")
    print("\t※强效魔法杖，可以到130")
    count = common.input_digital()
    
    print("5秒钟后开始自动附魔做魔杖")
    time.sleep(5)
    
    附魔做魔杖(int(count))

    print("执行完成！！")


def 附魔做魔杖(count_times):
    mouse1 = mouse.Controller()

    # 鼠标左键点一下
    for i in range(count_times):
        mouse1.click(mouse.Button.left, 1)
        time.sleep(11)


if __name__ == '__main__':
    main()