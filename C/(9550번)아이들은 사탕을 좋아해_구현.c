// https://www.acmicpc.net/problem/9550
#include<stdio.h>
int main()
{
	// t: 테스트 갯수, n: 종류별 사탕 갯수, k: 아이들이 만족하는 사탕의 갯수
	int t, n, k, candy;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		// count: 초대할 수 있는 아이들의 수
		int count = 0;
		scanf("%d %d", &n, &k);
		for (int j = 0; j < n; j++)
		{
			scanf("%d", &candy);
			while (candy >= k)
			{
				candy -= k;
				count++;
			}
		}
		printf("%d\n", count);
	}
	return 0;
}