package euler;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class Pbt82 {

	/**
	 * @param args
	 * @throws IOException 
	 */
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new FileReader("./data/in82"));
		String str = bf.readLine();

		int size = 5;
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
		for (int i = 0; i < minSum.length; i++) {
			minSum[i][0]=mat[i][0];
		}

		for (int i = 0; i < mat.length; i++) {
			for (int k = 1; k < mat.length; k++) {
				
			}
		}

		for (int i = 0; i < mat.length; i++) {
			for (int k = 0; k < mat.length; k++) {
				System.out.print(minSum[i][k]+" ");
			}
			System.out.println();
		}
	}

}
