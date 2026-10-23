const thumbs = document.querySelectorAll('.galeria-thumb');
const modal = document.getElementById('lightbox-modal');
const modalImg = document.getElementById('lightbox-img');
const btnFechar = document.querySelector('.lightbox-fechar');

thumbs.forEach((thumb) => {
    thumb.addEventListener('click', function () {
        modal.style.display = 'flex';
        modalImg.src = this.src;
    });
});

btnFechar.addEventListener('click', function () {
    modal.style.display = 'none';
});

modal.addEventListener('click', function (e) {
    if (e.target === modal) {
        modal.style.display = 'none';
    }
});
