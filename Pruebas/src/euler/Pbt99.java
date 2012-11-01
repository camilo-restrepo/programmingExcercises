package euler;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.math.BigInteger;

public class Pbt99 {

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new FileReader("./data/in99"));
		String str = bf.readLine();
		double max=0;
		int cont = 1;
		int linea = 1;
		while(str!=null){
			String[] s = str.split(",");
			int base = Integer.parseInt(s[0]);
			int exp = Integer.parseInt(s[1]);
			double val = exp*Math.log10(base);
			if(val-max>0)
			{
				linea = cont;
				max=val;
			}
			cont++;
			str = bf.readLine();
		}
		System.out.println(max+" "+linea);
	}
}
