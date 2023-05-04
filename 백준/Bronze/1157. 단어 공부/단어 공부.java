import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map.Entry;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // input 값
        String words = br.readLine().toUpperCase();
        // 해쉬맵 사용
        HashMap<Character, Integer> map = new HashMap<>();
        // 문자 순회하면서 값 더하기
        for (int i = 0; i < words.length(); i++) {
            char word = words.charAt(i);
            if (map.containsKey(word)) {
                map.put(word, map.get(word) + 1);
            } else {
                map.put(word, 1);
            }
        }

        // 최대값을 가지는 키 찾기
        Character maxKey = null;
        int maxValue = Integer.MIN_VALUE;
        int maxCnt = 0;
        
        for (Entry<Character, Integer> entry : map.entrySet()) {
            if (entry.getValue() > maxValue) {
                maxKey = entry.getKey();
                maxValue = entry.getValue();
                maxCnt = 0;
            }else if (entry.getValue() == maxValue){
                maxCnt++;
            }
        }
        if (maxCnt > 0){
            System.out.println('?');
        }else{
            System.out.println(maxKey); 
        }
    } // end:main
}
