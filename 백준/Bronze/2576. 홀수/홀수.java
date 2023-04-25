import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int minVal = Integer.MAX_VALUE;
		int sumVal = 0;
        int value = 0;
        
        for (int i = 0; i < 7; i++)
        {
            value = sc.nextInt();
            if (value % 2 == 1){
                sumVal += value;
                if (minVal > value)
                minVal = value;
            }
        }
        
        if (sumVal == 0){
            System.out.println(-1);
        }
        else{
            System.out.println(sumVal);
            System.out.print(minVal);
        }
	}
}