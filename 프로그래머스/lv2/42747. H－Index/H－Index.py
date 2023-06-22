def solution(citations):
    citations.sort(reverse=True)
    h_index = max(map(min, enumerate(citations, start=1)))
    return h_index