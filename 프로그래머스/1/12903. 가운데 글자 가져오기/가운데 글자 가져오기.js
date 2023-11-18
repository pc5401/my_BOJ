function solution(s) {
    if (s.length % 2){
        let num = Math.floor(s.length/2);
        return s[num];
    }else{
        let num = s.length / 2;
        return s[num-1]+s[num];
    }
}