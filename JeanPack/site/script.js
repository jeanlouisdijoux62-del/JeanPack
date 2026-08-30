// Navigation toggle for small screens
document.addEventListener('click', (e) => {
  if (e.target.closest('.nav-toggle')){
    const btn = e.target.closest('.nav-toggle');
    const menu = document.getElementById('main-menu');
    const expanded = btn.getAttribute('aria-expanded') === 'true';
    btn.setAttribute('aria-expanded', String(!expanded));
    menu.classList.toggle('show');
  }
});

// Contact form handling: accessible confirmation message
document.addEventListener('submit', e => {
  if (e.target.matches('.contact-form')) {
    e.preventDefault();
    const form = e.target;
    let msg = form.querySelector('.form-message');
    if (!msg){
      msg = document.createElement('div');
      msg.className = 'form-message';
      msg.setAttribute('role','status');
      msg.style.marginTop = '12px';
      form.appendChild(msg);
    }
    msg.textContent = 'Message envoyé (simulation). Merci !';
    msg.style.color = '#064e3b';
    form.reset();
  }
});

// Smooth scrolling for internal links
document.querySelectorAll('a[href^="#"]').forEach(a=>{
  a.addEventListener('click', e=>{
    const href = a.getAttribute('href');
    if (href.length>1){
      const el = document.querySelector(href);
      if (el){ e.preventDefault(); el.scrollIntoView({behavior:'smooth'}); }
    }
  })
});

