function formatRemaining(targetDate) {
    const now = new Date();
    const diff = targetDate - now;

    if (diff <= 0) {
        return "ya disponible";
    }

    const totalSeconds = Math.floor(diff / 1000);
    const hours = Math.floor(totalSeconds / 3600);
    const minutes = Math.floor((totalSeconds % 3600) / 60);
    const seconds = totalSeconds % 60;

    const parts = [];

    if (hours > 0) {
        parts.push(`${hours}h`);
    }

    if (minutes > 0 || hours > 0) {
        parts.push(`${minutes}m`);
    }

    parts.push(`${seconds}s`);

    return parts.join(" ");
}

function updateCountdowns() {
    const minElements = document.querySelectorAll(".countdown-min");
    const maxElements = document.querySelectorAll(".countdown-max");

    minElements.forEach((element) => {
        const dateString = element.dataset.datetime;
        const targetDate = new Date(dateString);
        element.textContent = formatRemaining(targetDate);
    });

    maxElements.forEach((element) => {
        const dateString = element.dataset.datetime;
        const targetDate = new Date(dateString);
        element.textContent = formatRemaining(targetDate);
    });
}

document.addEventListener("DOMContentLoaded", () => {
    updateCountdowns();
    setInterval(updateCountdowns, 1000);
});