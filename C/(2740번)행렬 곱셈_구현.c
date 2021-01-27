#include <stdio.h>
int main()
{
	int N, M, K;
	int mat[100][100] = { 0 }, matA[100][100], matB[100][100];
	
	// matA의 크기를 입력 받음(N: row, M: column)
	scanf("%d %d", &N, &M);
	
	// matA의 원소들을 입력받음
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
			scanf("%d", &matA[i][j]);
	}

	// matB의 크기를 입력 받음(M: row, K: column)
	scanf("%d %d", &M, &K);

	// matA의 원소들을 입력받음
	for (int i = 0; i < M; i++)
	{
		for (int j = 0; j < K; j++)
			scanf("%d", &matB[i][j]);
	}

	// matA 행렬과 matB의 행렬의 곱을 계산 후 출력
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