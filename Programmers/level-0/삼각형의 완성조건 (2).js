function solution(sides) {
	let answer = [];
	sides.sort((a, b) => b - a);
	for (let i = sides[0] - sides[1] + 1; i <= sides[0]; i++) {
			answer.push(i);
	}
	for (let i = sides[0] + 1; i < sides[0] + sides[1]; i++) {
			answer.push(i);
	}
	
	return [...new Set(answer)].length;
}