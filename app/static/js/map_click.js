document.addEventListener("DOMContentLoaded", () => {
    const mapImage = document.getElementById("map-image");
    const marker = document.getElementById("map-marker");
    const savedMarker = document.getElementById("saved-marker");
    const mapWrapper = document.getElementById("map-wrapper");
    const xInput = document.getElementById("x");
    const yInput = document.getElementById("y");
    const coordsText = document.getElementById("coords-text");
    const saveButton = document.getElementById("save-kill-btn");

    if (!mapImage || !marker || !savedMarker || !mapWrapper || !xInput || !yInput || !coordsText || !saveButton) {
        return;
    }

    // Estado inicial: no hay nueva selección
    xInput.value = "";
    yInput.value = "";
    saveButton.disabled = true;

    function placeMarkerByPercent(markerElement, xPercent, yPercent) {
        const rect = mapImage.getBoundingClientRect();
        const pixelX = (xPercent / 100) * rect.width;
        const pixelY = (yPercent / 100) * rect.height;

        markerElement.style.display = "block";
        markerElement.style.left = `${pixelX}px`;
        markerElement.style.top = `${pixelY}px`;
    }

    function loadSavedMarker() {
        const lastX = mapWrapper.dataset.lastX;
        const lastY = mapWrapper.dataset.lastY;

        if (!lastX || !lastY) {
            savedMarker.style.display = "none";
            return;
        }

        placeMarkerByPercent(savedMarker, Number(lastX), Number(lastY));
    }

    mapImage.addEventListener("click", (event) => {
        const rect = mapImage.getBoundingClientRect();

        const clickX = event.clientX - rect.left;
        const clickY = event.clientY - rect.top;

        const xPercent = clickX / rect.width;
        const yPercent = clickY / rect.height;

        const mapX = Math.round(xPercent * 100);
        const mapY = Math.round(yPercent * 100);

        xInput.value = mapX;
        yInput.value = mapY;

        marker.style.display = "block";
        marker.style.left = `${clickX}px`;
        marker.style.top = `${clickY}px`;

        coordsText.textContent = `Nueva tumba seleccionada.`;
        saveButton.disabled = false;
    });

    mapImage.addEventListener("load", loadSavedMarker);
    window.addEventListener("resize", loadSavedMarker);

    if (mapImage.complete) {
        loadSavedMarker();
    }
});