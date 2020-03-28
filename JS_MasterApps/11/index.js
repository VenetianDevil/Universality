function addToList(){
    const input = document.getElementById('input_field').value;
    let list = document.getElementById('list');
    let li = document.createElement('li');
    li.textContent = input;
    let button = document.createElement('button');
    button.type = 'button';
    button.textContent = 'Remove'
    button.addEventListener('click', function(li) {
        li.remove();
    }.bind(null, li), {once: true});
    li.appendChild(button)
    list.prepend(li);
}