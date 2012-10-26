package euler;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Pbt81 {

	/**
	 * @param args
	 * @throws IOException 
	 */
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new FileReader("./data/in81"));
		String str = bf.readLine();
		
		int size = 80;
		int[][] mat = new int[size][size];
		int j = 0;
		while(str!=null){
			String s[] = str.split(",");
			for (int i = 0; i < s.length; i++) {
				mat[j][i]=Integer.parseInt(s[i]);
			}
			j++;
			str = bf.readLine();
		}
		
		int[][] minSum = new int[size][size];
		minSum[0][0]=mat[0][0];
		
		for (int i = 0; i < mat.length; i++) {
			for (int k = 0; k < mat.length; k++) {
				if(minSum[i][k]!=0){
					minSum[i][k]=mat[i][k];
				}else{
					int enK = Integer.MAX_VALUE;
					int enI = Integer.MAX_VALUE;
					if(k>0){
						enK = minSum[i][k-1];
					}
					if(i>0){
						enI = minSum[i-1][k];
					}
					minSum[i][k]=mat[i][k] + Math.min(enK, enI);
				}
			}
		}
		System.out.println(minSum[size-1][size-1]);
//		for (int i = 0; i < mat.length; i++) {
//			for (int k = 0; k < mat.length; k++) {
//				System.out.print(minSum[i][k]+" ");
//			}
//			System.out.println();
//		}
	}
}