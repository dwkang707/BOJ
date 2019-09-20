// https://www.acmicpc.net/problem/2921
#include<stdio.h>
#include<math.h>
int main()
{
	// n: 처음 타고 있던 사람수, t: 테스트 갯수, k: 각 테스트별 정류장 갯수
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