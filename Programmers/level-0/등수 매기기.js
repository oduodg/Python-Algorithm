function solution(score) {
	let answer = Array(score.length).fill(1);
	let mean = [];
	score.map(([eng, math]) => mean.push((eng + math) / 2));
	
	for (let i = 0; i < mean.length; i++) {
			for (let j = 0; j < mean.length; j++) {
					if (mean[i] < mean[j]) answer[i]++;
			}
	}
	
	return answer;
}