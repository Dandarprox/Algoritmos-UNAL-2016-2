from sys import stdin
import heapq

t = int(stdin.readline())
for _ in range(t):
    heap = []
    nhilos, nprocesos = map(int, stdin.readline().strip().split(" "))
    priority = [int(x) for x in stdin.readline().strip().split(" ")]

    z = 0
    counter = 0
    while z != nhilos:
        print z, 0
        linea += 1
        if priority[counter] == 0:
            z-= 1
        else:
            heapq.heappush(heap, (priority[counter], z))
        counter += 1
        if counter == nprocesos:
            break
        z+=1

    while counter != nprocesos:
        tiempo, hilo = heapq.heappop(heap)
        heapq.heappush(heap, (tiempo + priority[counter], hilo))
        print hilo, tiempo
        linea += 1
        counter += 1
