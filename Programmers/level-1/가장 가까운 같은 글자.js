function solution(s) {
	let answer = [];
	for (let i = 0; i < s.length; i++) {
			const curr = s[i];
			const idx = s.lastIndexOf(curr, i - 1);
			if (idx === i || idx === -1) answer.push(-1);
			else answer.push(i - idx);
	}
	
	return answer;
}