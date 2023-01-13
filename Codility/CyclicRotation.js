// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A, K) {
	// Implement your solution here
	if (A.length === 0) return A;
	for (let i = 0; i < K; i++) {
			A.unshift(A.pop())
	}

	return A;
}