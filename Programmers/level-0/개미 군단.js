const solution = (hp) => {
	let a = Math.trunc(hp / 5);
	hp -= a * 5;
	let b = Math.trunc(hp / 3);
	hp -= b * 3;
	return a + b + hp;
}