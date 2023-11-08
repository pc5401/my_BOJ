import sys
import collections
input = sys.stdin.readline

if __name__ == "__main__":
    N, W, L = map(int, input().split())
    trucks = collections.deque(map(int, input().split()))
    time = 0
    bridge = collections.deque([0 for _ in range(W)])

    for truck in trucks:
        if truck + sum(bridge) <= L:
            bridge.popleft()
            bridge.append(truck)
            time += 1
            continue

        while 1:
            if truck + sum(bridge) > L:
                bridge.popleft()
                bridge.append(0)
                time += 1
            else:
                bridge.pop()
                bridge.append(truck)
                break

    time += W
    print(time)