import os

def reset_cu():
    f = open("resource/character.time","w",encoding="UTF-8")
    f.write("star5 = [1,False]\nstar4 = [1,False]")
    f.close()
    f = open("resource/character.txt","w",encoding="UTF-8")
    f.write("")
    f.close()
    os.system("cls")

def reset_wu():
    f = open("resource/weapon.time","w",encoding="UTF-8")
    f.write("star5_wu = [1]\nstar4_wu = [1,False]")
    f.close()
    f = open("resource/weapon.txt","w",encoding="UTF-8")
    f.write("")
    f.close()
    os.system("cls")

if __name__ == "__main__":
    reset_cu()
    reset_wu()