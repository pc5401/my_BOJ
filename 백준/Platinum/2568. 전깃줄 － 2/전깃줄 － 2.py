import sys
import bisect

def main():
    input = sys.stdin.readline
    
    N = int(input())
    lines = [tuple(map(int, input().split())) for _ in range(N)]
    lines.sort(key=lambda x: x[0])
    
    B = [lines[i][1] for i in range(N)]
    
    LISval = []            
    pos_of_length = []     
    prev = [-1] * N
    
    for i in range(N):
        val = B[i]
        
        if not LISval or val > LISval[-1]:
            # LIS 확장
            LISval.append(val)
            

            if len(pos_of_length) > 0:
                prev[i] = pos_of_length[-1]
            else:
                prev[i] = -1
                
            pos_of_length.append(i)
        
        else:
            pos = bisect.bisect_left(LISval, val)
            LISval[pos] = val
            
            pos_of_length[pos] = i
            
            if pos == 0:
                prev[i] = -1
            else:
                prev[i] = pos_of_length[pos-1]
    
    L = len(LISval)
    print(N - L) 
    
    remains = set()
    idx = pos_of_length[L-1]
    
    while idx != -1:
        remains.add(idx)
        idx = prev[idx]
    
    removed = []
    for i in range(N):
        if i not in remains:
            removed.append(lines[i][0])
    

    removed.sort()
    for r in removed:
        print(r)

if __name__ == "__main__":
    main()
