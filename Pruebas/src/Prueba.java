import java.io.Serializable;
import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Calendar;
import java.util.Collections;
import java.util.Date;
import java.util.GregorianCalendar;
import java.util.HashSet;
import java.util.Hashtable;
import java.util.List;
import java.util.Observable;
import java.util.PriorityQueue;
import java.util.Random;
import java.util.Set;
import java.util.regex.Matcher;
import java.util.regex.Pattern;


public class Prueba {



	public static void main(String[] args) throws ParseException {
		String s = "a";
		System.out.println(s.contains("A"));
		
//		int i = 15;
//		int count =0;
//		while(i!=0){
//			System.out.println("i: "+i);
//			System.out.println("i-1:" +(i-1));
//			i=i&(i-1);
//			System.out.println(i);
//			count++;
//		}
//		System.out.println("c: "+count);

		//		String rgString = "^[\\w-_]+(\\.[\\w]+)*@[\\w]+(\\.[\\w]+)*\\.[a-z]{2,4}$";
		//		CharSequence inputStr = "c@u..co";
		//		Pattern pattern = Pattern.compile(rgString);
		//		Matcher matcher = null;
		//		matcher = pattern.matcher(inputStr);
		//
		//		if (matcher.matches()) {
		//			System.out.println("Matched");
		//		} else {
		//			System.out.println("Not Matched");
		//		}

//		int[] input = {1,2,3,4};
//		int result=1;
//		int[] output = new int[input.length];
//		for(int i=0;i<input.length;i++)
//		{
//			output[i]=result;
//			result*=input[i];
//		}
//		result=1;
//		for(int i=input.length-1;i>=0;i--)
//		{
//			output[i]*=result;
//			result*=input[i];
//		}
//		
//		for (int i = 0; i < output.length; i++) {
//			System.out.print(output[i]+" ");
//		}
	}

	public static int excel(String col) {
		int n = col.length();
		if (n < 1)
			return 0;
		int base = (int)('Z' - 'A');
		int result = col.charAt(n - 1) - 'A' + 1;
		for (int i = n - 2; i >= 0; i--) {
			result += (col.charAt(i) - 'A' + 1) * base;
			base *= base;
		}
		return result;  
	}


	public static boolean isPrime(int n){
		if(n<0)return isPrime(-n);
		if(n<5 || n%2==0 || n%3==0) return (n==2||n==3);
		int maxP = (int)Math.sqrt(n)+2;
		for(int i = 5; i< maxP; i+=6)
			if(n%i==0 || n%(i+2)==0)
				return false;
		return true;
	}

	public static int kOrder(int[] array, int k, int min, int max){
		if(min==max){
			return array[min];
		}
		int pivot = (min+max)/2;
		int n = pivot-min+1;
		if(k==n){
			return array[pivot];
		}
		if(k<n){
			return kOrder(array, k, min, pivot-1);
		}else{
			return kOrder(array, k-n, pivot+1, max);
		}
	}

	public static int[] minMax(int[] array, int min, int max){
		int[] resp = new int[2];
		if(min==max){
			resp[0]=array[min];
			resp[1]=array[min];
		}else if(min+1==max){
			if(array[min]>array[max]){
				resp[0]=array[min];
				resp[1]=array[max];
			}else{
				resp[0]=array[max];
				resp[1]=array[min];
			}
		}else{
			int mid=(min+max)/2;
			int[] a1=minMax(array, min, mid);
			int[] a2= minMax(array, mid+1, max);

			resp[0]=(a1[0]>a2[0])?a1[0]:a2[0];
			resp[1]=(a1[1]<a2[1])?a1[1]:a2[1];
		}
		return resp;
	}

	public static List<Integer> primeFactors(int number) {
		int n = number; 
		List<Integer> factors = new ArrayList<Integer>();
		for (int i = 2; i <= n; i++) {
			while (n % i == 0) {
				factors.add(i);
				n /= i;
			}
		}
		return factors;
	}

	public static String reverse ( String s ) {
		int length = s.length(), last = length - 1;
		char[] chars = s.toCharArray();
		for ( int i = 0; i < length/2; i++ ) {
			char c = chars[i];
			chars[i] = chars[last - i];
			chars[last - i] = c;
		}
		return new String(chars);
	}


	public static int binarySearch(int[] array, int number, int min, int max){
		if(array.length==0)
			return -1;
		else{
			int mid = (int) Math.floor((min+max)/2);
			if(array[mid]==number)
				return mid;
			else if(array[mid]>number)
				return binarySearch(array, number, min, mid-1);
			else
				return binarySearch(array, number, mid+1, max);
		}
	}

	public static boolean isPalind(int val){
		int i = 0;
		int k = val;

		while(k!=0){
			i=(i<<1)|(k&1);
			k=k>>1;
		}
		return (i==val)?true:false;
	}

	public static int NumberOfSetBits(int i)
	{
		int count=0;
		while(i!=0){
			i=i&(i-1);
			count++;
		}
		return count;
	}

	public static int fib(int n){
		int f1 = 0;
		int f2=1;
		for(int i = 0 ; i < n ; i++){
			int temp = f1+f2;
			f1=f2;
			f2=temp;
		}
		return f2;
	}

	public static int fib1(int n){
		return (n<=1)?n:fib1(n-1)+fib1(n-2);
	}

}
