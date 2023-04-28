import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    // 첫 줄 여러 정수 값을 입력받습니다.
    String[] data = br.readLine().split(" ");
    int H = Integer.parseInt(data[0]);
    int W = Integer.parseInt(data[1]);
    int N = Integer.parseInt(data[2]);
    int M = Integer.parseInt(data[3]);
    
    int cnt = 0;

    for (int i=0; i<H; i += (1+N))
    {
      for (int j=0; j<W; j += (1+M))
      {
        cnt++;
      }
    }
    System.out.println(cnt);
  }
}
