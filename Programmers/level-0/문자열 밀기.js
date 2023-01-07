function solution(A, B) {
	if (A === B) return 0;
	let answer = 0;
	
	for (let i = 0; i < A.length - 1; i++) {
			A = A[A.length - 1] + A.substr(0, A.length - 1);
			answer++;
			if (A === B) return answer;
	}
	
	return -1;
}