function solution(my_string) {
	const numbers = Array.from({length: 10}, (v, i) => i);
	let arr = [...my_string];
	let answer = [];
	arr.map(v => {
			if (v in numbers) {
					answer.push(Number(v));
			}
	})
	return answer.sort((a, b) => a - b);
}