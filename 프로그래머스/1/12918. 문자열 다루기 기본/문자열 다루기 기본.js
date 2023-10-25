function solution(s) {
    if (s.length != 4 && s.length != 6) return false;
    for (let e of s){
        if (e < '0' || e > '9') return false
    }
    return true;
}