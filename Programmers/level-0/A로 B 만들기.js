function solution(before, after) {
	[...before].map(v => after = after.replace(v, ""));
	return after ? 0 : 1;
}