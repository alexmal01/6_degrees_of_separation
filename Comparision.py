import queue
import random
import numpy as np
import time


def generate_graph_np(n, max_e):
    adj_list = np.ndarray((n, max_e), int, np.array([-1] * (n * max_e)))
    for i in range(n):
        adj_number = random.randint(1, max_e)
        for j in range(adj_number):
            adj = i
            while adj == i or adj_list[adj][max_e - 1] != -1:
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


def generate_graph(n, max_e):
    adj_list = [[] for _ in range(n)]
    for i in range(n):
        adj_number = random.randint(1, max_e)
        for j in range(adj_number):
            if len(adj_list[i]) == max_e:
                break
            adj = i
            while adj == i or len(adj_list[adj]) >= max_e:
                adj = random.randint(0, n - 1)
            adj_list[i].append(adj)
            adj_list[adj].append(i)
    return adj_list


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
    for i in visited_list:
        if not i:
            print("Disproved")
            proved = False
            break
    return proved


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


def main():
    start = time.time()
    adj_list = generate_graph(n=12000, max_e=11)
    end = time.time()
    print(f"Time of graph generation using base: {end - start}")
    start = time.time()
    adj_list_np = generate_graph_np(n=12000, max_e=11)
    end = time.time()
    print(f"Time of graph generation using NumPy: {end - start}")
    adj_list_cp = [[] for _ in range(len(adj_list))]
    for i in range(adj_list_np.shape[0]):
        for j in range(adj_list_np.shape[1]):
            if adj_list_np[i][j] == -1:
                break
            adj_list_cp[i].append(adj_list_np[i][j])
    start = time.time()
    for i in range(len(adj_list)):
        if i % 250 == 0:
            print(i)
        if not bfs(adj_list_cp, i, 6):
            break
    else:
        print("Proved")
    end = time.time()
    print(f"Graph search execution time using base: {end - start}")
    start = time.time()
    for i in range(adj_list_np.shape[0]):
        if i % 250 == 0:
            print(i)
        if not bfs(adj_list_np, i, 6):
            break
    else:
        print("Proved")
    end = time.time()
    print(f"Graph search execution time using NumPy: {end - start}")

if __name__ == '__main__':
    main()
