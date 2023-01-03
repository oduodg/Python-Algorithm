function solution(n) {
	let factorial = [1, 1]; // 0!, 1!
	
	for (let i = 2; i <= 10; i++) {
			factorial.push(factorial[i-1] * i);
	}
	
	if (n >= factorial[factorial.length - 1]) {
			return 10;
	}
	
	for (let num of factorial) {
			if (num > n) {
					return factorial.indexOf(num) - 1;
			}
	}
}