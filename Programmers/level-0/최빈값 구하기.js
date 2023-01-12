const solution = (array) => {
	if (array.length === 1) return array[0];
	
	const obj = {};
	const answer = [];
	
	array.forEach(e => {
			obj[e] = ++obj[e] || 1;
	});
	
	for (let key in obj) {
			answer.push([key, obj[key]]);
	}
	
	answer.sort((a, b) => b[1] - a[1]);
	
	if (answer.length === 1) return Number(answer[0][0]);
	// 최빈값이 여러 개인 경우
	if (answer[0][1] === answer[1][1]) return -1;
	
	return Number(answer[0][0]);
}