function solution(n, arr1, arr2) {
	let answer = [];
	
	const toBinary = (arr) => {
			return arr.map(v => {
									v = v.toString(2);
									if (v.length < n) {
											v = "0".repeat(n - v.length).concat(v);
									}
									return v;
							});
	}

	arr1 = toBinary(arr1);
	arr2 = toBinary(arr2);
	
	const secretCode = {'0': ' ', '1': '#'};
	
	for (let i = 0; i < n; i++) {
			let line = "";
			for (let j = 0; j < n; j++) {
					if (arr1[i][j] === arr2[i][j]) line += secretCode[arr1[i][j]];
					else line += '#';
			}
			answer.push(line);
	}
	
	return answer;
}