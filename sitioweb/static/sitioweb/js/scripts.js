document.addEventListener('DOMContentLoaded', function() {
    const galleryModal = document.getElementById('galleryModal');
    
    if (galleryModal) {
        galleryModal.addEventListener('show.bs.modal', function (event) {
            const triggerElement = event.relatedTarget;
            const slideIndex = triggerElement.getAttribute('data-bs-slide-to');
            const carouselElement = document.getElementById('modalCarousel');
            
            if (carouselElement) {
                const carousel = bootstrap.Carousel.getOrCreateInstance(carouselElement);
                carousel.to(slideIndex);
            }
        });
    }
});