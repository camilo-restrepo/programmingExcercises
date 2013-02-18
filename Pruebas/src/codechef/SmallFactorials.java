package codechef;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;

//Small Factorials
public class SmallFactorials {

	public static void main(String[] args) throws IOException {
		BigInteger[] arr = new BigInteger[101];
		arr[0]=BigInteger.ZERO;
		arr[1]=BigInteger.ONE;
		for(int i = 2 ; i < arr.length ;i++){
			arr[i] = arr[i-1].multiply(new BigInteger(i+""));
		}
		
		BufferedReader r = new BufferedReader(new InputStreamReader (System.in));
		int n = Integer.parseInt(r.readLine());
		while(n>0){
			System.out.println(arr[Integer.parseInt(r.readLine())].toString());
			n--;
		}
	}
}
