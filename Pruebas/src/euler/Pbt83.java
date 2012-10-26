package euler;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class Pbt83 {

	/**
	 * @param args
	 * @throws IOException 
	 */
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new FileReader("./data/in83"));
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
		for (int i = 0; i < mat.length; i++) 
			for (int k = 0; k < mat.length; k++) 
				minSum[i][k]= Integer.MAX_VALUE;

		minSum[0][0]=mat[0][0];

		for(int l = 0; l < size*size ; l++){
			for (int i = 0; i < mat.length; i++) {
				for (int k = 0; k < mat.length; k++) {
					if(!(i==0 && k==0)){
						int up=Integer.MAX_VALUE;
						int down=Integer.MAX_VALUE;
						int left=Integer.MAX_VALUE;
						int right = Integer.MAX_VALUE;
						if(k>0)
							left=minSum[i][k-1];
						if(k<size-1)
							right=minSum[i][k+1];
						if(i>0)
							up=minSum[i-1][k];
						if(i<size-1)
							down = minSum[i+1][k];
						minSum[i][k]=Math.min(mat[i][k] + Math.min(Math.min(up, down), Math.min(left, right)), minSum[i][k]);
					}
				}
			}
		}
		System.out.println(minSum[size-1][size-1]);
	}
}
