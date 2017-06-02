function show_otp() {
	var id = document.getElementById('otp_div');
	if (id.style.display === 'none') {
		id.style.display = 'block';
	} else {
		id.style.display = 'none';
	}
}