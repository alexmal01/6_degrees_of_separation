import queue
import random
import numpy as np
import time


def bfs_np(adj_list, starting_vertex, limit):
    proved = True
    bfs_queue = queue.Queue()
    visited_list = np.zeros(len(adj_list), int)
    depth = 1
    bfs_queue.put((starting_vertex, depth))
    while not bfs_queue.empty():
        v, cur_depth = bfs_queue.get()
        if cur_depth > limit:
            break
        for j in range(adj_list.shape[1]):
            u = adj_list[v][j]
            if u == -1:
                break
            if visited_list[u] == 0:
                visited_list[u] = 1
                bfs_queue.put((u, cur_depth + 1))
    for i in visited_list:
        if i == 0:
            print("Disproved")
            proved = False
            break
    return proved


def generate_graph_np(n, max_e):
    random.seed(123)
    adj_list = np.ndarray((n, max_e), int, np.array([-1] * (n * max_e)))
    # print(adj_list)
    for i in range(n):
        adj_number = random.randint(1, max_e)
        for j in range(adj_number):
            adj = i
            while adj == i:
                adj = random.randint(0, n - 1)
            k = 0
            l = 0
            for h in range(adj_list.shape[1]):
                if adj_list[i][h] == -1:
                    k = h
                    break
            for h in range(adj_list.shape[1]):
                if adj_list[adj][h] == -1:
                    l = h
                    break
            adj_list[i][k] = adj
            adj_list[adj][l] = i
    return adj_list


def main():
    adj_list_np = generate_graph_np(n=2000, max_e=10)
    for i in range(adj_list_np.shape[0]):
        # print(i)
        if not bfs_np(adj_list_np, i, 6):
            break
    else:
        print("Proved")


if __name__ == '__main__':
    main()
