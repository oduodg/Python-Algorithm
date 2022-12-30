const solution = (s, n) => {
	const arr = [...s];
	const answer = [];
	
	for (let c of arr) {
			if (c === ' ') {
					answer.push(c);
					continue;
			}
			
			let code = c.charCodeAt() + n;
			if (c === c.toUpperCase()) { // 대문자인 경우
					if (code > 90) code = 65 + (code - 90 - 1);
			} else { // 소문자인 경우
					if (code > 122) code = 97 + (code - 122 - 1);
			}
			answer.push(String.fromCharCode(code));
	}
	
	return answer.join("");
}