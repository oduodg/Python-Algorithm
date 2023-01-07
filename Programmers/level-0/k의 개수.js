function solution(i, j, k) {
	return Array.from({ length: j - i + 1}, (_, idx) => idx + i)
							.filter(v => v.toString().includes(k.toString()))
							.join("")
							.replace(new RegExp(`[^${k}]`, 'g'), '')
							.length;
}