function solution(spell, dic) {
	const word = spell.sort().join('');
	for (let v of dic) {
			if (word === [...v].sort().join('')) return 1;
	}
	return 2;
}