function solution(array, n) {
	let [diff, idx] = [100, 0];
	array.sort((a, b) => a - b)
			 .forEach((v, i) => {
					if (Math.abs(v - n) < diff) {
							diff = Math.abs(v - n);
							idx = i;
							}            
					})
	return array[idx];
}