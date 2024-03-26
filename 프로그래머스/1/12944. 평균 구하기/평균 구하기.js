function solution(arr) {
    var answer = arr.reduce((acc, curr)=>acc+curr, 0) / arr.length;
    return answer;
}