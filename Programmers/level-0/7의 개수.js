function solution(array) {
	return array.join('').split('').filter(v => v === '7').length;
}