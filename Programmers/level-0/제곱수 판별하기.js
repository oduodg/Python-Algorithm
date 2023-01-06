function solution(n) {
	const sqrt = Math.sqrt(n);
	return sqrt === Math.trunc(sqrt) ? 1 : 2;
}