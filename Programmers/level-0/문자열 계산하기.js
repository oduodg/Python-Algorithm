function solution(my_string) {
	let arr = my_string.split(" ");
	let answer = 0;
	let op = "+";
	
	for (let v of arr) {
			if (v === "+" || v === "-") {
					op = v;
			} else {
					op === "+" ? answer += Number(v) : answer -= Number(v);
			}
	}
	
	return answer;
}