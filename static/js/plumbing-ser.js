const bookingSection = document.getElementById("booking");
const bookingServiceInput = document.getElementById("bookingService");
const bookingPriceInput = document.getElementById("bookingPrice");
const bookingTitle = document.getElementById("bookingTitle");
const serviceCards = document.querySelectorAll(".service-card");
const freeQuoteBtn = document.getElementById("freeQuoteBtn");

function openBooking(serviceName, price) {
  bookingServiceInput.value = serviceName || "General Plumbing Service";
  bookingPriceInput.value = price ? `$${price} / hour` : "";
  bookingTitle.textContent = serviceName ? `Book Service: ${serviceName}` : "Book a Service";
  bookingSection.classList.remove("hidden");
  bookingSection.scrollIntoView({ behavior: "smooth" });
}

serviceCards.forEach((card) => {
  card.addEventListener("click", () => {
    const serviceName = card.getAttribute("data-service");
    const price = card.getAttribute("data-price");
    openBooking(serviceName, price);
  });
});

freeQuoteBtn.addEventListener("click", (e) => {
  e.preventDefault();
  openBooking();
});
