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

async function postReview(text, rating, place_id) {
  const textBox = document.getElementById("review-text");
  const response = await fetch("http://127.0.0.1:5000/api/v1/reviews/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${getCookie("token")}`,
    },
    body: JSON.stringify({ text, rating, place_id }),
  });

  if (response.ok) {
    alert("Review submitted successfully!");
    textBox.value = "";
  } else {
    alert("Failed to submit review");
  }
}

function checkAuthentication() {
  const token = getCookie("token");
  const loginLink = document.getElementById("login-link");
  const reviewForm = document.getElementById("review-form");

  if (!token) {
    loginLink.style.display = "block";

    if (reviewForm) {
      reviewForm.style.display = "none";
    }
  } else {
    loginLink.style.display = "none";

    if (reviewForm) {
      reviewForm.style.display = "block";
    }
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

async function fetchPlace(id, token) {
  const response = await fetch(`http://127.0.0.1:5000/api/v1/places/${id}`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
      "Access-Control-Allow-Origin": "*",
    },
  });

  if (response.ok) {
    const data = await response.json();
    displayPlace(data);
  }
}

function displayPlaces(places) {
  const list = document.getElementById("places-list").children[0];
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
    link.href = `place.html?id=${place.id}`;

    card.appendChild(title);
    card.appendChild(description);
    card.appendChild(link);
    li.appendChild(card);
    list.appendChild(li);
  });
}

function displayPlace(place) {
  const title = document.getElementById("title");
  const host = document.getElementById("host");
  const price = document.getElementById("price");
  const description = document.getElementById("description");
  const amenities = document.getElementById("amenities");

  title.textContent = place.title;
  host.textContent = `${place.owner.first_name} ${place.owner.last_name}`;
  price.textContent = `$${place.price}`;
  description.textContent = place.description;

  if (place.amenities.length <= 0) {
    const child = document.createElement("li");
    child.textContent = "None";
    amenities.appendChild(child);
  } else {
    place.amenities.forEach((place) => {
      const child = document.createElement("li");
      child.textContent = place.name;
      amenities.appendChild(child);
    });
  }

  fetchReviews(place.id, getCookie("token"));
}

async function fetchReviews(place_id, token) {
  const response = await fetch(
    `http://127.0.0.1:5000/api/v1/places/${place_id}/reviews`,
    {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
        "Access-Control-Allow-Origin": "*",
      },
    },
  );

  if (response.ok) {
    const data = await response.json();
    displayReviews(data);
  }
}

function displayReviews(reviews) {
  const list = document.getElementById("reviews").children[1];
  console.log(reviews);
  list.textContent = "";
  reviews.forEach((review) => {
    const li = document.createElement("li");
    const card = document.createElement("div");

    const ptext = document.createElement("p");
    const btext = document.createElement("b");

    const prating = document.createElement("p");
    const brating = document.createElement("b");

    const text = document.createElement("span");
    const rating = document.createElement("span");

    card.classList.add("card", "shadow");

    btext.textContent = `${review.user.first_name} ${review.user.last_name}: `;
    brating.textContent = "Rating: ";

    text.textContent = review.text;
    rating.textContent = review.rating;

    ptext.appendChild(btext);
    ptext.appendChild(text);

    prating.appendChild(brating);
    prating.appendChild(rating);

    card.appendChild(ptext);
    card.appendChild(prating);
    li.appendChild(card);
    list.appendChild(li);
  });
}

function getUrlId() {
  const parameters = new URLSearchParams(window.location.search);
  return parameters.get("id");
}

document.addEventListener("DOMContentLoaded", () => {
  const loginForm = document.getElementById("login-form");
  const reviewForm = document.getElementById("review-form");
  const priceFilter = document.getElementById("price-filter");
  const placeDetails = document.getElementById("place-details");

  if (loginForm) {
    loginForm.addEventListener("submit", async (e) => {
      e.preventDefault();
      const formData = new FormData(e.target);
      const email = formData.get("email");
      const password = formData.get("password");
      loginUser(email, password);
    });
  }

  if (reviewForm) {
    reviewForm.addEventListener("submit", async (e) => {
      e.preventDefault();
      const formData = new FormData(e.target);
      const text = formData.get("review-text");
      const rating = parseInt(formData.get("rating"), 10);
      const place = getUrlId();

      postReview(text, rating, place);
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
        const place = places[i];
        place_price = parseInt(place.firstChild.dataset.price, 10);

        if (place_price <= value || value < 0) {
          place.style.display = "block";
        } else {
          place.style.display = "none";
        }
      }
    });
  }

  if (placeDetails) {
    const id = getUrlId();
    const token = getCookie("token");

    fetchPlace(id, token);
  }

  checkAuthentication();
});
