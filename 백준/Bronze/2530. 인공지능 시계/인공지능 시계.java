import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    // 첫 줄 여러 정수 값을 입력받습니다.
    String[] data = br.readLine().split(" ");
    int H = Integer.parseInt(data[0]);
    int M = Integer.parseInt(data[1]);
    int S = Integer.parseInt(data[2]);
    
    int time = Integer.parseInt(br.readLine());

    int timeS = time % 60;
    int timeM = time / 60;
    int timeH = timeM / 60;
    timeM = timeM % 60;
    
    // 초 단위 계산
    S = S + timeS;
    if (S > 59)
    {
      S = S % 60;
      M += 1;
    }
    
    // 분 단위 계산
    M = M + timeM;
    if (M > 59)
    {
      M = M % 60;
      H += 1;
    }
    // 시 단위 계산
    H = (H + timeH) % 24;

    // 출력
    System.out.print(H + " " + M + " " + S);
  }
}
