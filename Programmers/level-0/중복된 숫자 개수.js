const solution = (array, n) => {
	let answer = 0;
	
	for (let num of array) {
			if (num === n) answer++; 
	}
	
	return answer;
}