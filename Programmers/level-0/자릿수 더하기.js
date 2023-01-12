const solution = (n) => {
	const str = String(n);
	const mapfn = (arg) => Number(arg);
	const arr = Array.from(str, mapfn);
	return arr.reduce((acc, curr) => acc + curr)
}