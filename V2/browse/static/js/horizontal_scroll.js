const scrollMovie = document.querySelector(".popular-movies");
const scrollSerie = document.querySelector(".popular-series");

scrollMovie.addEventListener("wheel", (evt) => {
    evt.preventDefault();
    scrollMovie.scrollLeft += evt.deltaY;
});
scrollSerie.addEventListener("wheel", (evt) => {
    evt.preventDefault();
    scrollSerie.scrollLeft += evt.deltaY;
});