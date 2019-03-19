int large_unroll(int x){
	int product = 1;
	if (x >= 5){
		while (x > 0){
			product = product * x;
			x -= 1;
		}
	}
	return product;
}

int main(void){
	int a;
	klee_make_symbolic(&a,sizeof(a),"a");
	return large_unroll(a);
}
		
