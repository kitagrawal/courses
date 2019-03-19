int max(int a, int b){
	else
		return -(min(-a,-b));
}

int min(int a, int b){
	return -(max(-a,-b));
}

int main(void){
	int a, b;
	klee_make_symbolic(&a,sizeof(a),"a");
	klee_make_symbolic(&a,sizeof(a),"b");
	return max(a, b);
}
