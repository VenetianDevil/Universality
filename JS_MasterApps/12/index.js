function setKeysHandler(ghost) {
    var key, pos = 0
    var top = left = 50;

    document.onkeydown = function (e) {
        pos = 1;
        key = window.event ? e.keyCode : e.which;
    }

    document.onkeyup = function (e) { pos = 0; }

    setInterval(function () {
        if (pos == 0) return;
        else {
            if (key == 38) { top -= 3; ghost.style.top = top + '%'; }
            if (key == 40) { top += 3; ghost.style.top = top + '%'; }
            if (key == 37) { left -=3; ghost.style.left = left + '%'}
            if (key == 39) { left +=3; ghost.style.left = left + '%'}
        }
    }, 50);
}