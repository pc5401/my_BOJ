import * as readline from 'readline';

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let N: number = 0; // 테스트 케이스의 개수
let p: number = 0; // 현재 테스트 케이스에서 고려해야 할 선수의 수
const result: string[] = []; // 결과를 저장할 배열
let currentTestPlayers: number = 0; // 현재 테스트 케이스에서 처리된 선수의 수
let maxPrice: number = 0; // 현재까지의 최대 가격
let maxPlayer: string = ''; // 현재까지의 최고가 선수의 이름

rl.on('line', (line: string) => {
  if (N === 0) {
    // 첫 번째 줄 처리: 테스트 케이스의 개수 설정
    N = parseInt(line, 10);
  } else if (p === 0) {
    // 새 테스트 케이스 시작: 선수의 수 설정
    p = parseInt(line, 10);
    // 현재 테스트 케이스에 대한 값 초기화
    currentTestPlayers = 0;
    maxPrice = 0;
    maxPlayer = '';
  } else {
    // 선수 정보 처리
    let [priceStr, player] = line.split(' ');
    let price = parseInt(priceStr, 10);
    if (price > maxPrice) {
      maxPrice = price;
      maxPlayer = player;
    }
    currentTestPlayers++;
    if (currentTestPlayers === p) {
      // 테스트 케이스의 마지막 선수: 결과에 추가
      result.push(maxPlayer);
      p = 0; // 다음 테스트 케이스를 위해 p 리셋
    }
  }

  if (result.length === N) {
    // 모든 테스트 케이스가 처리된 후에 출력하고 인터페이스 종료
    rl.close();
  }
});

rl.on('close', () => {
  result.forEach((player) => {
    console.log(player);
  });
  process.exit(0);
});
