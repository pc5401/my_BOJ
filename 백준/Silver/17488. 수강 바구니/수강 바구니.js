const readline = require('readline');

const rl = readline.createInterface({
  input : process.stdin,
  output : process.output
})

let input = [];

rl.on('line', (line)=>{
  input.push(line.split(' ').map(Number));
  if (input[0][0]*2 + 2 <= input.length) rl.close();
})

rl.on('close', ()=>{
  const [N, M] = input[0];
  const L = [...input[1]];
  const fst = input.slice(2, N+2);
  const scd = input.slice(N+2);
  const result = solve(N, M, L, fst, scd);
  for (let i = 0, j = result.length; i < j; i++){
    console.log(result[i].length > 0 ? result[i].join(' ') : '망했어요')
  }
})

/**
 * 문제 풀이 함수
 * @param {Number} N 
 * @param {Number} K 
 * @param {Array.<Number>} L 
 * @param {Array.<Array.<Number>>} fst 
 * @param {Array.<Array.<Number>>} scd 
 * @returns {Array.<Array.<Number>>}  
 */
const solve = (N, M, L, fst, scd) => {
  let rtn = Array.from({length : N}, ()=> []);
  // 1 차 수강 신청
  let fstLecture = classRegistration(M, fst);
  checkResult(L, fstLecture, rtn);

  // 2차 수강 신청
  let scdLecture = classRegistration(M, scd);
  checkResult(L, scdLecture, rtn);

  return rtn.map(e=>e.sort((a,b)=>a-b));
}

/**
 * 수강 신청 처리 함수
 * 
 * @param {Number} M - 과목 수
 * @param {Array.<Array.<Number>>} list - 학생들이 신청한 과목 리스트
 * @returns {Array.<Array.<Number>>} 각 과목별로 수강 신청한 학생 번호 배열
 */
const classRegistration = (M, list) => {
  let lecture = Array.from({length : M}, ()=> []);
  list.forEach((std, num)=>{
    std.some((e)=>{
      if (e === -1) return true;
      lecture[e-1].push(num);
      return false;
    })
  })
  return lecture
}

/**
 * 수강 신청 결과 확인 함수
 * 
 * @param {Array.<Number>} L - 각 과목의 남은 수강제한인원 배열
 * @param {Array.<Array.<Number>>} fstLecture - 과목별 수강 신청 학생 배열
 * @param {Array.<Array.<Number>>} rtn - 학생별 수강 성공 과목 배열
 */
const checkResult = (L, fstLecture, rtn) => {
  fstLecture.forEach((lct, i)=>{
    if (lct.length > L[i]){
      L[i] = 0;
    }else{
      L[i] -= lct.length;
      lct.forEach(e=>rtn[e].push(i+1));
    }
  })
}