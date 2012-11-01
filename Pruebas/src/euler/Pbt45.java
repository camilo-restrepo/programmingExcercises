package euler;

import java.text.DecimalFormat;


public class Pbt45 {

	public static void main(String[] args) {

		//		BigInteger num = new BigInteger("40000");
		double num = 40000;
		int cont = 0;
		while(cont!=2){
			if(isHexagonal(num) && isPentagonal(num) && isTriangular(num))
			{
				DecimalFormat df = new DecimalFormat("#0.00");
				System.out.println(df.format(num));
				cont++;
			}
			num++;
		}
	}

	private static boolean isTriangular(double num){
		double n = (Math.sqrt((8*num)+1)-1)/2;
		if(n-Math.floor(n)==0)
			return true;
		return false;
	}
	private static boolean isPentagonal(double num){
		double n = (Math.sqrt((24*num)+1)+1)/6;
		if(n-Math.floor(n)==0)
			return true;
		return false;
	}
	private static boolean isHexagonal(double num){
		double n = (Math.sqrt((8*num)+1)+1)/4;
		if(n-Math.floor(n)==0)
			return true;
		return false;
	}
}