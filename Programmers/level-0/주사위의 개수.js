const solution = (box, n) => {
	return box.map(v => Math.floor(v / n))
						.reduce((acc, curr) => acc * curr);
}