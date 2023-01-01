const solution = (n) => {
	let answer = 1;
	let v = 1;
	while (v <= parseInt(n / 2)) { 
			if (n % v === 0) answer++;
			v++;
	}
	return answer;
}