#copie main on va voir à quoi il sert
from pyautogui import *
import subprocess
import pyautogui
import time
import random
import win32api, win32con
import keyboard
import cv2
from tkinter import *
import sys
from tkinter import ttk
resolution = [1920,1080]
global a,var1,var2,var3
a,var1,var2=0,0,0
nbrdetourmax=10 #nombre de tour de map faut mettre un input aussi
var3=0 #nombre de tour de road en direct


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.10)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
def click1():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.10)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
#-------------------------Les variables nécessités dans la fonction cbt-----------------------------

#pm deviendra input(..) ou plutot une jauge eheh (faudra changer move dans cbt
global x1,y1,ennemi,perso,abandon, ennemi1,ennemi2,ennemi3,ennemi4,perso1,perso2,perso3,perso4,pm, pix,btnstopcbt,clafinducbt
x1,y1=0,0 #on va les utiliser pour la fonction attaque (atk)
abandon=0 #comptabilise le nombre de tour de cbt pour abandonner quand trop long au cas où l'épouvantail soit trop loin en mode hard
pix = 30    #distance d'une demi diagonale d'un carré de déplacement (2pix en x et 2pix en y feront descendre 
pm = 2      #vers le bas droite de 2d
clafinducbt=0
#-------------------------------------------CBT----------------------------------------
def fincbt():
    global clafinducbt
    btnstopcbt = pyautogui.locateCenterOnScreen('C:\\Users\\albin\\OneDrive\\Documents\\CODING\\dofus\\cbt\\btnfermercbt.png',region = resolution(17,4,65,82), confidence=0.7)
    if btnstopcbt:
        click(btnstopcbt[0],btnstopcbt[1])
        clafinducbt=1
        main()
def tempocbt():
    global clafinducbt
    if ennemi is None:
        fincbt()
        time.sleep(2)
        if clafinducbt==0:
            cbt()

def decalesouris() :
    pyautogui.moveTo(resolution(50,50))
def trouverennemi():
    global ennemi,ennemi1,ennemi2,ennemi3,ennemi4,ennemi5,ennemi6,ennemi7,ennemi8
    ennemi1 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\ennemi\ennemihautgch1.png',region = resolution(17,4,65,82), confidence=0.6)
    ennemi2 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\ennemi\ennemibasdrt.png',region = resolution(17,4,65,82), confidence=0.6)
    ennemi3 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\ennemi\ennemihautdrt.png',region =resolution(17,4,65,82), confidence=0.6)
    ennemi4 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\ennemi\ennemibasgch.png',region = resolution(17,4,65,82), confidence=0.6)
    ennemi5 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\ennemi\ennemi5.png',region = resolution(17,4,65,82), confidence=0.6)
    ennemi6 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\ennemi\ennemi6.png',region = resolution(17,4,65,82), confidence=0.6)
    ennemi7 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\ennemi\ennemi7.png',region = resolution(17,4,65,82), confidence=0.6)
    ennemi8 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\ennemi\ennemi8.png',region = resolution(17,4,65,82), confidence=0.6)
    ennemi9 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\ennemi\ennemi9.png',region = resolution(17,4,65,82), confidence=0.6)
    ennemi10 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\ennemi\ennemi10.png',region = resolution(17,4,65,82), confidence=0.6)
    ennemi11 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\ennemi\ennemi11.png',region = resolution(17,4,65,82), confidence=0.6)
    ennemi12 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\ennemi\ennemi12.png',region = resolution(17,4,65,82), confidence=0.6)
    if ennemi1==None and ennemi2==None and ennemi3==None and ennemi4==None and ennemi5==None and ennemi6==None and ennemi7==None and ennemi8==None and ennemi9==None and ennemi10==None and ennemi11==None and ennemi12==None :
        decalesouris()
        if ennemi1 :
            ennemi=pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\ennemi\ennemihautgch1.png',region = resolution(17,4,65,82), confidence=0.6)
            print("1")
        if ennemi2:
            ennemi= pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\ennemi\ennemibasdrt.png',region = resolution(17,4,65,82), confidence=0.6)
            print("2")
        if ennemi3:
            ennemi=pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\ennemi\ennemihautdrt.png',region =resolution(17,4,65,82), confidence=0.6)
            print("3")
        if ennemi4 :
            ennemi=pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\ennemi\ennemibasgch.png',region = resolution(17,4,65,82), confidence=0.6)
            print("4")
        if ennemi5 :
            ennemi=pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\ennemi\ennemi5.png',region = resolution(17,4,65,82), confidence=0.6)
            print("5")
        if ennemi6 :
            ennemi=pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\ennemi\ennemi6.png',region = resolution(17,4,65,82), confidence=0.6)
            print("6")
        if ennemi7 :
            ennemi=pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\ennemi\ennemi7.png',region = resolution(17,4,65,82), confidence=0.6)
            print("7")
        if ennemi8 :
            ennemi=pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\ennemi\ennemi8.png',region = resolution(17,4,65,82), confidence=0.6)
            print("8")
        if ennemi9 :
            ennemi=pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\ennemi\ennemi9.png',region = resolution(17,4,65,82), confidence=0.6)
            print("9")
        if ennemi10 :
            ennemi=pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\ennemi\ennemi10.png',region = resolution(17,4,65,82), confidence=0.6)
            print("10")
        if ennemi11 :
            ennemi=pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\ennemi\ennemi11.png',region = resolution(17,4,65,82), confidence=0.6)
            print("11")
        if ennemi12 :
            ennemi=pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\ennemi\ennemi12.png',region = resolution(17,4,65,82), confidence=0.6)
            print("12")

def terminertour():
    global x1,y1,ennemi,perso,abandon, ennemi1,ennemi2,ennemi3,ennemi4,perso1,perso2,perso3,perso4,pm, pix,btnstopcbt
    time.sleep(2)
    btnstopcbt = pyautogui.locateCenterOnScreen('C:\\Users\\albin\\OneDrive\\Documents\\CODING\\btnfermercbt.png',region = resolution(17,4,65,82), confidence=0.9)
    fincbt()
    passertour = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\terminertour.png', confidence=0.5)
    if passertour:
        click(passertour.x,passertour.y)
    if not passertour and not btnstopcbt :
        pyautogui.moveTo(100,100) #ca peut etre du au fait que la souris est sur l'ennemi, il suffit de bouger la souris
        terminertour()
    abandon+=1
    if abandon==20 :
        abandon = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\imageabandon.png', confidence=0.8)
        click(abandon.x,abandon.y)

def activermodecrea():
    global x1,y1,ennemi,perso,abandon, ennemi1,ennemi2,ennemi3,ennemi4,perso1,perso2,perso3,perso4,pm, pix,btnstopcbt
    fincbt()
    if perso1==None and perso2==None and perso3==None and perso4==None :    
        pyautogui.keyDown('shift')
        pyautogui.press('(')
        pyautogui.keyUp('shift')
        print("mode créa activé")
        fincbt()
        quelperso()
        reconnaissanceduterrain()
    if perso1 or perso2 or perso3 or perso4 :
        print("il reconnait le perso la")

