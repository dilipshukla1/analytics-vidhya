const BASE_URL = "/api";

async function login() {
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  const res = await fetch(`${BASE_URL}/login/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    credentials: "include",
    body: JSON.stringify({ email, password }),
  });

  const data = await res.json();
  document.getElementById("out").textContent =
    JSON.stringify(data, null, 2);
}

async function profile() {
  const res = await fetch(
    `${BASE_URL}/user-rest-galaxy/profile/`,
    { credentials: "include" }
  );

  const data = await res.json();
  document.getElementById("out").textContent =
    JSON.stringify(data, null, 2);
}

