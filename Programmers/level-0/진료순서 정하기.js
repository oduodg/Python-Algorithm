const solution = (emergency) => {
	let arr = [...emergency].sort((a, b) => b - a);
	let answer = [];
	emergency.map(v => answer.push(arr.indexOf(v) + 1));
	return answer;
}