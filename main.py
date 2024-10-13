# 导入模块
from PIL import Image,ImageTk
import tkinter as tk
import os
from character import *
from weapon import *

# 从文件中读取版本信息
f = open("resource/version.config","r",encoding = "UTF-8")
version = f.readline().strip('\n')
f.close()

# 定义启动函数
def way1():
    window.destroy()
    creatWindow_cu()
    creatWindow()
def way2():
    window.destroy()
    creatWindow_wu()
    creatWindow()
def way3():
    print("正在建设")
def way4():
    print("正在建设")
def website():
    os.system("start https://mc.kurogame.com/")

# 定义绘制窗口函数
def creatWindow():
    # 创建tk窗口
    global window
    window = tk.Tk()

    # 设置窗口基本信息
    window.title("抽卡模拟器")
    window.geometry("1280x760+5+5")
    window.resizable(False, False)
    window.iconbitmap("resource/titleicon.ico")

    # 绘制背景图
    bg_img = ImageTk.PhotoImage(Image.open("resource/bg.png"))
    tk.Label(window, image=bg_img).pack(anchor="center")

    # 显示版本号信息
    tk.Label(window, text = "当前角色: {0}\n当前武器: {1}\n版本: {2}".format(five_star_cu[0],five_star_wu[0],version),
            font = ("文鼎方新书H7GBK_H",14), bg = "black", justify = "left",width=18, 
            fg = "white").place(x = 1280, y = 760, anchor = "se")

    # 绘制按钮
    tk.Button(window, text = "角色活动唤取", font = ("文鼎方新书H7GBK_H",16), 
            bg = "grey", fg = "white", width = 12, cursor = "hand2",
            command = way1).place(x = 1060, y = 570, anchor = "se")

    tk.Button(window, text = "武器活动唤取", font = ("文鼎方新书H7GBK_H",16), 
            bg = "grey", fg = "white", width = 12, cursor = "hand2",
            command = way2).place(x = 1240, y = 570, anchor = "se")

    tk.Button(window, text = "常驻角色唤取", font = ("文鼎方新书H7GBK_H",16), 
            bg = "grey", fg = "white", width = 12, cursor = "hand2",
            command = way3).place(x = 1060, y = 630, anchor = "se")

    tk.Button(window, text = "常驻武器唤取", font = ("文鼎方新书H7GBK_H",16), 
            bg = "grey", fg = "white", width = 12, cursor = "hand2",
            command = way4).place(x = 1240, y = 630, anchor = "se")

    tk.Button(window, text = "官方网站", font = ("文鼎方新书H7GBK_H",16), 
            bg = "grey", fg = "orange", width = 12, cursor = "hand2",
            command = website).place(x = 1240, y = 180, anchor = "se")

    tk.Button(window, text = "退出程序", font = ("文鼎方新书H7GBK_H",16), 
            bg = "grey", fg = "dark red", width = 12, cursor = "hand2",
            command = exit).place(x = 1240, y = 240, anchor = "se")

    # 进入消息循环
    window.mainloop()

if __name__ == "__main__":
    creatWindow()