def levraimouv(placeperso):
    if nbrpm.get()==None :
        if placeperso=="hautgch":
            moveTo(perso.x,perso.y)
            lemouvx=3*resolution(2.34)
            lemouvy=3*1/2*resolution(2.34)
        if placeperso=="hautdrt" :
            moveTo(perso.x,perso.y)
            lemouvx=-3*resolution(2.34)
            lemouvy=3*1/2*resolution(2.34)
        if placeperso=="basdrt" :
            moveTo(perso.x,perso.y)
            lemouvx=-3*resolution(2.34)
            lemouvy=-3*1/2*resolution(2.34)
        if placeperso=="basgch" :
            moveTo(perso.x,perso.y)
            lemouvx=3*resolution(2.34)
            lemouvy=-3*1/2*resolution(2.34)
        return(lemouvx,lemouvy)
    if nbrpm.get() :
        print("PM : " +nbrpm.get())
        if placeperso=="hautgch":
            moveTo(perso.x,perso.y)
            lemouvx=int(nbrpm.get())*resolution(2.34)
            lemouvy=int(nbrpm.get())*1/2*resolution(2.34)                         #ici faudra changer pour mettre la resolution à la place de 45, d'ailleurs c'est proportionnel en x et en y shallah c'est pareil quand tu change de résolution
        if placeperso=="hautdrt" :
            moveTo(perso.x,perso.y)
            lemouvx=-int(nbrpm.get())*resolution(2.34)
            lemouvy=int(nbrpm.get())*1/2*resolution(2.34)
        if placeperso=="basdrt" :
            moveTo(perso.x,perso.y)
            lemouvx=-int(nbrpm.get())*resolution(2.34)
            lemouvy=-int(nbrpm.get())*1/2*resolution(2.34)
        if placeperso=="basgch" :
            moveTo(perso.x,perso.y)
            lemouvx=int(nbrpm.get())*resolution(2.34)
            lemouvy=-int(nbrpm.get())*1/2*resolution(2.34)
        return(lemouvx,lemouvy)

def move() :
    global x1,y1,ennemi,perso,abandon, ennemi1,ennemi2,ennemi3,ennemi4,perso1,perso2,perso3,perso4,pm, pix,btnstopcbt
    fincbt()
    trouverennemi()
    print('go move')
    time.sleep(1)
    if ennemi.x<perso.x and ennemi.y<perso.y :
        #pour quand l'ennemi est en haut à gauche par rapport au perso
        pyautogui.move(levraimouv("basdrt")[0],levraimouv("basdrt")[1])
        click1()
        time.sleep(2)
    if ennemi.x<perso.x and ennemi.y>perso.y :
        #pour quand l'ennemi est en bas à gauche par rapport au perso
        pyautogui.move(levraimouv("hautdrt")[0],levraimouv("hautdrt")[1])
        click1()
        time.sleep(2)
    if ennemi.x>perso.x and ennemi.y>perso.y :
        #pour quand l'ennemi est en bas à droite par rapport au perso
        pyautogui.move(levraimouv("hautgch")[0],levraimouv("hautgch")[1])
        click1()
        time.sleep(2)
    if ennemi.x>perso.x and ennemi.y<perso.y :
        #pour quand l'ennemi est en haut à droite par rapport au perso
        pyautogui.move(levraimouv("basgch")[0], levraimouv("basgch")[1])
        click1()
        time.sleep(2)
