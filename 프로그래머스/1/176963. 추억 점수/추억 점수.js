function solution(name, yearning, photo) {
    let answer = [];
    const nameMap = new Map();
    name.forEach((e,i)=>nameMap.set(e,yearning[i]));
    photo.forEach(member=>{
        let ans = 0;
        member.forEach(e=>{
            if (nameMap.has(e)) {
            ans += nameMap.get(e)
            }
        })
        answer.push(ans);
    })
    
    return answer;
}