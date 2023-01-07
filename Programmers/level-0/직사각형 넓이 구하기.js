function solution(dots) {
	dots.sort((a, b) => a[1] - b[1]);

	const x = dots[1][0] - dots[0][0];
	const y = dots[2][1] - dots[1][1];

	return Math.abs(x * y);
}