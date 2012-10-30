package euler;

public class Pbt31 {

	private static int S[] = {1,2,5,10,20,50,100,200};
	
	public static void main(String[] args) {
		int resp = count(200, 7);
		System.out.println(resp);
	}

	private static int count(int n, int m){
		if(n==0)
			return 1;
		if(n<0)
			return 0;
		if(m<0 && n>=1)
			return 0;
		return count(n, m-1)+count(n-S[m], m);
	}
}
