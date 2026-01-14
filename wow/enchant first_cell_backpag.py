import time

import TOOLS_COMMON as common
from pynput import mouse

def main():

    print("请输入你要附魔包裹第一格子多少次")
    print("附魔前，要打开人物栏和包裹栏")
    count = common.input_digital()
    
    print("5秒钟后开始自动附魔包裹第一格子")
    time.sleep(5)
    
    附魔包裹第一格子(int(count))

    print("执行完成！！")


def 附魔包裹第一格子(times):
    fumo_button = (381, 893)
    confirm_position = (1197, 315)

    first_package_cell_position = (2155, 853)

    for i in range(times):
        mouse1 = mouse.Controller()

        common.click_once(mouse1,fumo_button,.5)
        common.click_once(mouse1,first_package_cell_position,1)
        common.click_once(mouse1,confirm_position,6)


if __name__ == '__main__':
    main()