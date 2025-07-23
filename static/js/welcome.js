document.addEventListener("DOMContentLoaded", () => {
    const audio = document.getElementById("money-audio");
    if (audio) {
        audio.volume = 0.7;
        audio.play().catch(e => {
            console.log("Autoplay blocked:", e);
        });
    }
});
