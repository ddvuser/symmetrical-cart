document.addEventListener("DOMContentLoaded", function() {
    console.log("wtf")
    var quantityIncrementButtons = document.querySelectorAll('#quantity-increment');
    var quantityDecrementButtons = document.querySelectorAll('#quantity-decrement');

    quantityIncrementButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            var input = button.parentElement.querySelector('#quantity-input');
            input.value = parseInt(input.value) + 1;
        });
    });

    quantityDecrementButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            var input = button.parentElement.querySelector('#quantity-input');
            if (input.value > 1) {
                input.value = parseInt(input.value) - 1;
            }
        });
    });
});
