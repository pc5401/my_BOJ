function solution(s){
    let stack = [];
    
    for (const e of s){
        if (e === "("){
            stack.push(e);
        }else if (stack.length === 0){
            return false
        }else{
            stack.pop();
        }
    }

    if (stack.length === 0){
        return true;
    }
    return false;
}