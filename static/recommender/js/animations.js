// Silicon Valley Animations - Scroll Reveal
document.addEventListener('DOMContentLoaded', () => {

    // Observer Options
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    // Intersection Observer
    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target); // Only animate once
            }
        });
    }, observerOptions);

    // Target elements
    const animatedElements = document.querySelectorAll('.animate-fadeIn, .card, .hero, section h2, .wizard-step');

    animatedElements.forEach(el => {
        el.classList.add('reveal-on-scroll');
        observer.observe(el);
    });
});
