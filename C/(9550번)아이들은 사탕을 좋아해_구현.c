// https://www.acmicpc.net/problem/9550
#include<stdio.h>
int main()
{
	// t: �׽�Ʈ ����, n: ������ ���� ����, k: ���̵��� �����ϴ� ������ ����
	int t, n, k, candy;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		// count: �ʴ��� �� �ִ� ���̵��� ��
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