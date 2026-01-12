// Determine backend URL based on environment
const BASE_URL =
  window.location.hostname === "localhost" ||
  window.location.hostname === "127.0.0.1"
    ? "http://127.0.0.1:8000"
    : "http://frontend-service:80"; // Access via LoadBalancer in cluster

function show(data) {
  const out = document.getElementById("out");
  if (out) out.textContent = JSON.stringify(data, null, 2);
  else console.log(data);
}

async function login() {
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  try {
    const res = await fetch(`${BASE_URL}/api/login`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      credentials: "include",
      body: JSON.stringify({ email, password })
    });

    const data = await res.json();
    if (res.ok) show({ message: "Login successful", user: data });
    else show({ error: data.error || "Invalid credentials" });
  } catch (err) {
    show({ error: err.toString() });
  }
}

async function publicApi() {
  try {
    const res = await fetch(`${BASE_URL}/api/rest-galaxy/public-info`, {
      credentials: "include"
    });
    const data = await res.json();
    show(data);
  } catch (err) {
    show({ error: err.toString() });
  }
}

async function profile() {
  try {
    const res = await fetch(`${BASE_URL}/api/user-rest-galaxy/profile`, {
      credentials: "include"
    });
    const data = await res.json();
    if (res.ok) show(data);
    else show({ error: data.error || "Profile fetch failed" });
  } catch (err) {
    show({ error: err.toString() });
  }
}

// Event listeners
document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("loginBtn")?.addEventListener("click", login);
  document.getElementById("publicBtn")?.addEventListener("click", publicApi);
  document.getElementById("profileBtn")?.addEventListener("click", profile);
});

