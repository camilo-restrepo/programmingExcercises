package codechef;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		boolean p1 = false;
		boolean p2 = false;
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(bf.readLine());
		int max = 0;
		int s1 = 0;
		int s2 = 0;
		while(n>0){
			String str[] = bf.readLine().split(" ");
			s1 += Integer.parseInt(str[0]);
			s2 += Integer.parseInt(str[1]);
			int resta  = s1-s2;
			if(resta>0){
				if(resta>=max){
					p1=true;
					p2=false;
					max=resta;
				}				
			}else{
				resta=Math.abs(resta);
				if(resta>=max){
					p1=false;
					p2=true;
					max=resta;
				}
			}
			n--;
		}
		if(p1)
			System.out.println("1 "+max);
		else
			System.out.println("2 "+max);
	}
}