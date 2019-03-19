int abs_val(int x){
	if (x < 0)
		return -1*x;
	else
		return x;
}

int main(void){
	int a;
	klee_make_symbolic(&a, sizeof(a), "a");
	return abs_val(a);
}
