function show_models(key){
    fetch(`./model/${key}/`)
    .then(response => response.text())
    .then(text => {
        document.getElementById('models').innerHTML = text;
    });
}

document.addEventListener('DOMContentLoaded', function (){
    console.log('ok');
    document.querySelectorAll('button').forEach(button => {
        button.onclick = function() {
            document.getElementById('all_products').style.display = 'none';
            show_models(this.dataset.board);
        }
    });
});