import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int T = Integer.parseInt(br.readLine());
    for (int i = 0; i < T; i++) {
        String[] data = br.readLine().split(" ");
        int N = Integer.parseInt(data[0]);
        String words = data[1];
        StringBuilder res = new StringBuilder();
        for (int k = 0; k < words.length(); k++){
          for (int j = 0; j < N; j++){
            res.append(words.charAt(k));
          }
        }
        System.out.println(res);
    } 
  }
}
