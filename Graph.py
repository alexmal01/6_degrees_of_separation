import queue
import random
import numpy as np


def bfs(adj_list, starting_vertex, limit):
    proved = True
    bfs_queue = queue.Queue()
    visited_list = [False for _ in range(len(adj_list))]
    depth = 1
    bfs_queue.put((starting_vertex, depth))
    while not bfs_queue.empty():
        v, cur_depth = bfs_queue.get()
        if cur_depth > limit:
            break
        for j in range(len(adj_list[v])):
            u = adj_list[v][j]
            if visited_list[u] == 0:
                visited_list[u] = 1
                bfs_queue.put((u, cur_depth + 1))
    # print(visited_list)
    for i in visited_list:
        if not i:
            print("Disproved")
            proved = False
            break
    return proved


def generate_graph(n, max_e):
    adj_list = [[] for _ in range(n)]
    for i in range(n):
        adj_number = random.randint(1, max_e)
        for j in range(adj_number):
            adj = i
            while adj == i:
                adj = random.randint(0,n-1)
            adj_list[i].append(adj)
            adj_list[adj].append(i)
    return adj_list


def main():
    adj_list = generate_graph(n=5000, max_e=8)
    # print(adj_list)
    for i in range(len(adj_list)):
        print(i)
        if not bfs(adj_list, i, 6):
            break
    else:
        print("Proved")


if __name__ == '__main__':
    main()
