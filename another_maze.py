import cv2
import numpy as np
from random import randint
import pprint
from collections import deque

#def DFS(graph, start, visited=None):
#    if visited is None:
#        visited = set()
#    visited.add(start)
#    for next in graph[start] - visited:
#        DFS(graph, next, visited)
#    return visited
#

#graph = {'0': set(['1', '2']),
#         '1': set(['0', '3', '4']),
#         '2': set(['0']),
#         '3': set(['1']),
#         '4': set(['2', '3'])}
#
#DFS(graph, '0')
#pp = pprint.PrettyPrinter()


def maze2graph(maze):
    height = len(maze)
    width = len(maze[0]) if height else 0
    graph = {(i, j): [] for j in range(width) for i in range(height) if not maze[i][j]}
    for row, col in graph.keys():
        if row < height - 1 and not maze[row + 1][col]:
            graph[(row, col)].append(("S", (row + 1, col)))
            graph[(row + 1, col)].append(("N", (row, col)))
        if col < width - 1 and not maze[row][col + 1]:
            graph[(row, col)].append(("E", (row, col + 1)))
            graph[(row, col + 1)].append(("W", (row, col)))
    return graph

def find_path_bfs(maze):
    start, goal = (1, 1), (len(maze) - 2, len(maze[0]) - 2)
    queue = deque([("", start)])
    visited = set()
    graph = maze2graph(maze)
    while queue:
        pp.pprint(queue)
        path, current = queue.popleft()
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        for direction, neighbour in graph[current]:
            queue.append((path + direction, neighbour))
    return "NO WAY!"

#N = int(input("Введите количество строк в матрице: "))
#M = int(input("введите количество столбцуов в матрице: "))
#A = [[0]*M for i in range(N)]
#Присвоенине элементам матрицы значений 0 или 1, 1 - стена, 0 - отсутствие стены
#for i in range(N):
#    for j in range(M):
#        A[i][j] = int(input(f"A[{i}][{j}]="))
#    print()

#Вывод полученнго лабиринта:

#for i in range(len(A)):
#    for j in range(len(A[i])):
        #print(A[i][j], end = ' ')
#    print()

#pp = pprint.PrettyPrinter()
#pp.pprint(find_path_bfs(A))
