function solution(s) {
    s = s.split(' ');
    s.sort((a, b) => Number(a) - Number(b));
    return s[0].concat(` ${s[s.length - 1]}`)
}