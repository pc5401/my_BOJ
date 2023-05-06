import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    // input 값
    int N = Integer.parseInt(br.readLine());
    String[] names = new String[N];
    for (int i = 0; i < N; i++){ // 입력값 배열에 저장
      names[i] = br.readLine();
    }

    int[] cnt = new int[26]; // 갯수
    for (int i = 0; i < N; i++){ 
      cnt[names[i].charAt(0) - 'a']++;
    }

    // 문자 개수
    StringBuilder res = new StringBuilder();
    for (int i = 0; i < 26; i++){
      if (cnt[i] >=5)
      res.append((char)(i+'a'));
    }

    // 결과값
    if (res.length() == 0){
      System.out.println("PREDAJA");
    } else {
      System.out.println(res.toString());
    }
  } // end:main
}
