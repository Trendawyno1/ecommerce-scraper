const WHATSAPP_NUMBER = "201000000000"; // استبدل الرقم برقم العيادة بصيغة دولية بدون +
const form = document.getElementById('bookingForm');
const statusBox = document.getElementById('formStatus');
const serviceSelect = document.getElementById('serviceSelect');
const sticky = document.querySelector('.sticky-cta');
const menu = document.querySelector('[data-menu]');

document.getElementById('year').textContent = new Date().getFullYear();
const dateInput = form.querySelector('input[type="date"]');
const today = new Date();
const localISO = new Date(today.getTime() - today.getTimezoneOffset() * 60000).toISOString().split('T')[0];
dateInput.min = localISO;

document.querySelectorAll('.service-card').forEach(card => {
  card.addEventListener('click', () => {
    document.querySelectorAll('.service-card').forEach(c => c.classList.remove('is-selected'));
    card.classList.add('is-selected');
    serviceSelect.value = card.dataset.service;
    document.getElementById('booking').scrollIntoView({ behavior: 'smooth' });
  });
});

form.addEventListener('submit', (e) => {
  e.preventDefault();
  if (!form.checkValidity()) {
    statusBox.textContent = 'من فضلك كمّل البيانات المطلوبة علشان نقدر نأكد الحجز.';
    form.reportValidity();
    return;
  }
  const data = Object.fromEntries(new FormData(form).entries());
  const text = [
    'طلب حجز جديد من الموقع',
    `الاسم: ${data.name}`,
    `الموبايل: ${data.phone}`,
    `الخدمة: ${data.service}`,
    `اليوم المناسب: ${data.date}`,
    `الفترة: ${data.time}`,
    data.notes ? `ملاحظات: ${data.notes}` : ''
  ].filter(Boolean).join('\n');
  statusBox.textContent = 'تم تجهيز طلبك. سيتم فتح واتساب لإرساله لفريق العيادة.';
  const url = `https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(text)}`;
  window.open(url, '_blank', 'noopener');
});

document.querySelector('[data-menu-open]').addEventListener('click', () => {
  menu.hidden = false;
  document.body.style.overflow = 'hidden';
});
document.querySelector('[data-menu-close]').addEventListener('click', closeMenu);
menu.querySelectorAll('a').forEach(a => a.addEventListener('click', closeMenu));
function closeMenu(){ menu.hidden = true; document.body.style.overflow = ''; }
const bookingObserver = new IntersectionObserver(([entry]) => {
  sticky.classList.toggle('is-hidden', entry.isIntersecting);
}, { threshold: .25 });
bookingObserver.observe(document.getElementById('booking'));