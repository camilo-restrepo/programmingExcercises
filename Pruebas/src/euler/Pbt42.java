package euler;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Hashtable;

public class Pbt42 {

	public static void main(String[] args) throws IOException {
		String[] letras = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"};
		Hashtable<String, Integer> fastLetras = new Hashtable<String, Integer>();
		for (int i = 0; i < letras.length; i++) {
			fastLetras.put(letras[i].toUpperCase(), (i+1));
		}
		
		boolean[] triangulares = new boolean[10000];
		for (int i = 0; i < triangulares.length; i++) {
			int t = (int) (i*(i+1))/2;
			if(t<10000)
				triangulares[t]=true;
		}
		
		BufferedReader bf = new BufferedReader(new FileReader("./data/in42"));
		String str = bf.readLine();
		String words[] = str.split(",");
		int contador=0;
		for (int i = 0; i < words.length; i++) {
			words[i]=words[i].replace("\"", "");
			int	 suma = 0;
			for(int j = 0 ; j < words[i].length() ; j++){
				String letra = words[i].charAt(j)+"";
				suma+=fastLetras.get(letra);
			}
			if(triangulares[suma])
				contador++;
		}
		System.out.println(contador);
	}
}