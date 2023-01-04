const solution = (my_string) => {
	return [...new Set(my_string)].join('');
}