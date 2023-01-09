function solution(n) {
	const arr = Array.from({length: 200}, (v, i) => i + 1);
	for (let i = 1; i <= 200; i++) {
			if (i % 3 === 0 || String(i).split('').includes('3')) {
					arr[i-1] = false; // 3x 숫자
			}
	}
	
	return arr.filter(v => v !== false)[n - 1];
}