document.addEventListener("DOMContentLoaded", function() {
var alerts = document.querySelectorAll('.alert');
	alerts.forEach(function(alert) {
		setTimeout(function() {
			if (alert) {	
				alert.classList.remove('show');
				setTimeout(function() {
					alert.remove();
				}, 200);
			}// Duration of the fade animation
		}, 3000); // Display alert for 4 seconds (4000 milliseconds)
	});
    var currentProgress = 0;
    var progressBar = document.getElementById('dynamic');
	if (progressBar) {
		var interval = setInterval(function() {
			currentProgress += 25;
			progressBar.style.width = currentProgress + "%";
			progressBar.setAttribute("aria-valuenow", currentProgress);
			if (currentProgress >= 100) {
				clearInterval(interval);
			}
		}, 700);
	}
});
