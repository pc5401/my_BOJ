function solution(n, k) {
    const v = parseInt(n/10)
    var answer = n * 12000 + (k-v) * (2000);
    return answer;
}