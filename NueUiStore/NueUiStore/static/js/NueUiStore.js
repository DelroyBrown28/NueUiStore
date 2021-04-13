$(document).ready(function () {
  $('.sidenav').sidenav();
});

const aboutButton = document.querySelector('.nav-about-button');
const closeAboutButton = document.querySelector('.about-page-close-btn');
// const navOpen = document.querySelector('nav-open');


// Stops animation from playing unless refreshed
const tl = new TimelineLite({
  paused: true,
  reversed: true
});

tl.to('.art-cards, .cta-wrap', 0.3, {
    autoAlpha: 0,
    stagger: 0.1,
    ease: Power2.easeOut,
  })
  .to('.artist-feature-section', 0.3, {
    autoAlpha: 1,
    ease: Power2.easeOut,
  })
  .to('.about-page-close-btn', 0.3, {
    autoAlpha: 1,
    ease: Power2.easeOut,
  })
  
  

// Button to toggle animation
aboutButton.addEventListener('click', () => {

  if (tl.isActive()) {
    e.preventDefault();
    e.stopImmediatePropagation();
    return false;
  }
  toggleTween(tl)
})

closeAboutButton.addEventListener('click', () => {

  if (tl.isActive()) {
    e.preventDefault();
    e.stopImmediatePropagation();
    return false;
  }
  toggleTween(tl)
})

function toggleTween(tween) {
  tween.reversed() ? tween.play() : tween.reverse();
}