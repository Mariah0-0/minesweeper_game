# -*- coding: utf-8 -*-
"""
Created on Wed May 26 19:14:16 2021

@author: maria"""

import random

def display():
    print()
    print('      | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |')
    print('   ---+----------------------------------------')
    for r in range(10):
        print('    '+str(r)+' ', end='')
        for c in range(10):
            if vis[r][c]==1:
                print('| '+str(puzzle[r][c]), end=' ')
            else:
                print('|  ', end=' ')
        print('|')
        print('   ---|---+---+---+---+---+---+---+---+---+---+')

def inprc():
    try:
        while True:
            while True:
                row = int(input('\nRow: '))
                if row in range(0,10):
                    break
                else:
                    print('Row doesn\'t exist')
            while True:
                col = int(input('Column: '))
                if col in range(0,10):
                    break
                else:
                    print('Column doesn\'t exist')
            if vis[row][col]==1:
                print('\nCell not valid')
            else:
                break
        return row,col
    except:
        print('\nInvalid value')
        return inprc()

def sur(r,c):
    sur = []
    for r1 in range(0,10):
        for c1 in range(0,10):
            if r==r1 and c==c1:
                continue
            if r1 in range(r-1,r+2) and c1 in range(c-1,c+2):
                sur.append((r1,c1))
    return sur

def createpuzzle(rc):
    for i in range(12):
        while True:
            row = random.randint(0,9)
            col = random.randint(0,9)
            if puzzle[row][col]=='*':
                continue
            if rc[0]==row and rc[1]==col:
                continue
            if (row,col) in sur(rc[0],rc[1]):
                continue
            puzzle[row][col]='*'
            break
    for r in range(0,10):
        for c in range(0,10):
            if puzzle[r][c]==0:
                count = 0
                for i in sur(r,c):
                    if puzzle[i[0]][i[1]]=='*':
                        count+=1
                puzzle[r][c]=count

def makevis(rc):
    vis[rc[0]][rc[1]] = 1
    if puzzle[rc[0]][rc[1]]==0:
        for cell in sur(rc[0],rc[1]):
            if vis[cell[0]][cell[1]]==0:
                makevis(cell)

def makeallvis():
    for r in range(0,10):
        for c in range(0,10):
            vis[r][c]=1

def play():
    display()
    fm = inprc()
    createpuzzle(fm)
    makevis(fm)
    display()
    while True:
        move = inprc()
        if puzzle[move[0]][move[1]]=='*':
            makeallvis()
            print()
            display()
            print('\nGAME OVER :(')
            break
        makevis(move)
        won = True
        for r in range(0,10):
            for c in range(0,10):
                if vis[r][c]==0 and puzzle[r][c]!='*':
                    won = False
        if won==True:
            makeallvis()
            print()
            display()
            print('\nCONGRATULATIONS! :D')
            break
        print()
        display()

puzzle = [[0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0]]

vis = [[0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0]]

play()