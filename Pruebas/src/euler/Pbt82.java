package euler;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class Pbt82 {

	/**
	 * @param args
	 * @throws IOException 
	 */
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new FileReader("./data/in82"));
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
		ArrayList<Integer> arr = new ArrayList<Integer>();
		for (int i = 0; i < mat.length; i++) {
			for (int k = 0; k < mat.length; k++) 
				minSum[i][k]=Integer.MAX_VALUE;
			minSum[i][0]=mat[i][0];
		}

		for(int l = 0; l < size ; l++){

			for (int i = 0; i < mat.length; i++) {
				for (int k = 0; k < mat.length; k++) {
					int up=Integer.MAX_VALUE;
					int down=Integer.MAX_VALUE;
					int right = Integer.MAX_VALUE;
					if(k>0)
						right=minSum[i][k-1];
					if(i>0)
						up=minSum[i-1][k];
					if(i<size-1)
						down = minSum[i+1][k];
					int total = mat[i][k] + (Math.min(Math.min(up, down), right));
					if(total>0)
						minSum[i][k]=Math.min(total, minSum[i][k]);	
				}
			}

			int min = Integer.MAX_VALUE;
			for (int i = 0; i < mat.length; i++) {
				if(minSum[i][size-1]<min)
					min=minSum[i][size-1];
			}
			arr.add(min);
		}
		
		int min = Integer.MAX_VALUE;
		for (int i = 0; i < arr.size(); i++) {
			if(arr.get(i)<min)
				min=arr.get(i);
		}
		System.out.println(min);
	}
}
