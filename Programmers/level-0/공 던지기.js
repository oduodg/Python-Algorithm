function solution(numbers, k) {
	let arr = [];
	arr = numbers.filter(v => v % 2 === 1);
	
	const length = numbers.length;
	if (length % 2 === 0) {
			return arr[(k-1) % (length / 2)];
	} else {
			arr = arr.concat(numbers.filter(v => v % 2 === 0));
			return arr[(k-1) % length];
	}
}