package codechef;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Hashtable;

//Holes in the Text 
public class HolesInText {

	public static void main(String[] args) throws NumberFormatException, IOException {
		Hashtable<String, Integer> ht = new Hashtable<String, Integer>(26);
		ht.put("A", 1);
		ht.put("B", 2);
		ht.put("C", 0);
		ht.put("D", 1);
		ht.put("E", 0);
		ht.put("F", 0);
		ht.put("G", 0);
		ht.put("H", 0);
		ht.put("I", 0);
		ht.put("J", 0);
		ht.put("K", 0);
		ht.put("L", 0);
		ht.put("M", 0);
		ht.put("N", 0);
		ht.put("O", 1);
		ht.put("P", 1);
		ht.put("Q", 1);
		ht.put("R", 1);
		ht.put("S", 0);
		ht.put("T", 0);
		ht.put("U", 0);
		ht.put("V", 0);
		ht.put("W", 0);
		ht.put("X", 0);
		ht.put("Y", 0);
		ht.put("Z", 0);
		BufferedReader r = new BufferedReader(new InputStreamReader (System.in));
		int n = Integer.parseInt(r.readLine());
		while(n>0){
			String str = r.readLine();
			int cuenta = 0;
			for(int  i = 0 ; i < str.length() ; i++){
				cuenta+=ht.get(str.charAt(i)+"");
			}
			System.out.println(cuenta);
			n--;
		}
	}
}