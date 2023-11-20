def solution(A,B):
    answer = 0
    A.sort()
    B.sort(key=lambda x:-x)
    
    for i, e in enumerate(A):
        answer += (e*B[i])

    return answer