def attaquesadi():
    global leperso,x1,y1,ennemi,perso,abandon, ennemi1,ennemi2,ennemi3,ennemi4,ennemi5,ennemi6,ennemi7,ennemi8,perso1,perso2,perso3,perso4,pm, pix,btnstopcbt
    if leperso == "sadi" :
        print('ton perso est un sadida')
        larme = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les sorts\sadilarme.png', confidence=0.5)
        click(larme[0],larme[1])
        click(ennemi[0],ennemi[1])
        decalesouris()
        click(pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les sorts\sadiheal.png', confidence=0.5))
        click(pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les sorts\casebleu.png', confidence=0.5))
        decalesouris()
        click(larme[0],larme[1])
        click(ennemi[0],ennemi[1])
        time.sleep(2)
def lavraiatk():
    global x1,y1,ennemi,perso,abandon, ennemi1,ennemi2,ennemi3,ennemi4,ennemi5,ennemi6,ennemi7,ennemi8,perso1,perso2,perso3,perso4,pm, pix,btnstopcbt
    fincbt()
    trouverennemi()
    pyautogui.press("'")
    tempocbt()
    click(ennemi[0],ennemi[1])
    time.sleep(2)
    fincbt()
    pyautogui.press("'")
    click(ennemi[0],ennemi[1])

def atk():
    global x1,y1,ennemi,perso,abandon, ennemi1,ennemi2,ennemi3,ennemi4,perso1,perso2,perso3,perso4,pm, pix,btnstopcbt
    if perso1==None and perso2==None and perso3==None and perso4==None and ennemi1==None and ennemi2==None and ennemi3==None and ennemi4==None:
        passertour = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\terminertour.png', confidence=0.5)
        click(passertour[0],passertour[1])
    attaquesadi()
    lavraiatk()
    move()
    lavraiatk()
    time.sleep(2)
    fincbt()
        
def reconnaissanceduterrain():
    global x1,y1,ennemi,perso,abandon, ennemi1,ennemi2,ennemi3,ennemi4,perso1,perso2,perso3,perso4,pm, pix,btnstopcbt
    btnstopcbt=pyautogui.locateCenterOnScreen('C:\\Users\\albin\\OneDrive\\Documents\\CODING\\btnfermercbt.png',region = resolution(17,4,65,82), confidence=0.8)
    fincbt()
    if btnstopcbt :
        click(btnstopcbt.x,btnstopcbt.y)
        main()
    ennemi1 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\ennemi\ennemihautgch1.png',region = resolution(17,4,65,82), confidence=0.6)
    ennemi2 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\ennemi\ennemibasdrt.png',region = resolution(17,4,65,82), confidence=0.6)
    ennemi3 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\ennemi\ennemihautdrt.png',region =resolution(17,4,65,82), confidence=0.6)
    ennemi4 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\ennemi\ennemibasgch.png',region = resolution(17,4,65,82), confidence=0.6)
    if ennemi1 :
        ennemi=pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\ennemi\ennemihautgch1.png',region = resolution(17,4,65,82), confidence=0.6)
        print(ennemi1.x+ ennemi1.y)
    if ennemi2 :
        ennemi= pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\ennemi\ennemibasdrt.png',region = resolution(17,4,65,82), confidence=0.6)
        print(ennemi2.x +ennemi2.y)
    if ennemi3 :
        ennemi=pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\ennemi\ennemihautdrt.png',region =resolution(17,4,65,82), confidence=0.6)
        print(ennemi3.x + ennemi3.y)
    if ennemi4 :
        ennemi=pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\ennemi\ennemibasgch.png',region = resolution(17,4,65,82), confidence=0.6)
        print(ennemi4.x +ennemi4.y)
    if perso1 :
        perso=perso1
    if perso2 :
        perso=perso2
    if perso3 :
        perso=perso3
    if perso4 :
        perso=perso4
    if perso1==None and perso2==None and perso3==None and perso4==None :
        print('probleme pour trouver perso sur l"écran')
        fincbt()
        activermodecrea()
        reconnaissanceduterrain()
    if ennemi1==None and ennemi2==None and ennemi3==None and ennemi4==None and btnstopcbt==None:
        print("probleme pour trouver ennemi sur l'écran")
        activermodecrea()
        reconnaissanceduterrain()
    print("la fonction reconnaissance est passée")

def quelperso():
    global x1,y1,ennemi,perso,abandon, ennemi1,ennemi2,ennemi3,ennemi4,perso1,perso2,perso3,perso4,pm, pix,btnstopcbt, leperso
    leperso=listecombo.get()
    btnstopcbt=pyautogui.locateCenterOnScreen('C:\\Users\\albin\\OneDrive\\Documents\\CODING\\btnfermercbt.png',region = resolution(17,4,65,82), confidence=0.8)
    if btnstopcbt :
        click(btnstopcbt.x,btnstopcbt.y)
        main()
    if leperso == 'iop' :
        perso1 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\iop1.png',region = resolution(17,4,65,82), confidence=0.6)
        perso2 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\iop2.png',region = resolution(17,4,65,82), confidence=0.6)
        perso3 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\iop3.png',region = resolution(17,4,65,82), confidence=0.6)
        perso4 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\iop4.png',region = resolution(17,4,65,82), confidence=0.6)
#    if leperso == 'osa' :
#        perso1 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\osa1.png',region = resolution(17,4,65,82), confidence=0.4)
#        perso2 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\osa2.png',region = resolution(17,4,65,82), confidence=0.4)
#        perso3 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\osa3.png',region = resolution(17,4,65,82), confidence=0.4)
#        perso4 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\osa4.png',region = resolution(17,4,65,82), confidence=0.4)
#    if leperso == 'sram' :
#        perso1 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\sram1.png',region = resolution(17,4,65,82), confidence=0.4)
#        perso2 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\sram2.png',region = resolution(17,4,65,82), confidence=0.4)
#        perso3 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\sram3.png',region = resolution(17,4,65,82), confidence=0.4)
#        perso4 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\sram4.png',region = resolution(17,4,65,82), confidence=0.4)
#    if leperso == 'elio' :
#        perso1 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\elio1.png',region = resolution(17,4,65,82), confidence=0.4)
#        perso2 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\elio2.png',region = resolution(17,4,65,82), confidence=0.4)
#        perso3 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\elio3.png',region = resolution(17,4,65,82), confidence=0.4)
#        perso4 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\elio4.png',region = resolution(17,4,65,82), confidence=0.4)
#    if leperso == 'cra' :
#        perso1 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\cra1.png',region = resolution(17,4,65,82), confidence=0.4)
#        perso2 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\cra2.png',region = resolution(17,4,65,82), confidence=0.4)
#        perso3 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\cra3.png',region = resolution(17,4,65,82), confidence=0.4)
#        perso4 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\cra4.png',region = resolution(17,4,65,82), confidence=0.4)
    if leperso == 'sadi' :
        perso1 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\sadi1.png',region = resolution(17,4,65,82), confidence=0.7)
        perso2 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\sadi2.png',region = resolution(17,4,65,82), confidence=0.7)
        perso3 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\sadi3.png',region = resolution(17,4,65,82), confidence=0.7)
        perso4 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\sadi4.png',region = resolution(17,4,65,82), confidence=0.7)
#    if leperso == 'sacri' :
#        perso1 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\sacri1.png',region = resolution(17,4,65,82), confidence=0.4)
#        perso2 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\sacri2.png',region = resolution(17,4,65,82), confidence=0.4)
#        perso3 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\sacri3.png',region = resolution(17,4,65,82), confidence=0.4)
#        perso4 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\sacri4.png',region = resolution(17,4,65,82), confidence=0.4)
#    if leperso == 'enu' :
#        perso1 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\enu1.png',region = resolution(17,4,65,82), confidence=0.4)
#        perso2 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\enu2.png',region = resolution(17,4,65,82), confidence=0.4)
#        perso3 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\enu3.png',region = resolution(17,4,65,82), confidence=0.4)
#        perso4 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\enu4.png',region = resolution(17,4,65,82), confidence=0.4)
#    if leperso == 'eni' :
#        perso1 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\eni1.png',region = resolution(17,4,65,82), confidence=0.4)
#        perso2 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\eni2.png',region = resolution(17,4,65,82), confidence=0.4)
#        perso3 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\eni3.png',region = resolution(17,4,65,82), confidence=0.4)
#        perso4 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\eni4.png',region = resolution(17,4,65,82), confidence=0.4)
#    if leperso == 'féca' :
#        perso1 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\féca1.png',region = resolution(17,4,65,82), confidence=0.4)
#        perso2 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\féca2.png',region = resolution(17,4,65,82), confidence=0.4)
#        perso3 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\féca3.png',region = resolution(17,4,65,82), confidence=0.4)
#        perso4 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\féca4.png',region = resolution(17,4,65,82), confidence=0.4)
#    if leperso == 'panda' :
#        perso1 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\panda1.png',region = resolution(17,4,65,82), confidence=0.4)
#        perso2 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\panda2.png',region = resolution(17,4,65,82), confidence=0.4)
#        perso3 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\panda3.png',region = resolution(17,4,65,82), confidence=0.4)
#        perso4 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\panda4.png',region = resolution(17,4,65,82), confidence=0.4)
#    if leperso == 'xelor' :
#        perso1 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\xelor1.png',region = resolution(17,4,65,82), confidence=0.4)
#        perso2 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\xelor2.png',region = resolution(17,4,65,82), confidence=0.4)
#        perso3 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\xelor3.png',region = resolution(17,4,65,82), confidence=0.4)
#        perso4 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\xelor4.png',region = resolution(17,4,65,82), confidence=0.4)
#    if leperso == 'ougi' :
#        perso1 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\ougi1.png',region = resolution(17,4,65,82), confidence=0.4)
#        perso2 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\ougi2.png',region = resolution(17,4,65,82), confidence=0.4)
#        perso3 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\ougi3.png',region = resolution(17,4,65,82), confidence=0.4)
#        perso4 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\ougi4.png',region = resolution(17,4,65,82), confidence=0.4)
#    if leperso == 'roub' :
#        perso1 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\roub1.png',region = resolution(17,4,65,82), confidence=0.4)
#        perso2 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\roub2.png',region = resolution(17,4,65,82), confidence=0.4)
#        perso3 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\roub3.png',region = resolution(17,4,65,82), confidence=0.4)
#        perso4 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\roub4.png',region = resolution(17,4,65,82), confidence=0.4)
#    if leperso == 'huppermage' :
#        perso1 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\huppermage1.png',region = resolution(17,4,65,82), confidence=0.4)
#        perso2 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\huppermage2.png',region = resolution(17,4,65,82), confidence=0.4)
#        perso3 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\huppermage3.png',region = resolution(17,4,65,82), confidence=0.4)
#        perso4 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\huppermage4.png',region = resolution(17,4,65,82), confidence=0.4)
#    if leperso == 'steamer' :
#        perso1 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\steamer1.png',region = resolution(17,4,65,82), confidence=0.4)
#        perso2 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\steamer2.png',region = resolution(17,4,65,82), confidence=0.4)
#        perso3 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\steamer3.png',region = resolution(17,4,65,82), confidence=0.4)
#        perso4 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\steamer4.png',region = resolution(17,4,65,82), confidence=0.4)
#    if leperso == 'éca' :
#        perso1 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\éca1.png',region = resolution(17,4,65,82), confidence=0.4)
#        perso2 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\éca2.png',region = resolution(17,4,65,82), confidence=0.4)
#        perso3 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\éca3.png',region = resolution(17,4,65,82), confidence=0.4)
#        perso4 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\éca4.png',region = resolution(17,4,65,82), confidence=0.4)
#    if leperso == 'zobal' :
#        perso1 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\zobal1.png',region = resolution(17,4,65,82), confidence=0.4)
#        perso2 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\zobal2.png',region = resolution(17,4,65,82), confidence=0.4)
#        perso3 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\zobal3.png',region = resolution(17,4,65,82), confidence=0.4)
#        perso4 = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\les personnages\zobal4.png',region = resolution(17,4,65,82), confidence=0.4)
    print('le choix du perso est intégré')

def cbt():
    global clafinducbt
    quelperso()
    activermodecrea()
    reconnaissanceduterrain()
    fincbt()
    atk()
    if clafinducbt==1 :
        clafinducbt=0
        return
    time.sleep(2)
    terminertour()
    time.sleep(3)
    cbt()
#----------------------------------PARTIE COMBAT FIN--------------------------------------
#---------------------------------------LES DJS---------------------------------------
global salledj
salledj=3
def djpichon() :
        if salledj==0 :
            la = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\djs\djpichon1.png',confidence=0.7)
            click(la[0],la[1])
            time.sleep(0.3)
            la = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\djs\djpichon2.png',confidence=0.7)
            click(la[0],la[1])
            time.sleep(0.3)
            try :
                la = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\djs\djpichon3.png',confidence=0.7)
                click(la[0],la[1])
                time.sleep(0.3)
            except :
                la = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\djs\djpichon5.png',confidence=0.7)
                click(la[0],la[1])
                time.sleep(0.3)
            la = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\djs\djpichon4.png',confidence=0.7)
            click(la[0],la[1])
            time.sleep(0.3)            
            salledj+=1
        if salledj==1 :
            salledj+=1
            attaquerpichon()
            print("à faire")
        if salledj==2 :
            salledj+=1
            attaquerpichon()
        if salledj==3 :
            S()
            varrien=0
            while varrien == 0 :
                poisson = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\djs\poisson.png', region= resolution(17,4,65,82),confidence=0.4)
                if poisson[0] is not None :
                    click(poisson[0],poisson[1])
                    time.sleep(3)
                if poisson == None :
                    varrien=1
                    print("vois plus de poisson")
            if varrien == 0 :
                N()
                attaquerpichon()

#---------------------------------FARM CBT DEBUT----------------------------------------
def attaquerpichon() :
        pichon1=pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\ennemi\pichon1.png',confidence=0.5)
        pichon2=pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\ennemi\pichon2.png',confidence=0.5)
        pichon3=pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\ennemi\pichon3.png',confidence=0.5)
        pichon4=pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\ennemi\pichon4.png',confidence=0.5)
        if pichon3 :
            click(pichon3.x, pichon3.y)
            time.sleep(3)
            btnstartcbt = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\btnstartcbt.png',confidence=0.7)
            if btnstartcbt :
                click(btnstartcbt[0],btnstartcbt[1])
                cbt()
        if pichon1 :
            click(pichon1.x, pichon1.y)
            time.sleep(3)
            btnstartcbt = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\btnstartcbt.png',confidence=0.7)
            if btnstartcbt :
                click(btnstartcbt[0],btnstartcbt[1])
                cbt()
        if pichon2 :
            click(pichon2.x, pichon2.y)
            time.sleep(3)
            btnstartcbt = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\btnstartcbt.png',confidence=0.7)
            if btnstartcbt :
                click(btnstartcbt[0],btnstartcbt[1])
                cbt()
        if pichon4 :
            click(pichon4.x, pichon4.y)
            time.sleep(3)
            btnstartcbt = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\btnstartcbt.png',confidence=0.7)
            if btnstartcbt :
                click(btnstartcbt[0],btnstartcbt[1])
                cbt()

def farmcbt():
    global vary,varx, salledj
    if listecombo.get()=="dj pichon" :
        djpichon()
    if listecombo.get()=="pichons" :
        try :
            attaquerpichon()
        except :
            if varx==0 and vary==0:
                E()
            if varx==1 and vary==0 :
                N()
            if varx==1 and vary==1 :
                W()
            if varx==0 and vary==1 :
                S()
    main()
#---------------------------------La fonction banque----------------------------------------
varx,vary=0,0
#partie détection
def inventaire ():
    inventaireplein = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\inventaireplein.png', confidence=0.7)
    if inventaireplein :
        gotozebank()
#partie déplacement
def gotozebank():
    global varx, vary
    while varx!=0 :
        if varx<0 :
            E()
        if varx>0 :
            W()
    if varx==0 :
        while vary!=0 :
            if vary>0 :
                S()
            if vary<0 :
                N()
    if varx==0 and vary==0 :
        if choixzone.get()=="Champs d'astrub": #la y aura les différents lieu de farm
            E()
            S()
            S()
            S()
            S()
            depotastrub()
        if choixzone.get()=="Foret d'astrub" :
            N()
            E()
            E()
            E()
            E()
            E()
            N()
            N()
            N()
            E()
            depotastrub()
#partie dépot
def depotastrub():
    #y a moyen que y ai pas besoin de la changer meme si on est à frigost jsuis pas sûr IL FAUT CHANGER SELON LA BANQUE LA PLUS PROCHE
        laoufautcliquer = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\labanque\labanque.png', confidence=0.7)
        click(laoufautcliquer.x,laoufautcliquer.y)
        time.sleep(4)
        laoufautcliquer = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\labanque\lehibou.png', confidence=0.7)
        click(laoufautcliquer.x,laoufautcliquer.y)
        time.sleep(2)
        laoufautcliquer = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\labanque\consultercoffre.png', confidence=0.7)
        click(laoufautcliquer.x,laoufautcliquer.y)
        time.sleep(1)
        laoufautcliquer =pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\labanque\transfererressources1.png',region = resolution(46,4,52,82), confidence=0.7)
        click(laoufautcliquer.x,laoufautcliquer.y)
        time.sleep(2)
        laoufautcliquer =pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\labanque\transfererressources2.png', confidence=0.7)
        click(laoufautcliquer.x,laoufautcliquer.y)
        time.sleep(3)
        laoufautcliquer =pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\labanque\ptitecroix.png', confidence=0.7)
        click(laoufautcliquer.x,laoufautcliquer.y)
        time.sleep(1)
        laoufautcliquer =pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\labanque\sortirbanque.png', confidence=0.7)
        click(laoufautcliquer.x,laoufautcliquer.y)
        time.sleep(2)
        E()
        retouraufarm()
    #et aussi faudra vérifier si quand il varx et vary valent 0 le perso doit vérifier où il est et si il est pas là ou il faut bah c la d 

#il faudra faire une variable si t'es abo ou pas pour prendre le havre sac (bcp plus simple)

#partie retour
def retouraufarm():
    global varx,vary
    if choixzone.get()=="Champs d'astrub":
        N()
        N()
        N()
        N()
        W()
        varx,vary=0,0
        main()
    if choixzone.get()=="Foret d'astrub":
        E()
        varx,vary=0,0
        alleraufarm()

def alleraufarm():
    global varx, vary
    if choixzone.get()=="Foret d'astrub":
        S()
        S()
        W()
        W()
        W()
        W()
        W()
        S()
        varx,vary=0,0
    if choixzone.get()=="Champs d'astrub" :
        W()
        N()
        N()
        N()
        N()
        W()
        varx,vary=0,0
    if choixzone.get()=="dj pichon" :
        E(3)
        N(5)
        E()
        N(5)
        E(4)
        varx,vary=0,0
    main()
#--------------------INFOS OU CLIQUER POUR DROITE GAUCHE HAUT BAS------------------------------
def E (jaj=1):
    global varx
    while jaj>0 :
        click(resolution(92,50)[0],resolution(92,50)[1])
        varx+=1
        jaj+=-1
        time.sleep(7.5)
def N (jaj=1):
    global vary
    while jaj>0 :
        click(resolution(50,2)[0],resolution(50,2.5)[1])
        vary+=1
        jaj+=-1
        time.sleep(7.5)
def W (jaj=1):
    global varx
    while jaj>0 :
        click(resolution(2,50)[0],resolution(2,50)[1])
        varx+=-1
        jaj+=-1
        time.sleep(7.5)
def S (jaj=1):
    global vary
    while jaj>0 :
        click(resolution(50,88)[0],resolution(50,88)[1])
        vary+=-1
        jaj+=-1
        time.sleep(7.5)
#-------------------------Les fonctions du déplacement sur les maps--------------------------
varallerfarm=0

def smartchampstrub() :
    "c'est ce qui fais les déplacement choisis sur la map monde, COMMENCER A LA CASE [3;-22]"
    global var1,var2,var3,nbrdetourmax #var1 et var2 permettent de faire un schéma simple, var3 comptabilise les tours du bot
    if var3<nbrdetourmax :
        if var2<1 : #LA ON REMONTE EN ZIGZAG
            if var1<4 :
                E()
                var1=var1+1
                main()
            if var1==4 :
                N()
                var1=var1+1
                main()
            if 4<var1<10 :
                W()
                var1=var1+1
                main()
            if var1==10 :
                N()
                var1=0
                var2=var2+1
                main()
        if var2==1 : #LE DEMI-TOUR MES AYEUX
            if var1<3:
                E()
                var1=var1+1
                main()
            if var1==3:
                N()
                var1+=1
                main()
            if 3<var1<7:
                W()
                var1+=1
                main()
            if var1==7 :
                S()
                var1=0
                var2=+1
                main()
        if var2==3 : #LA REDESCENTE 
            if var1<3:
                E()
                var1+=1
                main()
            if var1==3:
                S()
                var1+=1
                main()
            if 3<var1<6:
                W()
                var1+=1
                main()
            if var1==6:
                S()
                var1+=1
                main()
            if var1==7 :
                var2+=1
                var1=0
                main()
        if var2==4 :
            if var1<4:
                E()
                var1+=1
                main()
            if var1==4:
                S()
                var1+=1
                main()
            if 4<var1<9:
                W()
                var1+=1
                main()
            if var1==9:
                S()
                var2+=1
                main()
        if var2==5 :
            N()
            var3=var3+1
            var1,var2=0,0
            main()
    if var3==nbrdetourmax :
        return
def smartforetstrub ():
    global var1,var2,var3, nbrdetourmax
    if var3==0 :
        print("jaj")
        if var2<4:
            if var1<3 :
                W()
                var1+=1
                main()
            if var1==3 :
                N()
                var1+=1
                main()
            if 3<var1<7 :
                E()
                var1+=1
                main()
            if var1==7 and var2<3 :
                N()
                var1=0
                var2+=1
                main()
            if var1==7 and var2==3 :
                var2+=1
                var1=0
                main()
        if var2==4 :
            if var1<2 :
                E()
                var1+=1
                main()
            if var1==2:
                N()
                var1=0
                var2=0
                var3+=1
                main()
    if var3==1 :
        if var2<3:
            if var1<4 :
                W()
                var1+=1
                main()
            if var1==4 :
                N()
                var1+=1
                main()
            if 4<var1<8 :
                E()
                var1+=1
                main()
            if var1==9 :
                N()
                var2+=1
                var1=0
                main()
        if var2==3 :
            if var1<2:
                N()
                var1+=1
                main()
            if var1==2 :
                S()
                var1+=1
                main()
            if var1==3 :
                S()
                var1=0
                var2=0
                var3+=1
                main()
    if var3==2 :
        if var2<3 :
            if var1<4:
                W()
                var1+=1
                main()
            if var1==4 :
                S()
                var1+=1
                main()
            if 4<var1<9 :
                E()
                var1+=1
                main()
            if var1==9:
                S()
                var2+=1
                var1=0
                main()
        if var2==3:
            if var1==0 :
                W()
                var1+=1
                main()
            if var1==1 :
                W()
                var3+=1
                var2=0
                var1=0
                main()
    if var3==3 :
        if var2<4:
            if var1<4 :
                W()
                var1+=1
                main()
            if var1==4 :
                S()
                var1+=1
                main()
            if 4<var1<8 :
                E()
                var1+=1
                main()
            if var1==8 and var2!=3 :
                S()
                var1=0
                var2+=1
                main()
            if var1==8 and var2==3 :
                var2=0
                var1=0
                var3=0
                nbrdetourmax+=1                
                main()
#COSKIHJDDSJSLDKJOIEJLDKSJSDLKJSIHAIUJSBKHJIVBPHVPUHYGVPUYFAJHBWXPIUHSGVQPUHYQGPIQDUGIDQUGH
def smartchoix():
    global var1,var2,var3,taillezone
    print(taillezone0)
    if taillezone0.get()==0 :
        print("gros bade, faut mettre une valeur de taille de zone")
        return
    xmax=int(taillezone0.get())
    ymax=int(taillezone1.get())
    if var3==0 :
        if var2<ymax :
            if var1<xmax :
                W()
                var1+=1
                main()
            if var1==xmax :
                N()
                var1+=1
                var2+=1
                main()
            if xmax<var1<2*xmax :
                E()
                var1+=1
                main()
            if var1==2*xmax :
                N()
                var2+=1
                var1=0
                main()
        if var2==ymax :
            var3+=1
            var2=0
            main()
    if var3==1 :
        if var2<ymax :
            if 0<var1<xmax :
                W()
                var1+=1
                main()
            if var1==xmax :
                S()
                var1+=1
                var2+=1
                main()
            if xmax<var1<2*xmax :
                E()
                var1+=1
                main()
            if var1==2*xmax :
                S()
                var1=0
                var2+=1
                main()
        if var2==ymax:
            if var1==0 :
                var1,var2,var3=0,0,0
                main()
            if xmax<var1<2*xmax  :
                E()
                var1+=1
                main()
            if var1==2*xmax :
                var1,var2,var3=0,0,0
                main()




#-------------------------------------MAAAAAAIIIIIINNNJUUUUUUUUUJJJJ-----------------------------------------

def main():
    global varallerfarm
    btnstartcbt = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\btnstartcbt.png',confidence=0.7)
    variablesmartgro=0
    farmcbt()
    inventaire()
    if btnstartcbt :#la on va rentrer le cbt
        click(btnstartcbt[0],btnstartcbt[1])
        cbt()
    if ble0.get()==0 :
        print("c'est le jaj")
    if ble0.get()==1 :
        leblé1= pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\Lesressources\bleptn1.png',region = resolution(17,4,65,82),confidence=0.6)
        leblé2= pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\Lesressources\bleptn2.png',region = resolution(17,4,65,82),confidence=0.6) 
        if leblé1:
            click(leblé1[0],leblé1[1])
            time.sleep(5)
            variablesmartgro=1
            main()
            return()
        if leblé2:
            click(leblé2[0],leblé2[1])
            time.sleep(5)
            variablesmartgro=1
            main()
            return()
    if orge0.get()==1 :
        orge1= pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\Lesressources\orge1.png', region= resolution(17,4,65,82), confidence=0.6)
        orge2= pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\Lesressources\orge2.png', region= resolution(17,4,65,82), confidence=0.6)
        orge3= pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\Lesressources\orge3.png', region= resolution(17,4,65,82), confidence=0.6)
        if orge3:
            click(orge3[0],orge3[1])
            time.sleep(5)
            variablesmartgro=1
            main()
            return()
        if orge1:
            click(orge1[0],orge1[1])
            time.sleep(5)
            variablesmartgro=1
            main()
            return()
        if orge2:
            click(orge2[0],orge2[1])
            time.sleep(5)
            variablesmartgro=1
            main()
            return()
    if ortie0.get()==1 :
        ortie1= pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\Lesressources\ortie1.png', region=resolution(17,4,65,82), confidence=0.8)
        ortie2= pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\Lesressources\ortie2.png',  region= resolution(17,4,65,82), confidence=0.8)
        ortie3= pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\Lesressources\ortie3.png',  region=resolution(17,4,65,82), confidence=0.8)
        if ortie1==True :
            click(ortie1[0],ortie1[1])
            time.sleep(5)
            variablesmartgro=1
            main()
            return()
        if ortie2==True :
            click(ortie2[0],ortie2[1])
            time.sleep(5)
            variablesmartgro=1
            main()
            return()
        if ortie3==True :
            click(ortie3[0],ortie3[1])
            time.sleep(5)
            variablesmartgro=1
            main()
            return()
    if frene0.get()==1 :
        frene1= pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\Lesressources\frene1.png', region=resolution(17,4,65,82), confidence=0.9)
        frene2= pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\Lesressources\frene2.png',  region=resolution(17,4,65,82), confidence=0.6)
        frene3= pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\Lesressources\frene3.png',  region=resolution(17,4,65,82), confidence=0.6)
        if frene1:
            click(frene1[0],frene1[1])
            time.sleep(5)
            variablesmartgro=1
            main()
            return()
        if frene2:
            click(frene2[0],frene2[1])
            time.sleep(5)
            variablesmartgro=1
            main()
            return()
        if frene3:
            click(frene3[0],frene3[1])
            time.sleep(5)
            variablesmartgro=1
            main()
            return()
    if chataignier0.get()==1 :
        chataignier1= pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\Lesressources\chataignier1.png', region= resolution(17,4,65,82), confidence=0.8)
        chataignier2= pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\Lesressources\chataignier2.png', region= resolution(17,4,65,75), confidence=0.9)
        chataignier3= pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\Lesressources\chataignier3.png', region= resolution(17,4,65,75), confidence=0.9)
        if chataignier1:
            click(chataignier1[0],chataignier1[1])
            time.sleep(5)
            variablesmartgro=1
            main()
            return()
        if chataignier2:
            click(chataignier2[0],chataignier2[1])
            time.sleep(5)
            variablesmartgro=1
            main()
            return()
        if chataignier3:
            click(chataignier3[0],chataignier3[1])
            time.sleep(5)
            variablesmartgro=1
            main()
            return()
    if noyer0.get()==1:
        noyer1=pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\Lesressources\noyer1.png', region= resolution(17,4,65,78), confidence=0.7)
        noyer2=pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\Lesressources\noyer2.png', region= resolution(17,4,65,82), confidence=0.7)
        noyer3=pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\Lesressources\noyer3.png', region= resolution(17,4,65,82), confidence=0.7)
        noyer4=pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\Lesressources\noyer4.png', region= resolution(20,4,62,82), confidence=0.7)
        if noyer1:
            click(noyer1[0],noyer1[1])
            time.sleep(5)
            variablesmartgro=1
            main()
            return()
        if noyer2:
            click(noyer2[0],noyer2[1])
            time.sleep(5)
            variablesmartgro=1
            main()
            return()
        if noyer3:
            click(noyer3[0],noyer3[1])
            time.sleep(5)
            variablesmartgro=1
            main()
            return()
        if noyer4:
            click(noyer4[0],noyer4[1])
            time.sleep(5)
            variablesmartgro=1
            main()
            return()
    if trefle0.get()==1 :
        trefle1= pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\Lesressources\trefle1.png',region= resolution(17,4,65,82), confidence=0.7)
        trefle2= pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\Lesressources\trefle2.png', region=resolution(17,4,65,82), confidence=0.7)
        trefle3= pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\Lesressources\trefle3.png', region=resolution(17,4,65,82), confidence=0.7)
        trefle4= pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\Lesressources\trefle4.png', region=resolution(17,4,65,82), confidence=0.7)
        if trefle1:
            click(trefle1[0],trefle1[1])
            time.sleep(5)
            variablesmartgro=1
            main()
            return()
        if trefle2:
            click(trefle2[0],trefle2[1])
            time.sleep(5)
            variablesmartgro=1   
            main()
            return()
        if trefle3:
            click(trefle3[0],trefle3[1])
            time.sleep(5)
            variablesmartgro=1
            main()
            return()
        if trefle4:
            click(trefle4[0],trefle4[1])
            time.sleep(5)
            variablesmartgro=1
            main()
            return()
    if sauge0.get()==1:
        sauge1=pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\Lesressources\sauge1.png', region= resolution(17,4,65,82), confidence=0.7)
        sauge2=pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\Lesressources\sauge2.png', region= resolution(17,4,65,82), confidence=0.7)
        if sauge1:
            click(sauge1[0],sauge1[1])
            time.sleep(5)
            variablesmartgro=1
            main()
            return()
        if sauge2:
            click(sauge2[0],sauge2[1])
            time.sleep(5)
            variablesmartgro=1
            main()
            return()
    if menthe0.get()==1 :
        menthe1= pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\Lesressources\menthe1.png',region= resolution(17,4,65,82), confidence=0.7)
        menthe2= pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\Lesressources\menthe2.png', region=resolution(17,4,65,82), confidence=0.7)
        if menthe1:
            click(menthe1[0],menthe1[1])
            time.sleep(5)
            variablesmartgro=1
            main()
            return()
        if menthe2:
            click(menthe2[0],menthe2[1])
            time.sleep(5)
            variablesmartgro=1
            main()
            return()
    if lin0.get()==1 :
        lin1= pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\Lesressources\lin1.png', region= resolution(17,4,65,82), confidence=0.7)
        lin2= pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\Lesressources\lin2.png', region= resolution(17,4,65,82), confidence=0.7)
        if lin1:
            click(lin1[0],lin1[1])
            time.sleep(5)
            variablesmartgro=1
            main()
            return()
        if lin2:
            click(lin2[0],lin2[1])
            time.sleep(5)
            variablesmartgro=1
            main()
            return()
    if avoine0.get()==1 :
        avoine1= pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\Lesressources\avoine1.png', region= resolution(17,4,65,82), confidence=0.7)
        avoine2= pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\Lesressources\avoine2.png', region= resolution(17,4,65,82), confidence=0.7)
        if avoine1:
            click(avoine1[0],avoine1[1])
            time.sleep(5)
            variablesmartgro=1
            main()
            return()
        if avoine2:
            click(avoine2[0],avoine2[1])
            time.sleep(5)
            variablesmartgro=1
            main()
            return()
    if fer0.get()==1:
        fer1=pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\Lesressources\fer1.png', region= resolution(17,4,65,82), confidence=0.7)
        fer2=pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\Lesressources\fer2.png', region= resolution(17,4,65,82), confidence=0.7)
        if fer1:
            click(fer1[0],fer1[1])
            time.sleep(5)
            variablesmartgro=1
            main()
            return()
        if fer2:
            click(fer2[0],fer2[1])
            time.sleep(5)
            variablesmartgro=1
            main()
            return()
    if bronze0.get()==1:
        bronze1=pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\Lesressources\bronze1.png', region= resolution(17,4,65,82), confidence=0.7)
        bronze2=pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\Lesressources\bronze2.png', region= resolution(17,4,65,82), confidence=0.7)
        if bronze1:
            click(bronze1[0],bronze1[1])
            time.sleep(5)
            variablesmartgro=1
            main()
            return()
        if bronze2:
            click(bronze2[0],bronze2[1])
            time.sleep(5)
            variablesmartgro=1
            main()
            return()
    if cuivre0.get()==1:
        cuivre1=pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\Lesressources\cuivre1.png', region= resolution(17,4,65,82), confidence=0.7)
        cuivre2=pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\Lesressources\cuivre2.png', region= resolution(17,4,65,82), confidence=0.7)
        if cuivre1:
            click(cuivre1[0],cuivre1[1])
            time.sleep(5)
            variablesmartgro=1
            main()
            return()
        if cuivre2:
            click(cuivre2[0],cuivre2[1])
            time.sleep(5)
            variablesmartgro=1
            main()
            return()
    if variablesmartgro==0 :
        if choixzone.get() == "Champs d'astrub" :
            smartchampstrub()
        if choixzone.get() == "Foret d'astrub" :
            smartforetstrub()
        if choixzone.get()== "à la main" :
            smartchoix()
        if choixzone.get()==None :
            main()
#----------------La fonction alleraufarm(),aller au point de farm--------------

#def alleraufarm():
    #if abo :

    #if not abo: 
    #ultra complexe faudrait prendre en compte le fait que t'ai une dd autopilote ce genre de bail
#------------------------La fonction connexion---------------------------------
global jij
jij=0
def connexion():
    #faut utiliser open() pour ouvrir un fichier, utiliser un fichier de stockage jsp pour les mdps et tt en mode jaaaj
    global jij
    while jij==0 :    
        subprocess.call(["C:\Program Files\Ankama\Ankama Launcher\Ankama Launcher.exe"])
        time.sleep(5)
        lancer = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\btnjouer.png', confidence=0.7)
        if lancer :
            click(lancer.x,lancer.y)
            jij=1
        if lancer == None :
            time.sleep(5)
            connexion()
    while jij==1 :
        time.sleep(5)
        lancerperso = pyautogui.locateCenterOnScreen(r'C:\Users\albin\OneDrive\Documents\CODING\dofus\jouerj.png', confidence=0.8)
        if lancerperso==None:
            connexion()
        if lancerperso==True :
            click(lancerperso.x,lancerperso.y)
            time.sleep(5)
#------------------------Fin fonction connexion------------------------------
resolx,resoly=1920,1080
#la fonction qui transforme la resolution rentrée pour adapter l'ensemble du main
def resolution(a=0,b=0,c=0,d=0): #a et b sera pour les valeurs de taille et hauteur
    global resolx,resoly
    if a :
        ac=eval(str(int(resolx)*a/100))
    if b :
        bc=eval(str(int(resoly)*b/100))
    if c :
        cc=eval(str(int(resolx)*c/100))
    if d :
        dc=eval(str(int(resoly)*d/100))
    if a and b and c and d :
        return ( int(ac),int(bc),int(cc),int(dc))
    if a and b and not c and not d :
        return ( int(ac),int(bc))
    if a and not b and not c and not d :
        return(int(ac))
def globalresol():
    global resolx,resoly
    resolx = resolx1.get()
    resoly = resoly1.get()
    print(resoly1.get,resolx1.get)
    if not resolx and not resoly :
        resolx=1920
        resoly=1080
        print ('jij')
    #vraiment dur vu que je peux mettre aucun calcul dans les parenthèsej
    #je peux mettre une nouvel variable local a qui prend la valeur 1, 2, 3, 4 ou 5 et à chaque fois ça fera un truc précis

    
#-------------------------la fenetre d'affichjaj---------------------------

#-----------------------fenetre de base----------------------------------
fen=Tk()
fen.title("La botance")
fen.geometry("1400x500")

#-----------------------------Les checkbuttons qui en active/désactive d'autres--------
def togglemineur() :
    fer.toggle()
    bronze.toggle()
    cuivre.toggle()
def togglebucheron():
    frene.toggle()
    chataignier.toggle()
    noyer.toggle()
def togglepaysan():
    ble.toggle()
    orge.toggle()
    lin.toggle()
    avoine.toggle()
def togglealchimiste():
    ortie.toggle()
    sauge.toggle()
    menthe.toggle()
    trefle.toggle()

#------------------------------les boutons qui vont lancer les différentes commandes--------------------
b1=Button(fen,text='pour ouvrir ankama cash', command=connexion)
b1.grid(column=0,row=9)
b2=Button(fen,text="a une pro man", command=quit)
b2.grid(column=0,row=8)
b3=Button(fen,text='lets go', command=main)
b3.grid(column=0,row=4)
b4=Button(fen,text='aller au farm depuis le zap', command=alleraufarm)
b4.grid(column=0, row=5)
#peut etre pas besoin de le lier à une fonction, les valeurs changent de manière global
#---------------------------------------pour la résolution------------------------------------------
resolx1,resoly1=IntVar(),IntVar()
resolutionx=Label(fen, text="Met ta résolution des x ici (moi 1920) : ")
resolutiony=Label(fen, text="Met ta résolution des y ici (moi 1080) : ")
resolutionx.grid(column=2,row=6,sticky='E')
resolutiony.grid(column=2,row=7,sticky='E')
laresolutionx=Entry(fen,textvariable =resolx1)
laresolutiony=Entry(fen,textvariable =resoly1)
laresolutionx.grid(column=3, row=6, padx=5)          #pour l'ensemble du programme
laresolutiony.grid(column=3, row=7, padx=5)
boutresol=Button(fen,text="prendre en compte résolution notée",command=globalresol)
boutresol.grid(column=3,row=8)

#------------------------------------La variable pm en mode posé------------------------------------
listepm=[2,3,4,5,6,7]
nbrpm=ttk.Combobox(fen, values=listepm)
nbrpm.grid(column=2, row=2, sticky='W')
Label(text='nombre de pm, 3 par défaut : ').grid(column=1,row=2,sticky='E')
#abo0=IntVar()
#---------------------Les variables ressources et les Checkbutton +abopasabo----------
#abopasabo=Checkbutton(fen,text="Si t'es abo coche la case",variable=abo0, onvalue=1,offvalue=0)
#abopasabo.grid(column=0, row=12)
ble0,orge0,ortie0 ,frene0,chataignier0, trefle0,lin0,avoine0, fer0, bronze0,cuivre0, menthe0,noyer0=IntVar(),IntVar(),IntVar(),IntVar(),IntVar(), IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar()
ble=Checkbutton(fen,text="blé", variable=ble0, onvalue=1,offvalue=0)
orge=Checkbutton(fen,text="orge", variable=orge0, onvalue=1,offvalue=0)
ortie=Checkbutton(fen,text="ortie", variable=ortie0, onvalue=1,offvalue=0)
menthe=Checkbutton(fen,text="menthe", variable=menthe0, onvalue=1,offvalue=0)
frene=Checkbutton(fen,text="frene", variable=frene0, onvalue=1,offvalue=0)
chataignier=Checkbutton(fen,text="chataignier", variable=chataignier0, onvalue=1,offvalue=0)
noyer=Checkbutton(fen,text='noyer', variable=noyer0, onvalue=1,offvalue=0)
trefle=Checkbutton(fen,text="trefle à 4 feuilles", variable=trefle0, onvalue=1,offvalue=0)
lin=Checkbutton(fen,text="lin", variable=lin0, onvalue=1,offvalue=0)
avoine=Checkbutton(fen,text='avoine', variable=avoine0, onvalue=1,offvalue=0)
fer=Checkbutton(fen,text='fer', variable=fer0, onvalue=1,offvalue=0)
bronze=Checkbutton(fen,text='bronze', variable=bronze0, onvalue=1, offvalue=0)
cuivre=Checkbutton(fen,text='cuivre', variable=cuivre0, onvalue=1,offvalue=0)
sauge0=IntVar()
sauge=Checkbutton(fen,text='sauge', variable=sauge0, onvalue=1,offvalue=0)



#-----------------------choix perso (liste déroulante)--------------------
listeperso=["iop","osa","elio","cra","ougi","sacri","sadi","sram","féca", "xelor","panda","enu", "eni","roub","huppermage","éca","steamer","zobal"]
listecombo=ttk.Combobox(fen, values=listeperso)
listecombo.grid(column=3,row=2,stick='s')
#----------------------------LES LABELS DU GUI------------------------------
infoquoicocher= Label(fen, text='Coche les ressources que tu veux récupérer :')
choixperso=Label(fen, text='choisis ton personnage :')
choixperso.grid(column=3, row=1, stick='s')

metierpaysan=Checkbutton(fen,text='Paysan',command=togglepaysan)
metieralchimiste=Checkbutton(fen,text="Alchimiste",command=togglealchimiste)
metierbucheron=Checkbutton(fen,text='Bucheron',command=togglebucheron)
metiermineur=Checkbutton(fen,text='Mineur',command=togglemineur)
#---------------LES .GRID UNIQUEMENT DES RESSOURCES ET METIERS----------------------
infoquoicocher.grid(column=1,row=10, stick='w')

metierpaysan.grid(column=1,row=11,stick='s')
ble.grid(column=1,row=12, stick='w')
orge.grid(column=1,row=13, stick='w')
avoine.grid(column=1,row=14, stick='w')
lin.grid(column=1,row=15, stick='w')

metieralchimiste.grid(column=2,row=11,stick='s')
ortie.grid(column=2,row=12, stick='w')
trefle.grid(column=2,row=13, stick='w')
menthe.grid(column=2,row=14, stick='w')
sauge.grid(column=2, row=15,stick='w')

metierbucheron.grid(column=3,row=11,stick='s')
frene.grid(column=3,row=12, stick='w')
chataignier.grid(column=3,row=13, stick='w')
noyer.grid(column=3, row=14,stick='w')

metiermineur.grid(column=4, row=11,stick='s')
fer.grid(column=4, row=12,stick='w')
bronze.grid(column=4, row=13,stick='w')
cuivre.grid(column=4, row=14,stick='w')

#-------------------LE CHOIX DE LA ZONE DE FARM ENTRE AUTRE------------------

Label(fen,text="Ici il y a les différentes zones de farm : ").grid(column=0, row=20)
listezonefarm=["Champs d'astrub", "Foret d'astrub","pichons", "piou", "dj pichon", "à la main"]
choixzone=ttk.Combobox(fen, values=listezonefarm)
choixzone.grid(column=0, row=21)

#-----------SI il veut farm une zone en particulier--------------------
taillezone0,taillezone1=IntVar(), IntVar()

Label(fen,text="Si tu a choisis à la main, coche tes ressources").grid(column=2, row=20)
Label(fen,text="puis la taille de la zone de recherche ici").grid(column=2, row=21)
Label(fen,text="12,12 par exemple déplacera de 12 vers la gauche puis zigzag jusqu'à 12 map en haut").grid(column=2, row=22)
Entry(fen,textvariable=taillezone0).grid(column=2, row=23)
Entry(fen,textvariable=taillezone1).grid(column=2, row=24)


fen.mainloop()
#pour la fonction créa faudrait faire que si elle a été activé elle puisse pas etre réactivé
