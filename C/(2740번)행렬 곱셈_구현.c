#include <stdio.h>
int main()
{
	int N, M, K;
	int mat[100][100] = { 0 }, matA[100][100], matB[100][100];
	
	// matA�� ũ�⸦ �Է� ����(N: row, M: column)
	scanf("%d %d", &N, &M);
	
	// matA�� ���ҵ��� �Է¹���
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
			scanf("%d", &matA[i][j]);
	}

	// matB�� ũ�⸦ �Է� ����(M: row, K: column)
	scanf("%d %d", &M, &K);

	// matA�� ���ҵ��� �Է¹���
	for (int i = 0; i < M; i++)
	{
		for (int j = 0; j < K; j++)
			scanf("%d", &matB[i][j]);
	}

	// matA ��İ� matB�� ����� ���� ��� �� ���
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < K; j++)
		{
			for (int a = 0; a < M; a++)
				mat[i][j] = mat[i][j] + matA[i][a] * matB[a][j];
			printf("%d ", mat[i][j]);
		}
		printf("\n");
	}
	return 0;
}