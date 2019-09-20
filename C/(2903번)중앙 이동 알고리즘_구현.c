// https://www.acmicpc.net/problem/2921
#include<stdio.h>
#include<math.h>
int main()
{
	int n, sum;
	scanf("%d", &n);
	sum = pow(2, n) + 1;
	sum = pow(sum, 2);
	printf("%d", sum);
	return 0;
}