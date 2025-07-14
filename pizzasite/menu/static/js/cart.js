console.log("Skrypt JS dla koszyka działa! ");

let cart = JSON.parse(localStorage.getItem("cart")) || {};

function addToCart(id, name, price) {
    console.log(`Dodawanie do koszyka: ${name}, ID: ${id}, Cena: ${price}`);
    if (!cart[id]) {
        cart[id] = { name: name, price: price, quantity: 0 };
    }
    cart[id].quantity += 1;
    localStorage.setItem("cart", JSON.stringify(cart));
    alert(`${name} dodano do koszyka! 🛒`);
}

function updateCart() {
    let cartList = document.getElementById("cart-items");
    let totalPrice = 0;
    cartList.innerHTML = "";

    for (let id in cart) {
        let pizza = cart[id];
        let row = document.createElement("tr");
        row.innerHTML = `
            <td>${pizza.name}</td>
            <td>${pizza.price} PLN</td>
            <td>${pizza.quantity}</td>
            <td>
                <button onclick="changeQuantity(${id}, 1)">➕</button>
                <button onclick="changeQuantity(${id}, -1)">➖</button>
            </td>
        `;
        cartList.appendChild(row);
        totalPrice += pizza.price * pizza.quantity;
    }

    document.getElementById("total-price").innerText = `Razem: ${totalPrice.toFixed(2)} PLN`;
    localStorage.setItem("cart", JSON.stringify(cart));
}

function changeQuantity(id, change) {
    if (cart[id]) {
        cart[id].quantity += change;
        if (cart[id].quantity <= 0) {
            delete cart[id];
        }
    }
    updateCart();
}

function getCsrfToken() {
    let token = document.querySelector('[name=csrfmiddlewaretoken]')?.value;
    console.log("CSRF Token:", token);
    return token || "";
}

function submitOrder() {
    if (Object.keys(cart).length === 0) {
        alert("Twój koszyk jest pusty!");
        return;
    }

    let confirmation = confirm("Czy na pewno chcesz złożyć zamówienie?");
    if (!confirmation) return;

    fetch("/order/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCsrfToken()
        },
        body: JSON.stringify({ cart: cart })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Błąd podczas składania zamówienia: " + response.status);
        }
        return response.json();
    })
    .then(data => {
        console.log("Serwer odpowiedział:", data);
        alert("✅ Zamówienie zostało złożone!");
        cart = {};
        localStorage.setItem("cart", JSON.stringify(cart));
        updateCart();
        openPopup();
    })
    .catch(error => {
        console.error("Błąd:", error);
        alert("🚨 Błąd podczas składania zamówienia.");
    });
}

function openPopup() {
    document.getElementById("order-popup").style.display = "flex";
}

function closePopup() {
    document.getElementById("order-popup").style.display = "none";
}


window.onload = updateCart;
window.addToCart = addToCart;
window.updateCart = updateCart;
window.changeQuantity = changeQuantity;
window.submitOrder = submitOrder;
window.openPopup = openPopup;
window.closePopup = closePopup;
