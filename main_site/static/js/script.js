/* Toggle Navbar Visibility */

nav = document.getElementById('site_nav');
nav_btn = document.getElementById('nav_btn');

nav_btn.addEventListener('click', () => {
   nav.classList.toggle('show');
});