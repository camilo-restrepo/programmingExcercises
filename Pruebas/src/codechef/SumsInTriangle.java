package codechef;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

//Sums in a triangle 
public class SumsInTriangle {

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader (System.in));
		int n = Integer.parseInt(bf.readLine());
		while(n>0){
			int size=Integer.parseInt(bf.readLine());;
			int[][] mat = new int[size][size];
			int j=0;
			while(j!=size){
				String str = bf.readLine();
				String[] s = str.split(" ");
				for (int i = 0; i < s.length; i++) {
					mat[j][i] = Integer.parseInt(s[i]);
				}
				j++;
			}
			
			int[][] maxSum = new int[size][size];
			maxSum[0][0]=mat[0][0];
			for (int i = 1; i < mat.length; i++) {
				for (int k = 0; k < i+1; k++) {
					if(k==0){
						maxSum[i][k]=mat[i][k]+maxSum[i-1][k];
					}
					else if(k==i){
						maxSum[i][k]=mat[i][k]+maxSum[i-1][k-1];
					}
					else{
						maxSum[i][k]=mat[i][k]+Math.max(maxSum[i-1][k-1], maxSum[i-1][k]);
					}
				}
			}
			int max=0;
			for (int i = 0; i < maxSum.length; i++) {
				if(maxSum[maxSum.length-1][i]>max)
					max=maxSum[maxSum.length-1][i];
			}
			System.out.println(max);
			n--;
		}
	}
}
