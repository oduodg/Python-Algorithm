function solution(dots) {
	// 기울기가 같으면 평행한다.
	let answer = [];
	
	for (let i = 0; i < 3; i++) {
			for (let j = i + 1; j < 4; j++) {
					const x = dots[i][0] - dots[j][0];
					const y = dots[i][1] - dots[j][1];
					answer.push(y / x);
			}
	}
	
	return [...new Set(answer)].length !== answer.length ? 1 : 0;
}