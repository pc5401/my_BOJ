function solution(num1, num2) {
    const v = num1 % num2;
    var answer = (num1 - v) / num2;
    return answer;
}