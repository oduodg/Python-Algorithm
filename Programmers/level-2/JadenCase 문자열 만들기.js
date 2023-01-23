function solution(s) {
	let ans = '';
	let arr = s.split(' ');

	for (let i = 0; i < arr.length; i++) {
			for (let j = 0; j < arr[i].length; j++) {
					if (j === 0) {
							if (isNaN(arr[i][j])) ans += arr[i][j].toUpperCase();
							else ans += arr[i][j];
					} else {
							ans += arr[i][j].toLowerCase();
					}
			}
			ans += ' ';
	}

	return ans.slice(0, -1);
}