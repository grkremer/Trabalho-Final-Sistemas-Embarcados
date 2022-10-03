import serial
import time
import sys
from playsound import playsound


# make sure the 'COM#' is set according the Windows Device Manager
ser = serial.Serial('COM5', 9600, timeout=1)
time.sleep(2)

def printNumber(num):
    num = num%8
    if num == 1:
        playsound("resources/8.mp3")
    elif num == 2:
        playsound("resources/7.mp3")
    elif num == 3:
        playsound("resources/6.mp3")
    elif num == 4:
        playsound("resources/5.mp3")
    elif num == 5:
        playsound("resources/4.mp3")
    elif num == 6:
        playsound("resources/3.mp3")
    elif num == 7:
        playsound("resources/2.mp3")
    elif num == 0:
        playsound("resources/1.mp3")


def printLetter(num):
    num = (num -1) // 8
    if num == 0:
        playsound("resources/A.mp3")
    elif num == 1:
        playsound("resources/B.mp3")
    elif num == 2:
        playsound("resources/C.mp3")
    elif num == 3:
        playsound("resources/D.mp3")
    elif num == 4:
        playsound("resources/E.mp3")
    elif num == 5:
        playsound("resources/F.mp3")
    elif num == 6:
        playsound("resources/G.mp3")
    elif num == 7:
        playsound("resources/H.mp3")


def openBoard():
    with open('board.txt', 'r') as f:
        data = f.read()
    data = data.replace("[","").replace("]", "").replace("'","").replace(",","").replace(" ","")
    data = data.splitlines()
    return data

def printBoard(board, num):
    collum = (num - 1) % 8
    row = (num - 1) // 8
    if row <= 8 and collum <= 8 and row >=0 and collum >= 0:
        res = board[row][collum]
        if res == 'P':
            playsound("resources/Peao.mp3")
            playsound("resources/Branco.mp3")
        elif res == 'R':
            playsound("resources/Torre.mp3")
            playsound("resources/Branco.mp3")
        elif res == "N":
            playsound("resources/Cavalo.mp3")
            playsound("resources/Branco.mp3")
        elif res == "B":
            playsound("resources/Bispo.mp3")
            playsound("resources/Branco.mp3")
        elif res == "K":
            playsound("resources/Rei.mp3")
            playsound("resources/Branco.mp3")
        elif res == "Q":
            playsound("resources/Rainha.mp3")
            playsound("resources/Branco.mp3")
        elif res == "_":
            playsound("resources/Vazio.mp3")


for i in range(5000):
    line = ser.readline()   # read a byte
    if line:
        string = line # convert the byte string to a unicode string
        num = int.from_bytes(string, byteorder='little') - 658688
        print(num)
        printLetter(num)
        printNumber(num)
        board = openBoard()
        printBoard(board,num)
        

ser.close()

