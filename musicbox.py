from tkinter import *
import time
import datetime
import pygame

pygame.init()
pygame.mixer.init()
root = Tk()
root.title("Music Box")
root.geometry('1352x700+0+0')
root.configure(background='white')

abc = Frame(root, bg="powder blue", bd=20, relief=RIDGE)
abc.grid()
abc1 = Frame(abc, bg="powder blue", bd=20, relief=RIDGE)
abc1.grid()
abc2 = Frame(abc, bg="powder blue", relief=RIDGE)
abc2.grid()
abc3 = Frame(abc, bg="powder blue", relief=RIDGE)
abc3.grid()

str1 = StringVar()
str1.set("Just Like Music")
Date1 = StringVar()
Time1 = StringVar()

Date1.set(time.strftime("%d/%m/%Y"))
Time1.set(time.strftime("%H:%M:%S"))


# ======================================================================================================

def value_cs():
    str1.set("C#")
    sound = pygame.mixer.Sound("/home/raghav/Music/piano_keys/c1.wav")
    sound.play()

def value_c():
    str1.set("C")
    sound = pygame.mixer.Sound("/home/raghav/Music/piano_keys/c.wav")
    sound.play()

def value_c1():
    str1.set("C1")
    sound = pygame.mixer.Sound("/home/raghav/Music/piano_keys/c2.wav")
    sound.play()

def value_c11():
    str1.set("C#1")
    sound = pygame.mixer.Sound("/home/raghav/Music/piano_keys/c21.wav")
    sound.play()

def value_ds():
    str1.set("D#")
    sound = pygame.mixer.Sound("/home/raghav/Music/piano_keys/d1.wav")
    sound.play()

def value_d():
    str1.set("D")
    sound = pygame.mixer.Sound("/home/raghav/Music/piano_keys/d.wav")
    sound.play()

def value_D1():
    str1.set("D1")
    sound = pygame.mixer.Sound("/home/raghav/Music/piano_keys/d2.wav")
    sound.play()

def value_d11():
    str1.set("D#1")
    sound = pygame.mixer.Sound("/home/raghav/Music/piano_keys/d21.wav")
    sound.play()

def value_e():
    str1.set("E")
    sound = pygame.mixer.Sound("/home/raghav/Music/piano_keys/e.wav")
    sound.play()

def value_e1():
    str1.set("E1")
    sound = pygame.mixer.Sound("/home/raghav/Music/piano_keys/e2.wav")
    sound.play()

def value_f():
    str1.set("F")
    sound = pygame.mixer.Sound("/home/raghav/Music/piano_keys/f.wav")
    sound.play()

def value_fs():
    str1.set("F#")
    sound = pygame.mixer.Sound("/home/raghav/Music/piano_keys/f1.wav")
    sound.play()

def value_f1():
    str1.set("F1")
    sound = pygame.mixer.Sound("/home/raghav/Music/piano_keys/f2.wav")
    sound.play()

def value_g():
    str1.set("G")
    sound = pygame.mixer.Sound("/home/raghav/Music/piano_keys/g.wav")
    sound.play()

def value_gs():
    str1.set("G#")
    sound = pygame.mixer.Sound("/home/raghav/Music/piano_keys/g1.wav")
    sound.play()

def value_a():
    str1.set("A")
    sound = pygame.mixer.Sound("/home/raghav/Music/piano_keys/a.wav")
    sound.play()

def value_b():
    str1.set("B")
    sound = pygame.mixer.Sound("/home/raghav/Music/piano_keys/b.wav")
    sound.play()

def value_bb():
    str1.set("Bb")
    sound = pygame.mixer.Sound("/home/raghav/Music/piano_keys/a1.wav")
    sound.play()

# ===============================================Label with title=======================================================

Label(abc1, text="Piano Musical Keys", font=('arial', 25, 'bold'), padx=8, pady=8, bd=4, bg="powder blue", fg="white",
      justify=CENTER).grid(row=0, column=0, columnspan=11)

# ======================================================================================================

txtDate = Entry(abc1, textvariable=Date1, font=('arial', 25, 'bold'), bd=34, bg="powder blue", fg="black", width=18,
                justify=CENTER).grid(row=1, column=0, pady=1)
txtDisplay = Entry(abc1, textvariable=str1, font=('arial', 25, 'bold'), bd=34, bg="powder blue", fg="black", width=18,
                   justify=CENTER).grid(row=1, column=1, pady=1)
txtTime = Entry(abc1, textvariable=Time1, font=('arial', 25, 'bold'), bd=34, bg="powder blue", fg="black", width=17,
                justify=CENTER).grid(row=1, column=2, pady=1)

