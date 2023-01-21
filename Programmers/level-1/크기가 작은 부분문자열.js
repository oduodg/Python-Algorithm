function solution(t, p) {
	let ans = 0;
	for (let i = 0; i <= t.length - p.length; i++) {
			if (Number([...t].slice(i, i + p.length).join('')) <= Number(p)) {
					ans++;
			}
	}
	
	return ans;
}