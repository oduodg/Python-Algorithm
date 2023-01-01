const solution = (age) => {
	const alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'];
	let answer = [];
	[...String(age)].map(v => answer.push(alphabet[Number(v)]));
	return answer.join('');
}