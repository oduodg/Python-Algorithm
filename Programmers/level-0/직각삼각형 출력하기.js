const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = line.split(' ');
}).on('close', function () {
    //console.log(Number(input[0]));
    for (let i = 1; i <= Number(input[0]); i++) {
        let star = '';
        for (let j = 0; j < i; j++){
            star += '*';
        }
        console.log(star);
    }
});