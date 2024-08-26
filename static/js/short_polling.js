function shortPolling() {
    fetch('/short-polling/result/')
        .then(response => response.json())
        .then(data => {
            console.log(data);
            updateClientData(data.data, 'short-data-list');
        })
        .catch(error => console.error('Error:', error));
}

function updateClientData(data, elementId) {
    let list = document.getElementById(elementId);
    list.innerHTML = '';
    data.forEach(item => {
        let li = document.createElement('li');
        li.textContent = item.title + " - " + item.description;
        list.appendChild(li);
    });
}


document.addEventListener('DOMContentLoaded', () => {
    setInterval(shortPolling, 5000);
});