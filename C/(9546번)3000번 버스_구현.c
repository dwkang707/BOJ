// https://www.acmicpc.net/problem/2921
#include<stdio.h>
#include<math.h>
int main()
{
	// n: ó�� Ÿ�� �ִ� �����, t: �׽�Ʈ ����, k: �� �׽�Ʈ�� ������ ����
	int t, k;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		int n = 0;
		scanf("%d", &k);
		for (int j = 1; j <= k; j++)
		{
			n = n + ((pow(2, j) - 1) / 2) + 0.5;
		}
		printf("%d\n", n);
	}
	return 0;
}