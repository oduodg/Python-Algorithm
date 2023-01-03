const solution = (my_string) => {
	const vowels = ['a', 'e', 'i', 'o', 'u'];
	vowels.map(v => my_string = my_string.replaceAll(v, ''));
	return my_string;
}