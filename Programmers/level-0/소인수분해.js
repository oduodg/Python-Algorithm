const solution = (n) => {
	const isPrime = x => {
			let prime = Array(x + 1).fill(true).fill(false, 0, 2);
			
			for (let i = 2; i <= Math.ceil(Math.sqrt(x)); i++) {
					if (prime[i]) {
							for (let j = i * i; j <= n; j += i) {
									prime[j] = false;
									if (j === x) {
											return prime[j];
									}
							}
					}    
			}
			
			return prime[x];
	}
	
	let answer = [];
	for (let i = 2; i <= n; i++) {
			if (n % i === 0 && isPrime(i)) {
					answer.push(i);
			}
	}
	
	return answer;
}