const seats = document.querySelectorAll('.seat:not(.occupied)');
const selectedSeatsInput = document.getElementById('selectedSeats');
const selectedSeatsList = document.getElementById('selectedSeatsList');

seats.forEach(seat => {
    seat.addEventListener('click', () => {
        seat.classList.toggle('selected');
        updateSelectedSeats();
    });
});

function updateSelectedSeats() {
    const selectedSeats = document.querySelectorAll('.seat.selected');
    const seatsIndex = [...selectedSeats].map(seat => seat.getAttribute('data-seat'));
    selectedSeatsInput.value = seatsIndex.join(',');
    updateSelectedSeatsList(seatsIndex);
}

function updateSelectedSeatsList(seatsIndex) {
    selectedSeatsList.innerHTML = '';
    seatsIndex.forEach(seat => {
        const listItem = document.createElement('li');
        listItem.textContent = seat;
        selectedSeatsList.appendChild(listItem);
    });
}

document.getElementById('seatsForm').addEventListener('submit', function(event) {
    event.preventDefault();
    alert('Reserva confirmada para los asientos: ' + selectedSeatsInput.value);
});