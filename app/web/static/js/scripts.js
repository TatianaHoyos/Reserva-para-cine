function showSeats(id) {
    var seatContainers = document.querySelectorAll('.seat-container');
    seatContainers.forEach(function(container) {
        container.style.display = 'none';
    });
    document.getElementById('seats_' + id).style.display = 'block';
}

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('function').addEventListener('change', function() {
        showSeats(this.value);
    });
    // Mostrar la primera función por defecto
    showSeats(document.getElementById('function').value);
});