import sys
import os
import random

epsilon = open("epsilon.txt", "r+")
greed = eval(epsilon.read())


def degreed():
    g = greed - 0.01
    epsilon.seek(0)
    epsilon.write(f"{g}")
    epsilon.write("      ")


def user(a, log):
    r, c = eval(input("Enter Row, Column: "))
    while r not in range(1, 4) or c not in range(1, 4):
        sys.stderr.write("Please enter valid values\n\n")
        r, c = eval(input("Enter Row, Column: "))
    i = 3 * c + r - 4
    while l[i] != " ":
        sys.stderr.write("Please enter valid cell\n\n")
        r, c = eval(input("Enter Row, Column: "))
        i = 3 * c + r - 4
    l[i] = a
    listy = list(log)
    if a == 'x':
        player = "1"
    else:
        player = "2"
    listy[i] = player
    log = "".join(listy)
    return log


def listify(met):
    lis = []
    for i in range(3):
        lis.append(met[3*i:3*i+3])
    else:
        return lis


def rotate(mat):
    lis = listify(mat)
    b = ""
    for i in range(3):
        b += lis[2][i] + lis[1][i] + lis[0][i]
    return b


def mirror(mat):
    lis = listify(mat)
    b = ""
    for i in range(3):
        for j in range(3):
            b += lis[i][2-j]
    else:
        return b


def flip(mat):
    lis = listify(mat)
    lis[0], lis[2] = lis[2], lis[0]
    return "".join(lis)


def poss(log):
    p = []
    for i in range(4):
        p.append(rotate(log))
        p.append(mirror(log))
        p.append(flip(log))
        p.append(mirror(flip(log)))
    else:
        return p


def keeplog(p, st, file):
    for i in p:
        file.seek(0)
        thelogs = list(eval(file.read()))
        mem1 = [i, st]
        if mem1 in thelogs:
            file.close()
            break
        file.write(f",{mem1}")
    else:
        file.close()


def checkrow(t):
    a = 3 * (t - 1)
    return [l[a], l[a + 1], l[a + 2]]


def checkcol(t):
    a = t - 1
    return [l[a], l[a + 3], l[a + 6]]


def checkdia(t):
    if t == 1:
        return [l[0], l[4], l[8]]
    elif t == 2:
        return [l[2], l[4], l[6]]


def checkwin(a, b):
    for i in range(1, 4):
        if checkrow(i).count(a) == 3 or checkcol(i).count(a) == 3:
            return 1
        elif checkrow(i).count(b) == 3 or checkcol(i).count(b) == 3:
            return 2
    for i in range(1, 3):
        if checkdia(i).count(a) == 3 or checkdia(i).count(a) == 3:
            return 1
        elif checkdia(i).count(b) == 3 or checkdia(i).count(b) == 3:
            return 2
    if l.count(" ") == 0:
        return 3
    return 0


def innit(met,det):
    ind = 0
    for i in met:
        if i == "0":
            ind += 1
        elif i == det[ind]:
            ind += 1
        else:
            return False
    else:
        return True


def innitall(x,y):
    for i in y:
        if innit(x,i):
            return True
    else:
        return False


def losemove(listy, lis):
    blist = listy.copy()
    move = random.randint(0, 8)
    while l[move] != " ":
        print(move)
        move = random.randint(0, 8)
    blist[move] = "2"
    blisty = "".join(blist)
    noch = 0
    while innitall(blisty, lis):
        blist = listy.copy()
        move = random.randint(0, 8)
        if l[move] != " ":
            continue
        blist[move] = "2"
        blisty = "".join(blist)
        if noch >= 64:
            break
        noch += 1
    return move


def elsemove(listy, lis):
    blist = listy.copy()
    blisty = "".join(blist)
    move = random.randint(0, 8)
    while l[move] != " ":
        move = random.randint(0, 8)
    print("final: ", move)
    blist[move] = "2"
    blisty = "".join(blist)
    noch = 0
    while innitall(blisty, lis):
        blist = listy.copy()
        move = random.randint(0, 8)
        if l[move] != " ":
            continue
        blist[move] = "2"
        blisty = "".join(blist)
        if noch >= 64:
            break
        noch += 1
    return move


