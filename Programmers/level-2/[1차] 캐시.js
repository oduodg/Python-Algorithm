function solution(cacheSize, cities) {
	let runTime = 0;
	let cache = [];
	
	if (cacheSize === 0) {
			return cities.map(v => v = v.toLowerCase())
									 .length * 5;
	}
	
	cities.forEach(v => {
			v = v.toLowerCase();
			if (cache.includes(v)) {
					cache = cache.filter(city => city !== v);
					cache.push(v);
					runTime += 1;
			} else {
					if (cache.length === cacheSize) cache.shift();
					cache.push(v);
					runTime += 5;
			}
	});
	
	return runTime
}