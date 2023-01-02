const solution = (balls, share) => {
	const factorial = n => {
			if (n === 0) return BigInt(1);
			
			let answer = BigInt(1);
			
			while (n > 1) {
					answer *= BigInt(n);
					n--;
			}
			
			return BigInt(answer);
	}
	
	return factorial(balls) / (factorial(balls - share) * factorial(share));
}