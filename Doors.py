import tkinter as tk
import random
import time

root = tk.Tk()
root.geometry("390x300")

wlcm = tk.Label(root, width=36, font=("Arial", 12))
wlcm.grid(row=1, column=1, columnspan=3, ipadx=30)

is_playing = 0
score = 0
win = random.randint(0, 2)
tries = 0
switch = tk.BooleanVar()


def change_msg(msg="Hi, i'm a simulation of a Monty Hall problem!"):
    wlcm['text'] = msg


def reset(is_simulating=True):
    global is_playing
    global win
    global score_l
    global score
    global winrate

    is_playing = 0
    win = random.randint(0, 2)
    doors[0]['text'] = 'Play!'
    doors[1]['text'] = 'Simulate 1000'
    doors[2]['text'] = 'Quit'
    score_l['text'] = 'Score: ' + str(score)
    if tries != 0:
        winrate['text'] = 'Winrate:\n' + str(round(score / tries * 100, 3)) + '%'
    else:
        winrate['text'] = 'Winrate:\n0.0%'

    if is_simulating is False:
        root.after(2000, change_msg)
    else:
        change_msg()


def full_reset():
    global tries
    global score
    global tries_l

    tries = 0
    score = 0
    tries_l['text'] = 'Tries: ' + str(tries)
    reset()


def f():
    global is_playing
    global tries
    global tries_l
    global win
    global score

    if is_playing == 0:
        is_playing = 1
        tries += 1
        tries_l['text'] = 'Tries: ' + str(tries)

        doors[0]['text'] = 'Door 1'
        doors[1]['text'] = 'Door 2'
        doors[2]['text'] = 'Door 3'
        change_msg("Pick a Door")
    elif is_playing == 1:
        doors[0]['text'] = 'PICKED'
        for d in range(len(doors)):
            if d != win and d != 0:
                doors[d]['text'] = 'EMPTY'
                is_playing = 2
                break
        change_msg("Change The Door or click yours again")
    elif is_playing == 2 and doors[0]['text'] != 'EMPTY':
        if win == 0:
            score += 1
            wlcm['text'] = 'You Won!!!'
        else:
            wlcm['text'] = 'You Lost :('
        reset(False)


def s():
    global is_playing
    global win
    global score

    if is_playing == 0:
        if switch.get():
            for x in range(1000):
                f()
                f()
                if doors[1]['text'] != 'EMPTY':
                    s()
                else:
                    t()
        else:
            for x in range(1000):
                f()
                f()
                f()
        reset()

    elif is_playing == 1:
        doors[1]['text'] = 'PICKED'
        for d in range(len(doors)):
            if d != win and d != 1:
                doors[d]['text'] = 'EMPTY'
                is_playing = 2
                break
        change_msg("Change The Door or click yours again")
    elif is_playing == 2 and doors[1]['text'] != 'EMPTY':
        if win == 1:
            score += 1
            wlcm['text'] = 'You Won!!!'
        else:
            wlcm['text'] = 'You Lost :('
        reset(False)


def t():
    global is_playing
    global win
    global score

    if is_playing == 0:
        root.destroy()
    elif is_playing == 1:
        doors[2]['text'] = 'PICKED'
        for d in range(len(doors)):
            if d != win and d != 2:
                doors[d]['text'] = 'EMPTY'
                is_playing = 2
                break
        change_msg("Change The Door or click yours again")
    elif is_playing == 2 and doors[2]['text'] != 'EMPTY':
        if win == 2:
            score += 1
            wlcm['text'] = 'You Won!!!'
        else:
            wlcm['text'] = 'You Lost :('
        reset(False)


change_msg()

d1_p = tk.PhotoImage(file="img/door_1.png")
d1 = tk.Button(root, text='Play!', image=d1_p, command=f, compound=tk.TOP)
d1.grid(row=2, column=1, padx=10)

d2_p = tk.PhotoImage(file="img/door_2.png")
d2 = tk.Button(root, text='Simulate 1000', image=d2_p, command=s, compound=tk.TOP)
d2.grid(row=2, column=2)

d3_p = tk.PhotoImage(file="img/door_3.png")
d3 = tk.Button(root, text='Quit', image=d3_p, command=t, compound=tk.TOP)
d3.grid(row=2, column=3, padx=10)

doors = [d1, d2, d3]

tries_l = tk.Label(root, text='Tries: ' + str(tries))
tries_l.grid(row=3, column=1)

score_l = tk.Label(root, text='Score: ' + str(score))
score_l.grid(row=3, column=2)

winrate = tk.Label(root, text='Winrate:\n0.0%')
winrate.grid(row=3, column=3)

switchCheckbox = tk.Checkbutton(root, text="Swich the door\nwhen simulating", variable=switch, onvalue=True, offvalue=False)
switchCheckbox.grid(row=4, column=2)

Reset_b = tk.Button(root, text='Reset', command=full_reset, width=6)
Reset_b.grid(row=4, column=3, padx=10)

root.mainloop()
