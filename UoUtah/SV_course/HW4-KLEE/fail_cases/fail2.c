double division(int x, int y){
	if (x%2 != 0){
		x += 1;
	}
	if (y%2 != 1){
		y += 1;
	}
	return x/y;
}

double main(void){
	int a, b;
	klee_make_symbolic(&a,sizeof(a),"a");
	klee_make_symbolic(&a,sizeof(a),"b");
	return division(a,b);
}
