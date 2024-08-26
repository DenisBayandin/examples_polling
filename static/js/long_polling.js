function longPoll() {
    fetch('/long-polling/result/')
        .then(response => response.json())
        .then(data => {
            console.log('Long Polling Data:', data);
            updateUI(data.data, 'long-data-list');
        })
        .catch(error => console.error('Error:', error))
        .finally(() => {
            longPoll();
        });
}

function updateUI(data, elementId) {
    let list = document.getElementById(elementId);
    list.innerHTML = '';
    data.forEach(item => {
        let li = document.createElement('li');
        if (item.title && item.description){
        li.textContent = item.title + " - " + item.description;
        list.appendChild(li);
        }
        else {console.log(item)}
    });
}

document.addEventListener('DOMContentLoaded', () => {
    longPoll();
});