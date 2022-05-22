# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 14:04:00 2021

@author: Kanwal
"""

def drawField(field):
    for row in range(5):
       
        for column in range(5):
              print(field[row][column], end=" ")
        print("\n")    
player = 1
currentField = [['-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-']]

rowCount = [4, 4, 4, 4, 4]
check=0
drawField(currentField)
while(check==0):
    print(f'Players {player} turn')
    moveColumn = int(input('Column: '))
   
    if player == 1:
        if currentField[rowCount[moveColumn]][moveColumn] == '-':
            currentField[rowCount[moveColumn]][moveColumn] = 'X'
            rowCount[moveColumn] -= 1
            player = 2
    else:
        if currentField[rowCount[moveColumn]][moveColumn] == '-':
            currentField[rowCount[moveColumn]][moveColumn] = 'O'
            rowCount[moveColumn] -= 1
            player = 1
    drawField(currentField)
    for row in range(5):
     if currentField[row][0]=='X':
             if currentField[row][1]=='X':
                   if currentField[row][2]=='X':
                        if currentField[row][3]=='X':
                             if currentField[row][4]=='X':
                                  print("player 1 wins")
                                  check=1
     if currentField[row][0]=='O':
             if currentField[row][1]=='O':
                   if currentField[row][2]=='O':
                        if currentField[row][3]=='O':
                             if currentField[row][4]=='O':
                                  print("player 2 wins")
                                  check=1
                                 
    if currentField[0][0]=='O':
             if currentField[1][1]=='O':
                   if currentField[2][2]=='O':
                        if currentField[3][3]=='O':
                             if currentField[4][4]=='O':
                                  print("player 1 wins")
                                  check=1
    if currentField[0][0]=='X':
             if currentField[1][1]=='X':
                   if currentField[2][2]=='X':
                        if currentField[3][3]=='X':
                             if currentField[4][4]=='X':
                                  print("player 2 wins")
                                  check=1    