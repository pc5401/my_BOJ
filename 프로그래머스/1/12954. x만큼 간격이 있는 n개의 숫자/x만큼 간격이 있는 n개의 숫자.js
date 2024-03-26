function solution(x, n) {
    var answer = Array.from({length:n}, (e,i)=>(i+1)*x)
    return answer;
}