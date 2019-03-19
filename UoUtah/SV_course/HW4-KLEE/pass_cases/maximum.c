int find_max(int a, int b){
	if (a>b)
		return a;
	else if (a<b)
		return b;
}
int main(void){
	int a, b;
	klee_make_symbolic(&a,sizeof(a),"a")
	klee_make_symbolic(&a,sizeof(a),"b")
	return find_max(a,b);
}
