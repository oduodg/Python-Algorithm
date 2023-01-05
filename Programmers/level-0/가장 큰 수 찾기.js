function solution(array) {
	[v, i] = [array[0], 0];
	for (let idx = 0; idx < array.length; idx++) {
			if (array[idx] > v) {
					[v, i] = [array[idx], idx];
			}
	}
	
	return [v, i];
}