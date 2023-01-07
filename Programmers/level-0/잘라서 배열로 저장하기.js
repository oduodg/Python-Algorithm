function solution(my_str, n) {
	let arr = [];
	for (let i = n; i <= my_str.length; i += n) {
			arr.push(my_str.substring(i - n, i));
	}
	
	if (my_str.length / n !== arr.length) {
			arr.push(my_str.substring(arr.length * n));
	}
	
	return arr;
}