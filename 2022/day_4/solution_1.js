const fs = require('fs');


function readData() {
    try {
        return fs.readFileSync('input.txt', 'utf8');
    } catch (err) {
        throw err;
    }
}


function getArrayFromElfTasks(tasks) {
    let [start, stop] = tasks.split('-').map((value) => Number(value));
    let arr = Array.from({length: stop - start + 1}, (_, i) => start + i);
    return arr;
}


function parseElfArraysFromLine(line) {
    return line.split(',').map((value) => getArrayFromElfTasks(value));
}


function intersect(a, b) {
    var setB = new Set(b);
    return [...new Set(a)].filter(x => setB.has(x));
}


function checkIfArrayWithinOther(a, b) {
    let intersection = intersect(a, b);
    return a.length == intersection.length || b.length ==  intersection.length
}


function main() {
    const splitData = readData().split('\n');

    let count = 0;

    splitData.forEach((line) => {
        let [elfOneArray, elfTwoArray] = parseElfArraysFromLine(line);
        count += Number(checkIfArrayWithinOther(elfOneArray, elfTwoArray));
    });

    console.log(`Final count: ${count}`);
}


main();