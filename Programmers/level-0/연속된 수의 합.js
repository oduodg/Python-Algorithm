function solution(num, total) {
	const i = (total - ((num - 1) * num) / 2) / num;
	return Array.from({ length: num}, (_, idx) => idx + i);
}