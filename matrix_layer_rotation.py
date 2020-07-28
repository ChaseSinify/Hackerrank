#!/bin/python3
import math
import os
import random
import re
import sys

"""
matrix: a 2D array of integers
rot: an integer that represents the rotation factor
rows x cols
"""
def matrixRotation(matrix, rot, rows, cols):
    layers = [] #holds each "ring" of the matrix to make % rotation easy for each ring
    maxDepth = (min(rows, cols) // 2) - 1
    rowLength = cols #helpers for depth math, easier var names
    colLength = rows #helpers for depth math, easier var names

    #building the layer arrays
    for depth in range(0, maxDepth+1, 1):
        layers.append([]) #add a new layer
        
        #top row
        topRow = []
        for tr in range(depth, ((rowLength-1)-depth)+1):
            topRow.append(matrix[depth][tr])
        if topRow != []:
            for tri in topRow:
                layers[depth].append(tri)

        #right wall
        rightRow = [] #for now, this is just the wall  between topLeft and bottomLeft
        for rr in range(depth+1, ((colLength-1)-depth)):
            rightRow.append(matrix[rr][(rowLength-1)-depth]) #changed this to rowlength
        if rightRow != []:
            for rri in rightRow:
                layers[depth].append(rri)

        #bottom row
        bottomRow = []
        for br in range(depth, ((rowLength-1)-depth)+1):
            bottomRow.append(matrix[colLength-1-depth][br])
        if bottomRow != []:
            for bri in bottomRow[::-1]:
                layers[depth].append(bri)
        
        #left wall
        leftRow = [] #for now, this is just the wall  between topLeft and bottomLeft
        for lr in range(depth+1, ((colLength-1)-depth)):
            leftRow.append(matrix[lr][depth])
        if leftRow != []:
            for lri in leftRow[::-1]:
                layers[depth].append(lri)
    
    # print(layers) #testing
    #rotation
    for i in range(len(layers)):
        rotFactor = rot % len(layers[i])
        # start = len(layers[i]) - rotFactor #this is right rotation, we need left
        layers[i] = layers[i][rotFactor:] + layers[i][:rotFactor]
    # print(layers) #testing

    #output
    #rebuilding matrix --> should print directly once we hav working solution
    outMatrix = matrix.copy()
    for depth in range(len(layers)):
        # print(f'Depth: {depth}')
        tbSize = rowLength - (2 * depth) #represents length of top and bottom in full
        wallSize = colLength - (2 * depth) - 2 #len of walls BETWEEN top andbottom
        # print(f'tbSize: {tbSize}')
        # print(f'wallSize: {wallSize}')
        for i in range(len(layers[depth])):
            #sizes
            #example: row length = 7; col length = 6
            #for depth of 0, tbSize with be 7, wallSize will be 4
            #for depth of 1, tbSize with be 5, wallSize will be 2
            #for depth of 2(last), tbSize will be 3, wallSize will be 0
            #break
            if i < tbSize - 1: 
                outMatrix[depth][i+depth] = layers[depth][i]
                # print(f'1 | i:{i} | Touching matrix: {depth, i+depth}')
            elif i >= (tbSize - 1) and i < (tbSize + wallSize):
                outMatrix[depth+(i-(tbSize-1))][(rowLength-1)-depth] = layers[depth][i]
                # print(f'2 | i:{i} | Touching matrix: {depth+(i-(tbSize-1)), (rowLength-1)-depth}')
            elif i+depth >= (tbSize + wallSize) and i < (tbSize * 2 + wallSize):
                #changed the "i" after the and from i+depth to just i
                outMatrix[wallSize+1+depth][(rowLength - 1) - depth - (i - tbSize - wallSize)] = layers[depth][i]
                # print(f'3 | i:{i} | Touching matrix: {wallSize+1+depth, (rowLength - 1) - depth - (i - tbSize - wallSize)}')
            elif i + depth >= (tbSize * 2) + wallSize:
                outMatrix[(wallSize) - (i-(tbSize*2+wallSize) - depth)][depth] = layers[depth][i]
                # print(f'4 | i:{i} | Touching matrix: {(wallSize) - (i-(tbSize*2+wallSize) - depth), depth}')
        # break
    #testing
    # print(outMatrix)
    for _ in outMatrix:
        for __ in _:
            print(__, end = " ")
        print()


if __name__ == '__main__':
    mnr = input().rstrip().split()
    rows = int(mnr[0])
    cols = int(mnr[1])
    rot = int(mnr[2])
    matrix = []

    for _ in range(rows):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, rot, rows, cols)

