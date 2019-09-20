// https://www.acmicpc.net/problem/3003
#include<stdio.h>
int main()
{
	// 0: Å·, 1: Äý, 2: ·è, 3: ºñ¼ó, 4: ³ªÀÌÆ®, 5: Æù
	int piece[6], result[6];
	for (int i = 0; i < 6; i++)
	{
		scanf("%d", &piece[i]);
		if (i == 0 || i == 1)
		{
			if (piece[i] == 1)
				result[i] = 0;
			else if (piece[i] > 1)
				result[i] = 1 - piece[i];
			else
				result[i] = 1;
		}
		else if (i == 2 || i == 3 || i == 4)
		{
			if (piece[i] == 2)
				result[i] = 0;
			else if (piece[i] > 2)
				result[i] = 2 - piece[i];
			else
				result[i] = 2 - piece[i];
		}
		else
		{
			if (piece[i] == 8)
				result[i] = 0;
			else if (piece[i] > 8)
				result[i] = 8 - piece[i];
			else
				result[i] = 8 - piece[i];
		}
	}
	for (int i = 0; i < 6; i++)
		printf("%d ", result[i]);
	return 0;
}