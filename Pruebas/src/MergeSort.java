
public class MergeSort {
	private int[] numbers;
	private int[] helper;
	
	public int[] getNumbers(){
		return numbers;
	}
	
	public void sort(int[] values){
		numbers = values;
		helper = new int[values.length];
		mergesort(0, numbers.length-1);
	}

	private void mergesort(int min, int max) {
		if(min<max){
			int mid = (min+max)/2;
			mergesort(min, mid);
			mergesort(mid+1, max);
			merge(min, mid, max);
		}
	}

	private void merge(int min, int mid, int max) {
		
		for(int i = min; i<=max ; i++){
			helper[i]=numbers[i];
		}
		
		int i = min;
		int j = mid+1;
		int k= min;
		
		while(i<=mid && j<=max){
			if(helper[i]<=helper[j]){
				numbers[k] = helper[i];
				i++;
			}else{
				numbers[k] = helper[j];
				j++;
			}
			k++;
		}
		
		while(i<=mid){
			numbers[k]=helper[i];
			k++;
			i++;
		}
	} 
}
