const solution = (number) => {
	let answer = 0;
	
	for (let i = 0; i < number.length - 1; i++) {
			for (let j = i + 1; j < number.length; j++) {
					const l = number
											.slice(j+1)
											.filter(v => v === -(number[i] + number[j]))
											.length;
					if (l > 0) {
							answer += l;
					}
			}
	}
	
	return answer;
}