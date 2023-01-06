function solution(num, k) {
	let answer = num.toString().split('').indexOf(String(k));
	
	return answer >= 0 ? ++answer : answer;
}