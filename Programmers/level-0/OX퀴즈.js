function solution(quiz) {
	let answer = [];
	
	for (let q of quiz) {
			let arr = q.split(' ');
			[X, op, Y, Z] = [Number(arr[0]), arr[1], Number(arr[2]), Number(arr[4])];
			if (op === '+') {
					if (X + Y === Z) {
							answer.push("O");
					} else {
							answer.push("X");   
					}
			} else {
					if (X - Y === Z) {
							answer.push("O");
					} else {
							answer.push("X");   
					}
			}
	}
	
	return answer;
}