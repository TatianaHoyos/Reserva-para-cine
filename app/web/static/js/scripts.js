function showSeats(id) {
    var seatContainers = document.querySelectorAll('.seat-container');
    seatContainers.forEach(function(container) {
        container.style.display = 'none';
    });
    document.getElementById('seats_' + id).style.display = 'block';
}

function toggleSeat(seat) {
    if (!seat.classList.contains('occupied')) {
        seat.classList.toggle('selected');
        updateSelectedSeats();
    }
}

function updateSelectedSeats() {
    var selectedSeats = document.querySelectorAll('.seat.selected');
    var seatNumbers = Array.from(selectedSeats).map(function(seat) {
        return seat.getAttribute('data-seat');
    });
    document.querySelector('.selected-seats').innerText = 'Asientos seleccionados: ' + seatNumbers.join(', ');
}

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('function').addEventListener('change', function() {
        showSeats(this.value);
    });
    // Mostrar la primera función por defecto
    showSeats(document.getElementById('function').value);
});

function confirmarReserva() {
 
    fetch('/confirmar_reserva', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 'selectedSeats': 'selectedSeats' })
    })
    .then(response => response.json())
    .then(data => {
        if (data.redirect) {
            window.location.href = data.redirect;
        }
    })
    .catch(error => console.error('Error:', error));
}