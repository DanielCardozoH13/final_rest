'use strict'

window.addEventListener('load', e => {
    const form = document.querySelector('#form');
    const content = document.querySelector('#content');

    form.addEventListener('submit', e => {
        e.preventDefault();

        var data = new FormData(form);
        console.log(data);
        fetch('core/controller/instances-controller.php', {
            method: 'post',
            body: data
        })
            .then(response => response.text())
            .then(data => {
               content.innerHTML = data;
            });   
    });
});