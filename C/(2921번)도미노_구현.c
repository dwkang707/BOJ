// https://www.acmicpc.net/problem/2921
#include<stdio.h>
int main()
{
	int n, sum = 0;
	scanf("%d", &n);
	// n=1�϶� (0, 0), (0, 1), (1, 1), n=2�϶� (0,0), (0,1), (1,1), (0,2), (1,2), (2,2)
	for (int i = 0; i <= n; i++)
	{
		for (int j = 0; j <= i; j++)
			sum = i + j + sum;
	}
	printf("%d", sum);
	return 0;
}