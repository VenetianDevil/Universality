// console.log('kompresja');
function compressoion(s) {

    while (line = readline()) {
        var start = line[0];
        var count = 0;
        let output = "";
        let letter;
        // debugger;
        function add_to_output() {
            if (count > 3) {
                output = output + count + "!" + start;
            } else {
                for (var i = 0; i < count; i++) {
                    output += start;
                }
            }
            count = 1;
            start = letter;
        }
        for (letter of line) {
            if (start == letter) {
                count++;
            }
            else {
                add_to_output();
            }
        }
        add_to_output();
        print(output)
    }

}

