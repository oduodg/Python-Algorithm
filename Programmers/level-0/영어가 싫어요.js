function solution(numbers) {
	const dic = {
			"zero": 0, 
			"one": 1, 
			"two": 2, 
			"three": 3,
			"four": 4,
			"five": 5, 
			"six": 6,
			"seven": 7, 
			"eight": 8, 
			"nine": 9
	}
	
	let answer = "";
	let key = "";
	
	for (let s of numbers) {
			if (key in dic) {
					answer += dic[key];
					key = "";
			}
			key += s;
	}
	answer += dic[key];
	
	return Number(answer);
}