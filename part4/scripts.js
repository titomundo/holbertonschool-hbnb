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

  if (loginForm) {
    loginForm.addEventListener("submit", async (e) => {
      e.preventDefault();
      const formData = new FormData(e.target);
      const email = formData.get("email");
      const password = formData.get("password");
      loginUser(email, password);
    });
  }

  checkAuthentication();
});
