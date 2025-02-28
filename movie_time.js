function buyTicket(callback) {
    console.log("🎫 Ticket purchased. Waiting for the movie to start...");
    setTimeout(() => {
        console.log("🍿 Movie is ready! Enter the hall.");
        callback(); // Call the function after movie starts
    }, 3000);
}
function watchMovie() {
    console.log("🎬 Enjoying the movie!");
}
buyTicket(watchMovie);
