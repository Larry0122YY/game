import time

import TOOLS_COMMON as common
from pynput import mouse

def main():

    print("做药前，要打开炼金栏，鼠标放到做药按钮上(这个脚本本质上只是点鼠标左键)")
    print()
    print("请输入你要做多少个药水")
    count = common.input_digital()
    
    print("5秒钟后开始自动做药水")
    time.sleep(5)
    
    附魔做药(int(count))

    print("执行完成！！")


def 附魔做药(count_times):
    mouse1 =mouse.Controller()

    # 鼠标左键点一下
    for i in range(count_times):
        mouse1.click(mouse.Button.left, 1)
        time.sleep(6)


if __name__ == '__main__':
    main()