function solution(a, b) {
	// 기약분수 -> 최대공약수
	const getGCD = (a, b) => a % b === 0 ? b : getGCD(b, a % b);
	const isPrime = (n) => {
			let prime = Array(n + 1).fill(true).fill(false, 0, 2);
			
			for (let i = 2; i <= Math.ceil(Math.sqrt(n)); i++) {
					if (prime[i]) {
							for (let j = i * i; j <= n; j += i) {
									prime[j] = false;
									if (j === n) {
											return prime[j];
									}
							}
					}
			}
			return prime[n];
	}
	
	const gcd = getGCD(a, b);
	a = a / gcd;
	b = b / gcd;
	
	const getDivisor = (n) => Array.from({ length: n }, (v, i) => i +1 ).filter((el) => n % el === 0 && isPrime(el));
	
	const divisor = getDivisor(b);
	
	if (divisor.length === 0) { // a/b의 값이 정수인 경우(정수도 유한소수이다.)
			return 1;
	}
	else if (divisor.length === 1) {
			if (divisor.includes(2) || divisor.includes(5)) {
					return 1;
			}
	}
	else if (divisor.length === 2) {
			if (divisor.includes(2) && divisor.includes(5)) {
					return 1;
			}
	}
	
	return 2;
}