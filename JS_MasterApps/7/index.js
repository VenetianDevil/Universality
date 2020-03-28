function pizza() {
    for (let i = 1; i <= 10; i++) {
        let output = []
        for (j = 1; j <= i; j++) {
            output.push("\uD83C\uDF55")
        }
        console.log(output.join(' '))
    }
}

function stars() {
    let black = ["\u2605"];
    let white = new Array(7).fill("\u2606");

    for (let i = 1; i <= 8; i++) {
        let output = white.concat(black).concat(white);
        console.log(output.join(' '))
        
        black.push("\u2605", "\u2605");
        white.pop();
    }
}