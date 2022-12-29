function solution(denum1, num1, denum2, num2) {
	// 최대공약수 구하기
	const getGCD = (a, b) => a % b === 0 ? b : getGCD(b, a % b);
	// 최소공배수 구하기
	const getLCM  = (a, b) => a * b / getGCD(a, b);
	
	const lcm = getLCM(num1, num2);
	const quotient1 = lcm / num1;
	const quotient2 = lcm / num2;
	console.log(`gcd는 ${lcm}, quotient1은 ${quotient1}, quotient2은 ${quotient2}`);
	
	let resultDenum = denum1 * quotient1 + denum2 * quotient2;
	let resultNum =  lcm;
	console.log(`resultDenum는 ${resultDenum}, resultNum은 ${resultNum}`);
	
	const resultGCD = getGCD(resultDenum, resultNum);
	resultDenum = parseInt(resultDenum / resultGCD);
	resultNum = parseInt(resultNum / resultGCD);
	
	return [resultDenum, resultNum];
}