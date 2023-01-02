function solution(letter) {
	let morse = { 
	'.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
	'--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
	'--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
	'...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
	'-.--':'y','--..':'z'
	};
	
	let answer = '';
	let alphabet = '';
	for (let s of letter) {
			if (s === ' ') {
					answer += morse[alphabet];
					alphabet = '';
					continue;
			}
			alphabet += s;
	}
	// 맨 끝
	answer += morse[alphabet];
	return answer;
}