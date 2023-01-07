function solution(M, N) {
	if (M === 1 && N === 1) return 0;
	return (M - 1) + (N - 1 ) * M;
}