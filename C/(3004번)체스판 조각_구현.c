// https://www.acmicpc.net/problem/3004
#include<stdio.h>
int main()
{
	int n, count = 1;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++)
	{
		if (i % 2 == 0)
		{
			for (int j = 1; j <= i / 2 + 1; j++)
					count++;
		}
		else
		{
			for (int j = 1; j <= (i + 1) / 2; j++)
					count++;
		}
	}
	printf("%d", count);
	return 0;
}