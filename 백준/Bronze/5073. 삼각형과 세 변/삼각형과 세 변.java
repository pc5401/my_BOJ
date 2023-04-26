import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {  // 백준 풀 때는 Main으로 변경
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        while (true){
            String[] inputLine = br.readLine().split(" ");
            int a = Integer.parseInt(inputLine[0]);
            int b = Integer.parseInt(inputLine[1]);
            int c = Integer.parseInt(inputLine[2]);
            // 합
            int sumV = a + b + c;
            // 최대값
            int maxV = Math.max(Math.max(a, b), c);
            
            if (a == 0 && b == 0 && c == 0){
                break;
            }
            else if ((sumV - maxV) <= maxV){
                System.out.println("Invalid");
            }
            else if (a == b && b == c){
                System.out.println("Equilateral");
            }
            else if (a != b && b != c && a != c){
                System.out.println("Scalene");
            }
            else{
                System.out.println("Isosceles");
            }
        }
    }
}