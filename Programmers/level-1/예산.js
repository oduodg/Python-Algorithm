function solution(d, budget) {
	let sum = 0;
	let answer = 0;
	
	d.sort((a, b) => a - b).forEach(v => {
			sum += v;
			answer += 1;
			if (sum > budget) {
					sum -= v;
					answer -= 1;
					return false;
			}
	});
	
	return answer;
}