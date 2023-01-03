const solution = (n) => {
	const isNotPrime = (n) => {
			if (n <= 2) return 0;
			
			let prime = Array(n + 1).fill(true).fill(false, 0, 2)
			
			for (let i = 2; i <= Math.ceil(Math.sqrt(n)); i++) {
					if (prime[i]) {
							for (let j = i * i; j <= n; j += i) {
									prime[j] = false;
							}
					}
			}
			
			return prime.filter(v => v === false).length;
	}  

	return n <= 2 ? 0 : isNotPrime(n) - 2; // 1, 2는 제외함.
}