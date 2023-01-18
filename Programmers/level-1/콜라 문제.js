function solution(a, b, n) {
	let ans = 0;
	while (n >= a) {
			let c = Math.trunc(n / a); // 마트가 주는 콜라 병 수
			ans += b * c;
			n = n - a * c + b * c; // 현재 가지고 있는 콜라 병 수    
	}
	return ans;
}