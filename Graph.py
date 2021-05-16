import queue
import random
import time
import numpy as np
import matplotlib.pyplot as plt


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
            proved = False
            break
    return proved


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


def test(n, max_e):
    adj_list = generate_graph(n, max_e)
    for i in range(len(adj_list)):
        if i % 500 == 0:
            print(i)
        if not bfs(adj_list, i, 6):
            print("Disproved")
            return False
    else:
        print("Proved")
        return True


def main():
    n = int(input("Number of vertices: "))
    test_results = np.zeros(15)
    for max_e in range(1, 15):
        print(max_e)
        disproved = 0
        proved = 0
        while proved + disproved < 10:
            result = test(n, max_e)
            if result:
                proved += 1
            else:
                disproved += 1
        print(proved / (proved + disproved))
        test_results[max_e] = proved / (proved + disproved)
    x = plt.figure()
    plt.plot(test_results)
    plt.xlabel('max_e')
    plt.ylabel('Fraction passing the test')
    x.savefig('Wykres.png', dpi=120)
if __name__ == '__main__':
    main()
