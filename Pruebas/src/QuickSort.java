
public class QuickSort {
	private int[] numbers;

	public void sort(int[] values){
		numbers=values;
		quicksort(0, numbers.length-1);
	}

	private void quicksort(int min, int max) {
		int i = min;
		int j = max;
		int pivot = numbers[(min+max)/2];
		while(i<=j){
			while(numbers[i]<pivot)
				i++;
			while(numbers[j]>pivot)
				j--;

			if(i<=j){
				exchange(i, j);
				i++;
				j--;
			}
		}

		if(min<j)
			quicksort(min, j);
		if(i<max)
			quicksort(i, max);
	}

	private void exchange(int i, int j) {
		int temp = numbers[i];
		numbers[i]=numbers[j];
		numbers[j]=temp;		
	}

	public int[] getNumbers(){
		return numbers;
	}
}
