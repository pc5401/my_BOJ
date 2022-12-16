function solution(num_list) {
    res = []
    const l = num_list.length
    for (let i = l-1; i > -1; i--){
        res.push(num_list[i])
    }
    var answer = res;
    return answer;
}