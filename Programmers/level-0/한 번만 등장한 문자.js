function solution(s) {
	let answer = "";
	let dic = {};
	for (let v of s) {
			dic[v]? dic[v] += 1 : dic[v] = 1;
	}
	let arr = [];
	for (let key in dic) {
			arr.push([key, dic[key]])
	}
	arr.sort((a, b) => a[1] - b[1]);
	for (let v of arr) {
			if (v[1] === 1) {
					answer += v[0];
			}
	}
	
	return answer.split('').sort().join('');
}