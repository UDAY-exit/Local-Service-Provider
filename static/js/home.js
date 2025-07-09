// runnign images
const menuToggle = document.getElementById('menu-toggle');
const mobileMenu = document.getElementById('mobile-menu');

menuToggle.addEventListener('click', () => {
  mobileMenu.classList.toggle('show');
});

// Number section
function animateValue(id, start, end, duration, suffix = "") {
  const obj = document.getElementById(id);
  let current = start;
  const range = end - start;
  const increment = Math.ceil(range / (duration / 50)); // update every 50ms

  const timer = setInterval(() => {
    current += increment;
    if (current >= end) {
      current = end;
      clearInterval(timer);
    }
    obj.textContent = suffix === "+" ? current + "+" : current + suffix;
  }, 50);
}

animateValue("experts", 0, 150, 2000, "+");
animateValue("customers", 0, 10000, 3500, "+");
animateValue("serviceArea", 0, 1, 1500);
animateValue("services", 0, 12, 2500);



    
// enquiry section 
document.querySelector('form').addEventListener('submit', function (e) {
  const name = document.getElementById('name').value.trim();
  const mobile = document.getElementById('mobile').value.trim();

  if (!name || !mobile) {
    alert("Please fill in both name and mobile number.");
    e.preventDefault();  // ✅ keep this ONLY inside condition
    return;
  }

  // ✅ No need to reset here, Flask will redirect
  alert("Enquiry sent successfully!");
});

