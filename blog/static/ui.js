function toggle_metadata() {

	toggle = document.getElementById("metadata-toggle");
	content = document.getElementById("metadata-content");

	if (content.checkVisibility()) {
		toggle.innerHTML = "&plus;";
		content.style.display = "none";
	} else {
		toggle.innerHTML = "&minus;";
		content.style.display = "block";
	}
	
}
