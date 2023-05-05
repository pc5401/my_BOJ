import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String A = br.readLine().toLowerCase();
    String B = br.readLine().toLowerCase();
    int n = A.length();
    int m = B.length();
    int cnt = 0;

    int[] lst = new int[m];

    for (int i=0; i < n; i++){
      for (int j=0; j < m;j ++){
        if (A.charAt(i) == B.charAt(j) && lst[j] == 0){
          lst[j] = 1;
          cnt++;
          break;
        }
      }
    }
    System.out.println((n+m)-(cnt*2));
  }
}
