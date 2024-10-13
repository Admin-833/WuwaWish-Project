# 导入模块
import tkinter as tk
from PIL import Image, ImageTk
import time, random, os
from reset import reset_wu

# 读取保底信息
f = open("resource/weapon.time","r",encoding="UTF-8")
for i in f: exec(i)
f.close()

# 读取卡池信息
f = open("resource/global.wuwa","r",encoding="UTF-8")
for i in f: exec(i)
f.close()

f = open("resource/weapon.wuwa","r",encoding="UTF-8")
for i in f: exec(i)
f.close()

four_star_weapon_ext += four_star_weapon
for i in four_star_wu: 
    try: four_star_weapon_ext.remove(i)
    except: pass

# 重绘保底信息
def drawlabel(window):
    tk.Label(window, text = """距离上次五星{0}抽
距离上次四星{1}抽，大保底{2}""".format(star5_wu[0]-1, star4_wu[0]-1, star4_wu[1]),
font = ("文鼎方新书H7GBK_H",14), bg = "white", justify = "center",
fg = "black").place(x = 480, y = 720, anchor = "sw", width=320)

# 定义抽卡主函数
def fun_wu(t):
    global star5_wu,star4_wu
    result_star5 = []
    result_star4 = []
    result_star3 = []
    result_text = ""
    f = open("resource/weapon.txt","r+",encoding="UTF-8")
    time_str = time.strftime("%Y年%m月%d日 %H:%M:%S")
    for i in range(t):
        num = random.randrange(0,1000)
        a,c,d,e = 8,30,15,15    # 概率设置，单位千分之一
        if star5_wu[0] >= 70:          # 大于70抽时概率递增
            a = 8+(star5_wu[0]-69)*992/11
        if star4_wu[0] >= 9:           # 第9抽时二分之一概率出4星物品
            c, d, e = (1000-a)/4, (1000-a)/8, (1000-a)/8
        if star4_wu[0] >= 10:          # 每10抽时必出4星物品
            c, d, e = (1000-a)/2, (1000-a)/4, (1000-a)/4
        if star4_wu[1]:                # 4星大保底时必出UP武器
            c, d, e = c+d+e, 0, 0
        if num < a:                 # 五星UP武器
            result = "(5星)"+random.choice(five_star_wu)
            result_star5.append(result)
            star5_wu = [1,False]
            star4_wu[0] += 1
        elif num < a+c:           # 四星UP角色
            result = "(4星)"+random.choice(four_star_wu)
            result_star4.append(result)
            star4_wu = [1,False]
            star5_wu[0] += 1
        elif num < a+c+d:         # 四星常驻角色
            result = "(4星)"+random.choice(four_star_character)
            result_star4.append(result)
            star4_wu = [1,True]
            star5_wu[0] += 1
        elif num < a+c+d+e:       # 四星常驻武器
            result = "(4星)"+random.choice(four_star_weapon_ext)
            result_star4.append(result)
            star4_wu = [1,True]
            star5_wu[0] += 1
        else:                       # 三星武器
            result = "(3星)"+random.choice(three_star)
            result_star3.append(result)
            star4_wu[0] += 1
            star5_wu[0] += 1
        result_text = time_str + "  " + result + '\n' + result_text
    old = f.read()
    f.seek(0)
    f.write(result_text)
    f.write(old)
    f.close()
    f = open("resource/weapon.time","w",encoding="UTF-8")
    f.write("star5_wu = {}\nstar4_wu = {}".format(star5_wu,star4_wu))
    f.close()
    drawlabel(window)
    return result_star5, result_star4, result_star3
def one_wu():              # 单次唤取
    result_star5, result_star4, result_star3 = fun_wu(1)
    for i in result_star5: print("\033[33m{}\033[0m".format(i))
    for i in result_star4: print("\033[35m{}\033[0m".format(i))
    for i in result_star3: print("\033[34m{}\033[0m".format(i))
    print()
def ten_wu():              # 十次唤取
    result_star5, result_star4, result_star3 = fun_wu(10)
    for i in result_star5: print("\033[33m{}\033[0m".format(i),end=", ")
    for i in result_star4: print("\033[35m{}\033[0m".format(i),end=", ")
    for i in result_star3: print("\033[34m{}\033[0m".format(i),end=", ")
    print("\n")
def history_wu():          # 历史记录
    os.system("start resource/weapon.txt")
def clear_wu():            # 清除记录
    global star5_wu, star4_wu
    star5_wu = [1]
    star4_wu = [1,False]
    reset_wu()
    drawlabel(window)

# 定义绘制窗口函数
def creatWindow_wu():
    # 创建tk窗口
    global window
    window = tk.Tk()

    # 设置窗口基本信息
    window.title("武器活动唤取")
    window.geometry("1280x720+5+5")
    window.resizable(False, False)
    window.iconbitmap("resource/titleicon.ico")

    # 绘制背景图
    bg_img = ImageTk.PhotoImage(Image.open("resource/weapon.jpg"))
    tk.Label(window, image=bg_img).pack(anchor="center")
    
    # 显示保底信息
    drawlabel(window)

    # 绘制按钮
    tk.Button(window, text = "单次唤取", font = ("文鼎方新书H7GBK_H",16), 
            bg = "grey", fg = "white", width = 10, cursor = "hand2",
            command = one_wu).place(x = 40, y = 40, anchor = "nw")

    tk.Button(window, text = "十次唤取", font = ("文鼎方新书H7GBK_H",16), 
            bg = "grey", fg = "white", width = 10, cursor = "hand2",
            command = ten_wu).place(x = 205, y = 40, anchor = "nw")

    tk.Button(window, text = "历史记录", font = ("文鼎方新书H7GBK_H",16), 
            bg = "grey", fg = "white", width = 10, cursor = "hand2",
            command = history_wu).place(x = 40, y = 110, anchor = "nw")

    tk.Button(window, text = "返回主页", font = ("文鼎方新书H7GBK_H",16), 
            bg = "grey", fg = "white", width = 10, cursor = "hand2",
            command = window.destroy).place(x = 205, y = 110, anchor = "nw")

    tk.Button(window, text = "清除记录", font = ("文鼎方新书H7GBK_H",16), 
            bg = "grey", fg = "orange", width = 10, cursor = "hand2",
            command = clear_wu).place(x = 1075, y = 40, anchor = "ne")

    tk.Button(window, text = "退出程序", font = ("文鼎方新书H7GBK_H",16), 
            bg = "grey", fg = "dark red", width = 10, cursor = "hand2",
            command = exit).place(x = 1240, y = 40, anchor = "ne")

    # 进入消息循环
    window.mainloop()

if __name__ == "__main__":
    creatWindow_wu()