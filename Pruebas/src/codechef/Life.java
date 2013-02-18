package codechef;

import java.io.BufferedReader;
import java.io.InputStreamReader;

//Life, the Universe, and Everything
public class Life
{
	public static void main (String[] args) throws Exception
	{
		BufferedReader r = new BufferedReader(new InputStreamReader (System.in));
		while(true){
			String s = r.readLine();
			if(s.equals("42"))
				return;
			else
				System.out.println(s);
		}
	}
}