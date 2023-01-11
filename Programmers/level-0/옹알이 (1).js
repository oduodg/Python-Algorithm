function solution(babbling) {
	let answer = 0;
	let curr = '';
	
	for (let s of babbling) {
			let dict = ['aya', 'ye', 'woo', 'ma'];
			for (let i = 0; i < s.length; i++) {
					curr += s[i];
					
					if (dict.includes(curr)) {
							dict = dict.filter(v => v !== curr);
							curr = '';
					}   
			}
			if (curr === '') answer += 1;
			curr = ''; // 초기화
	}
	
	return answer;
}