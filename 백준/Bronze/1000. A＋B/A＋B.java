import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    // 첫 줄 정수 값을 입력받습니다.
    String[] data = br.readLine().split(" ");
    int A = Integer.parseInt(data[0]);
    int B = Integer.parseInt(data[1]);
    
    System.out.println(A+B);

  }
}
