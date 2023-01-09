function solution(lines) {
	// -100 <= a < b <= 100
	// a, b를 인덱스로 사용하기 위해(a, b를 0 이상으로 만들기 위해) +100씩 해준다.
	
	let arr = Array(200).fill(0);
	// arr[i]는 i ~ i+1 선분의 길이
	// arr[i] = 1 이면 선분이 1개, arr[i] = 2 이면 선분이 2개 겹침, 3 이면 3개 겹침.
	
	for (let line of lines) {
			for (let i = line[0] + 100; i < line[1] + 100; i++) {
					arr[i]++;
			}
	}
	
	return arr.filter(v => v >= 2).length;
}