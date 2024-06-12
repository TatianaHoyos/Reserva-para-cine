
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

//confirmar reserva
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
    document.querySelector('#selectedSeatsList').innerHTML = seatNumbers.map(function(seat) {
        return '<li>' + seat + '</li>';
    }).join('');
}

function confirmarReserva() {
    var selectedSeats = Array.from(document.querySelectorAll('.seat.selected')).map(function(seat) {
        return seat.getAttribute('data-seat');
    });

    var functionSelect = document.getElementById('function');
    var selectedOption = functionSelect.options[functionSelect.selectedIndex];

    var function_id = selectedOption.value;
    var movie_id = selectedOption.getAttribute('data-movie-id');
    var room_id = selectedOption.getAttribute('data-room-id');


    reserva = { 
        selectedSeats : selectedSeats, 
        function_id : function_id,
        movie_id : movie_id,
        room_id : room_id
    }
   
    fetch('/confirmar_reserva', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(reserva)
    })
    .then(response => response.json())
    .then(data => {
        if (data.redirect) {
            window.location.href = data.redirect;
        }
    })
    .catch(error => console.error('Error:', error));
}

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('function').addEventListener('change', function() {
        showSeats(this.value);
    });
    showSeats(document.getElementById('function').value);
});
