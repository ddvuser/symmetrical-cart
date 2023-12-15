document.addEventListener("DOMContentLoaded", function() {
	// Get the input fields and save button
    const nameInput = document.querySelector('#name-input');
    const surnameInput = document.querySelector('#surname-input');
    const phoneInput = document.querySelector('#phone-input');
    const addressInput = document.querySelector('#address-input');
    const saveBtn = document.querySelector('#save-btn');

    // Function to show the save button
    function showSaveButton() {
        saveBtn.style.display = 'block';
    }

    // Add event listeners to input fields
    nameInput.addEventListener('input', showSaveButton);
    surnameInput.addEventListener('input', showSaveButton);
    phoneInput.addEventListener('input', showSaveButton);
    addressInput.addEventListener('input', showSaveButton);

});
