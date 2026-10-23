const slides = document.querySelectorAll('.slide');
const btnPrev = document.querySelector('.anterior');
const btnNext = document.querySelector('.proximo');
let currentIndex = 0;
let autoPlayInterval;

function updateSlide() {
    slides.forEach((slide, index) => {
        if (index === currentIndex) {
            slide.style.display = 'block';
        } else {
            slide.style.display = 'none';
        }
    });
}

function nextSlide() {
    currentIndex++;
    if (currentIndex >= slides.length) {
        currentIndex = 0;
    }
    updateSlide();
}

function prevSlide() {
    currentIndex--;
    if (currentIndex < 0) {
        currentIndex = slides.length - 1;
    }
    updateSlide();
}

function startAutoPlay() {
    autoPlayInterval = setInterval(nextSlide, 4000);
}

function stopAutoPlay() {
    clearInterval(autoPlayInterval);
}

btnNext.addEventListener('click', () => {
    nextSlide();
    stopAutoPlay();
    startAutoPlay();
});

btnPrev.addEventListener('click', () => {
    prevSlide();
    stopAutoPlay();
    startAutoPlay();
});

const banner = document.querySelector('.banner-carrossel');
if (banner) {
    banner.addEventListener('mouseenter', stopAutoPlay);
    banner.addEventListener('mouseleave', startAutoPlay);
}

updateSlide();
startAutoPlay();