# =======================================================================================================

btncs = Button(abc2, height=6, width=6, text="C#", font=('arial', 18, 'bold'), bd=4, bg="black", fg="white",
               command=value_cs)
btncs.grid(row=0, column=0, padx=5, pady=5)

btnds = Button(abc2, height=6, width=6, text="D#", font=('arial', 18, 'bold'), bd=4, bg="black", fg="white", command= value_ds)
btnds.grid(row=0, column=2, padx=5, pady=5)

btnfs = Button(abc2, height=6, width=6, text="F#", font=('arial', 18, 'bold'), bd=4, bg="black", fg="white", command=value_fs)
btnfs.grid(row=0, column=4, padx=5, pady=5)

btnspace2 = Button(abc2, state=DISABLED, width=2, height=6, bg="powder blue", relief=FLAT)
btnspace2.grid(row=0, column=3, padx=5, pady=5)

btngs = Button(abc2, height=6, width=6, text="G#", font=('arial', 18, 'bold'), bd=4, bg="black", fg="white", command=value_gs)
btngs.grid(row=0, column=6, padx=5, pady=5)

btnbb = Button(abc2, height=6, width=6, text="Bb", font=('arial', 18, 'bold'), bd=4, bg="black", fg="white", command=value_bb)
btnbb.grid(row=0, column=8, padx=5, pady=5)

btnspace5 = Button(abc2, state=DISABLED, width=2, height=6, bg="powder blue", relief=FLAT)
btnspace5.grid(row=0, column=9, padx=5, pady=5)

btncs1 = Button(abc2, height=6, width=6, text="C#1", font=('arial', 18, 'bold'), bd=4, bg="black", fg="white", command=value_c11)
btncs1.grid(row=0, column=10, padx=5, pady=5)

btnds1 = Button(abc2, height=6, width=6, text="D#1", font=('arial', 18, 'bold'), bd=4, bg="black", fg="white", command=value_d11)
btnds1.grid(row=0, column=12, padx=5, pady=5)

# =======================================================================================================

btnc = Button(abc3, height=8, width=5, text="C", font=('arial', 18, 'bold'), bd=4, bg="black", fg="white", command=value_c)
btnc.grid(row=0, column=0, padx=5, pady=5)

btnd = Button(abc3, height=8, width=5, text="D", font=('arial', 18, 'bold'), bd=4, bg="black", fg="white", command=value_d)
btnd.grid(row=0, column=1, padx=5, pady=5)

btne = Button(abc3, height=8, width=5, text="E", font=('arial', 18, 'bold'), bd=4, bg="black", fg="white", command=value_e)
btne.grid(row=0, column=2, padx=5, pady=5)

btnf = Button(abc3, height=8, width=5, text="F", font=('arial', 18, 'bold'), bd=4, bg="black", fg="white", command=value_f)
btnf.grid(row=0, column=3, padx=5, pady=5)

btng = Button(abc3, height=8, width=5, text="G", font=('arial', 18, 'bold'), bd=4, bg="black", fg="white", command=value_g)
btng.grid(row=0, column=4, padx=5, pady=5)

btna = Button(abc3, height=8, width=5, text="A", font=('arial', 18, 'bold'), bd=4, bg="black", fg="white", command=value_a)
btna.grid(row=0, column=5, padx=5, pady=5)

btnb = Button(abc3, height=8, width=5, text="B", font=('arial', 18, 'bold'), bd=4, bg="black", fg="white", command=value_b)
btnb.grid(row=0, column=6, padx=5, pady=5)

btnc1 = Button(abc3, height=8, width=5, text="C1", font=('arial', 18, 'bold'), bd=4, bg="black", fg="white", command=value_c1)
btnc1.grid(row=0, column=7, padx=5, pady=5)

btnd1 = Button(abc3, height=8, width=5, text="D1", font=('arial', 18, 'bold'), bd=4, bg="black", fg="white", command=value_D1)
btnd1.grid(row=0, column=8, padx=5, pady=5)

btne1 = Button(abc3, height=8, width=5, text="E1", font=('arial', 18, 'bold'), bd=4, bg="black", fg="white", command=value_e1)
btne1.grid(row=0, column=9, padx=5, pady=5)

btnf1 = Button(abc3, height=8, width=5, text="F1", font=('arial', 18, 'bold'), bd=4, bg="black", fg="white", command=value_f1)
btnf1.grid(row=0, column=10, padx=5, pady=5)

# =======================================================================================================

root.mainloop()
