function solution(sides) {
	const [a, b, c] = sides.sort((a, b) => b - a);
	if (a < b + c) {
			return 1
	} else {
			return 2
	}
}

/*
function solution(sides) {
	const [a, b, c] = sides.sort((a, b) => b - a);
	return a < b + c ? 1 : 2;
}
*/