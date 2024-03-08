from typing import List


def is_ordered(length: int, beards: List[int]) -> int:
    if length < 3:
        return True
    
    if beards[0] < beards[1]:
        for i in range(1, length):
            if beards[i-1] > beards[i]:
                return False
    
    elif beards[0] > beards[1]:
        for i in range(1, length):
            if beards[i-1] < beards[i]:
                return False



    return True

def main():
    T = int(input())
    print("Gnomes:")

    for _ in range(T):
        beards = list(map(int, input().split()))
        if is_ordered(len(beards), beards):
            print("Ordered")
        else:
            print("Unordered")

if __name__ == "__main__":
    main()