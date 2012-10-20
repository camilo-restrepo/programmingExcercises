package euler;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class Pbt18 {

	@SuppressWarnings("unchecked")
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new FileReader("./data/in18"));
		String primera = bf.readLine();

		ArrayList<Node<Integer>> arr = new ArrayList<Node<Integer>>();
		arr.add(new Node<Integer>(Integer.parseInt(primera)));

		for (int i = 0; i < arr.size(); i++) {

			String str = bf.readLine();
			if(str!=null){
				String[] list = str.split(" ");
				Node<Integer> actual = arr.get(i);
				if(list.length==2){
					Node<Integer> n = new Node<Integer>(Integer.parseInt(list[0]));
					actual.setLeft(n);
					arr.add(n);
					n=new Node<Integer>(Integer.parseInt(list[1]));
					actual.setRight(n);
					arr.add(n);
				}
				else{

					for (int j = 0; j < list.length; j++) {
						actual = arr.get(i);
						Node<Integer> n = new Node<Integer>(Integer.parseInt(list[j]));
						if(j==0){
							actual.setLeft(n);
						}else if(j==list.length-1){
							actual.setRight(n);							
						}else{
							actual.setRight(n);
							arr.get(i+1).setLeft(n);
							i++;
						}
						arr.add(n);
					}
				}
			}
		}
		System.out.println(maxSum(arr.get(0)));
	}

	public static int maxSum(Node<?> n){
		if(n.left== null && n.right==null)
			return (Integer) n.data;
		else{
			int l = maxSum(n.left);
			int r = maxSum(n.right);
			if(l>r)
				return (Integer)n.data+l;
			else
				return (Integer)n.data+r;
		}
	}
	
	public static void inorder(Node<?> n){
		if (n != null)
		{
			inorder(n.getLeft());
			System.out.print(n.data + " ");
			inorder(n.getRight());
		}
	}


	private static class Node<T>{
		public Node<T> left;
		public Node<T> right;
		private T data;

		public Node(T data)
		{
			this.data = data;
		}
		public Node<T> getLeft()
		{
			return this.left;
		}
		public void setLeft(Node<T> left)
		{
			this.left = left;
		}
		public Node<T> getRight()
		{
			return this.right;
		}
		public void setRight(Node<T> right)
		{
			this.right = right;
		}
	}
}