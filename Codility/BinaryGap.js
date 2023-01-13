// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(N) {
	// Implement your solution here

	let arr = [];
	let cnt = 0;
	N = N.toString(2);

	for (let i = 0; i < N.length; i++) {
			if (N[i] === '0') cnt += 1;
			else {
					arr.push(cnt);
					cnt = 0;
			}
	}

	return Math.max(...arr);
}