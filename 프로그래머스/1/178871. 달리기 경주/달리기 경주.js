function solution(players, callings) {
    
    let playerMap = new Map();
    
    players.forEach((e,i)=> {
        playerMap.set(e,i);
    });
    
    callings.forEach((e,i)=>{
        let rank = playerMap.get(e);
        let temp = players[rank-1];
        players[rank-1] = e;
        players[rank] = temp;
        playerMap.set(e, rank-1);
        playerMap.set(temp, rank);
    })
    
    return players;
}