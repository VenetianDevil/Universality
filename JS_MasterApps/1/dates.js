function findDay() {
    debugger
    let number = readline();
    number = parseInt(number);
    var i = 0;
    const names = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
    if (number > 0 && number <= 100) {
        while (i < number) {
            let line = readline().split(' ');
            let date = new Date(line[2], line[1]-1, line[0]);
            print(names[date.getDay()] + '\n');
            i++;
        }
    }
}

var count = 0;

function readline(){
    const dane = [2, '8 3 2020', '12 1 2012', '13 1 2012'];
    return dane[count++]
}

