int linear_interpolatin(int x){
	static const int arr[] = {2,3};
	if (x > 1){
		x = 1
	}
	else if (x < 0){
		x = 0
	}
	return (arr[0]+(arr[1]-arr[0])*x)
}

int main(void){
	int a;
	klee_make_symbolic(&a, sizeof(a), "a");
	return linear_interpolation(a);
}
