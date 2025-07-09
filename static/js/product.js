const cart = {};



function renderCart() {
  const cartItems = document.getElementById('cart-items');
  cartItems.innerHTML = '';
  let total = 0;

  if (Object.keys(cart).length === 0) {
    cartItems.innerHTML = '<p>Your cart is empty.</p>';
    document.getElementById('order-button').disabled = true;
    document.getElementById('cart-total').textContent = 'Total: $0.00';
    return;
  }

  Object.entries(cart).forEach(([id, item]) => {
    const itemTotal = item.price * item.quantity;
    total += itemTotal;
    const div = document.createElement('div');
    div.innerHTML = `
      <p><strong>${item.name}</strong> - $${item.price.toFixed(2)} x ${item.quantity} = $${itemTotal.toFixed(2)}</p>
    `;
    cartItems.appendChild(div);
  });

  document.getElementById('cart-total').textContent = `Total: $${total.toFixed(2)}`;
  document.getElementById('order-button').disabled = false;
}

document.getElementById('order-button').addEventListener('click', () => {
  const cartArray = Object.entries(cart).map(([id, item]) => {
    return {
      name: item.name,
      price: item.price,
      quantity: item.quantity,
      total: item.price * item.quantity
    };
  });

  fetch('/submit_order', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ items: cartArray })
  })
  .then(response => response.json())
  .then(data => {
    alert('Order placed successfully!');
    // Optionally reset cart here
  })
  .catch(error => {
    console.error('Error submitting order:', error);
  });
});


function addToCart(id, name, price) {
  const qtyInput = document.getElementById(`qty-${id}`);
  let qty = parseInt(qtyInput.value);
  if (isNaN(qty) || qty < 1) qty = 1;
  if (cart[id]) {
    cart[id].quantity += qty;
  } else {
    cart[id] = { name, price, quantity: qty };
  }
  updateCartCount();
  alert(`Added ${qty} x ${name} to cart.`);
  qtyInput.value = 1;
}

document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.add-to-cart-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const id = btn.getAttribute('data-id');
      const product = btn.closest('.product');
      const name = product.querySelector('h3').textContent;
      const price = parseFloat(product.querySelector('.price').textContent.replace('$', ''));
      addToCart(id, name, price);
    });
  });

  document.getElementById('cart-button').addEventListener('click', () => {
    document.getElementById('cart-modal').classList.add('flex');
    renderCart();
  });

  document.getElementById('close-cart').addEventListener('click', () => {
    document.getElementById('cart-modal').classList.remove('flex');
  });

  document.getElementById('order-button').addEventListener('click', () => {
    alert('Order placed! Thank you.');
    Object.keys(cart).forEach(k => delete cart[k]);
    updateCartCount();
    renderCart();
    document.getElementById('cart-modal').classList.remove('flex');
  });

  document.getElementById('search-input').addEventListener('input', e => {
    const searchTerm = e.target.value.toLowerCase();
    document.querySelectorAll('.product').forEach(product => {
      const name = product.querySelector('h3').textContent.toLowerCase();
      const desc = product.querySelector('p').textContent.toLowerCase();
      product.style.display = (name.includes(searchTerm) || desc.includes(searchTerm)) ? 'block' : 'none';
    });
  });
});
