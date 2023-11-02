function solution(n, lost, reserve) {
    const lst = Array.from({length : n},()=>1);
    lost.sort((a, b) => a - b);
    reserve.sort((a, b) => a - b);
    
    for (i of lost) lst[i-1]--;
    for (i of reserve) lst[i-1]++;
    
    for (let i = 0; i < n; i++) {
        if (lst[i] === 2 && i > 0 && lst[i - 1] === 0) {
            lst[i]--;
            lst[i - 1]++;
        } else if (lst[i] === 2 && i < n - 1 && lst[i + 1] === 0) {
            lst[i]--;
            lst[i + 1]++;
        }
    }

    return lst.filter(i => i > 0).length;
}