def pc(log, file):
    os.system('cls')
    file.seek(0)
    fr1 = file.read()
    if random.random() < greed:
        f = random.randint(0, 8)
        while l[f] != " ":
            f = random.randint(0, 8)
        listy = list(log)
        listy[f] = "2"
        log = "".join(listy)
        return f,log
    else:
        listy = list(log)
        le = list(eval(fr1))
        win = []
        draw = []
        lose = []
        for i in le:
            if innit(log, i[0]):
                if i[1] == 1:
                    win.append(i[0])
                elif i[1] == 0:
                    draw.append(i[0])
                else:
                    lose.append(i[0])
        else:
            if len(win) == 0 and len(draw) == 0 and len(lose) == 0:
                f = random.randint(0, 8)
                while l[f] != " ":
                    f = random.randint(0, 8)
                listy = list(log)
                listy[f] = "2"
                log = "".join(listy)
                return f, log

            elif len(win) == 0 and len(draw) == 0:
                lmove = losemove(listy, lose)
                listy[lmove] = "2"
                log = "".join(listy)
                return lmove, log

            elif len(win) != 0:
                wmove = elsemove(listy, win)
                listy[wmove] = "2"
                log = "".join(listy)
                return wmove, log

            else:
                dmove = elsemove(listy, draw)
                listy[dmove] = "2"
                log = "".join(listy)
                return dmove, log


def pc2(step, log, file):
    os.system('cls')
    file.seek(0)
    fr1 = file.read()
    if random.random() < greed or step == 0:
        f = random.randint(0, 8)
        while l[f] != " ":
            f = random.randint(0, 8)
        listy = list(log)
        listy[f] = "1"
        log = "".join(listy)
        return f,log
    else:
        listy = list(log)
        le = list(eval(fr1))
        win = []
        draw = []
        lose = []
        for i in le:
            if innit(log, i[0]):
                if i[1] == -1:
                    win.append(i[0])
                elif i[1] == 0:
                    draw.append(i[0])
                else:
                    lose.append(i[0])
        else:
            if len(win) == 0 and len(draw) == 0 and len(lose) == 0:
                f = random.randint(0, 8)
                while l[f] != " ":
                    f = random.randint(0, 8)
                listy = list(log)
                listy[f] = "1"
                log = "".join(listy)
                return f, log

            elif len(win) == 0 and len(draw) == 0:
                lmove = losemove(listy, lose)
                listy[lmove] = "1"
                log = "".join(listy)
                return lmove, log

            elif len(win) != 0:
                wmove = elsemove(listy, win)
                listy[wmove] = "1"
                log = "".join(listy)
                return wmove, log

            else:
                dmove = elsemove(listy, draw)
                listy[dmove] = "1"
                log = "".join(listy)
                return dmove, log


def game():
    global greed
    file = open("log.txt", "r+")
    mem = '000000000'
    print(
        f" {l[0]} │ {l[1]} │ {l[2]}\n───┼───┼───\n {l[3]} │ {l[4]} │ {l[5]}\n───┼───┼───\n {l[6]} │ {l[7]} │ {l[8]}\n\n")
    k = input("Choose one [X/O]: ")
    if k.upper() == "X":
        a = "X"
        b = "O"
        j = 0
        while checkwin(a, b) == 0:
            if j % 2 == 0:
                mem = user(a, mem)
            else:
                move,mem = pc(mem,file)
                l[move] = "O"
            print(
                f" {l[0]} │ {l[1]} │ {l[2]}\n───┼───┼───\n {l[3]} │ {l[4]} │ {l[5]}\n───┼───┼───\n {l[6]} │ {l[7]} │ {l[8]}\n\n")
            j += 1

        if checkwin(a, b) == 1:
            print("bruh you won")
            keeplog(poss(mem), -1, file)
            degreed()
            return
        elif checkwin(a, b) == 2:
            print("lmao lost to random")
            keeplog(poss(mem), 1, file)
            degreed()
            return
        elif checkwin(a, b) == 3:
            print("shit always draws istg")
            keeplog(poss(mem), 0, file)
            degreed()
            return

    elif k.upper() == "O":
        a = "O"
        b = "X"
        j = 0
        while checkwin(a, b) == 0:
            if j % 2 != 0:
                mem = user(a, mem)
            else:
                move, mem = pc2(j, mem, file)
                l[move] = "X"
            print(
                f" {l[0]} │ {l[1]} │ {l[2]}\n───┼───┼───\n {l[3]} │ {l[4]} │ {l[5]}\n───┼───┼───\n {l[6]} │ {l[7]} │ {l[8]}\n\n")
            j += 1

        if checkwin(a, b) == 1:
            print("bruh you won")
            keeplog(poss(mem), -1, file)
            degreed()
            return
        elif checkwin(a, b) == 2:
            print("lmao lost to random")
            keeplog(poss(mem), 1, file)
            degreed()
            return
        elif checkwin(a, b) == 3:
            print("shit always draws istg")
            keeplog(poss(mem), 0, file)
            degreed()
            return


while True:
    l = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    game()
    inbu = input("Continue? (Y/N) : ")
    if inbu.lower() == 'y':
        continue
    else:
        epsilon.close()
        exit()
