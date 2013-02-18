package codechef;

//import java.io.BufferedReader;
import java.io.IOException;
//import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;

//Turbo Sort
public class Main2 {

	public static void main(String[] args) throws IOException {
//		BufferedReader r = new BufferedReader(new InputStreamReader (System.in));
		Scanner sc = new Scanner(System.in);
//		int n = Integer.parseInt(r.readLine());
		int n = Integer.parseInt(sc.nextLine());
		int[] arr = new int[n];
		int  j = 0;
		while(n>0){
			arr[j] = Integer.parseInt(sc.nextLine());
			j++;
			n--;
		}
		Arrays.sort(arr);
		for(int i = 0; i < arr.length ; i++)
			System.out.println(arr[i]);
	}
}