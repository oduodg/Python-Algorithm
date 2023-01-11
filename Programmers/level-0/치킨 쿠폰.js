function solution(chicken) {
	let coupon = chicken;
	let serviceChicken = 0;
	let answer = 0;
	
	while (coupon >= 10) {
			serviceChicken = Math.trunc(coupon / 10);
			coupon = coupon % 10 + serviceChicken;
			answer += serviceChicken;
	}
	
	return answer;
}