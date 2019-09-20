// https://www.acmicpc.net/problem/8974
#include<stdio.h>
int main()
{
	int A, B, sum = 0, arr[1000] = { 0 }, index = 0, value = 1;
	scanf("%d %d", &A, &B);
	while (1)
	{
		int count = 1;
		while (count <= value)
		{
			arr[index] = value;
			count++;
			index++;
			if (index == B)
				break;
		}
		if (index == B)
			break;
		value++;
	}

	//for (int i = 0; i < B; i++)
		//printf("%d ", arr[i]);

	for (int i = A - 1; i < B; i++)
		sum += arr[i];
	printf("%d", sum);
	
	return 0;
}