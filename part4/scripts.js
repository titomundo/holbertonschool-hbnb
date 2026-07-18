async function loginUser(email, password) {
  const response = await fetch("http://127.0.0.1:5000/api/v1/auth/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ email, password }),
  });

  if (response.ok) {
    const data = await response.json();
    document.cookie = `token=${data.access_token}; path=/`;
    window.location.href = "index.html";
  } else {
    alert("Login failed: " + response.statusText);
  }
}

function checkAuthentication() {
  const token = getCookie("token");
  const loginLink = document.getElementById("login-link");

  if (!token) {
    loginLink.style.display = "block";
  } else {
    loginLink.style.display = "none";
    fetchPlaces(token);
  }
}

function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);

  if (parts.length === 2) {
    return parts.pop().split(";").shift();
  }
}

async function fetchPlaces(token) {
  const response = await fetch("http://127.0.0.1:5000/api/v1/places/", {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
      "Access-Control-Allow-Origin": "*",
    },
  });

  if (response.ok) {
    const data = await response.json();
    displayPlaces(data);
  }
}

function displayPlaces(places) {
  list = document.getElementById("places-list").children[0];
  list.textContent = "";

  places.forEach((place) => {
    const li = document.createElement("li");
    const card = document.createElement("div");
    const title = document.createElement("h3");
    const description = document.createElement("p");
    const link = document.createElement("a");

    card.classList.add("card", "shadow");
    card.dataset.price = place.price;
    title.textContent = place.title;
    description.textContent = `Price per night: $${place.price}`;
    link.textContent = "See details";
    link.href = `http://127.0.0.1:5000/api/v1/places/${place.id}`;

    card.appendChild(title);
    card.appendChild(description);
    card.appendChild(link);
    li.appendChild(card);
    list.appendChild(li);
  });
}

document.addEventListener("DOMContentLoaded", () => {
  const loginForm = document.getElementById("login-form");
  const token = getCookie("token");
  const priceFilter = document.getElementById("price-filter");

  if (loginForm) {
    loginForm.addEventListener("submit", async (e) => {
      e.preventDefault();
      const formData = new FormData(e.target);
      const email = formData.get("email");
      const password = formData.get("password");
      loginUser(email, password);
    });
  }

  if (priceFilter) {
    const prices = [10, 50, 100];
    const default_opt = document.createElement("option");
    default_opt.value = -1;
    default_opt.textContent = "All";
    priceFilter.appendChild(default_opt);

    prices.forEach((price) => {
      option = document.createElement("option");
      option.value = price;
      option.textContent = price;

      priceFilter.appendChild(option);
    });

    priceFilter.addEventListener("change", (event) => {
      const value = parseInt(event.target.selectedOptions[0].value, 10);
      const places =
        document.getElementById("places-list").children[0].children;

      for (var i = 0; i < places.length; i++) {
        place = places[i];
        place_price = parseInt(place.firstChild.dataset.price, 10);

        if (place_price <= value || value < 0) {
          place.style.display = "block";
        } else {
          place.style.display = "none";
        }
      }
    });
  }

  checkAuthentication();
});
