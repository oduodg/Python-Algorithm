function solution(s) {
	let ans = [0];
	
	const separate = (s) => {
			if (s.length === 0) return ans[0];
			
			let x = s[0];
			let xCount = 0;
			let notxCount = 0;
			
			for (let i = 0; i < s.length; i++) {
					if (s[i] === x) xCount++;
					else notxCount++;
			
					if (xCount === notxCount) {
							ans[0] += 1;
							return separate(s.slice(i+1));
					}
			}
			
			return ans[0] += 1
	};    
	
	return separate(s);
}