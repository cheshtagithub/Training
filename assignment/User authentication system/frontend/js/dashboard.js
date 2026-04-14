const API_BASE_URL = "http://127.0.0.1:8000";

function getToken() {
    return localStorage.getItem("access_token");
}

function redirectToLogin() {
    window.location.href = `${API_BASE_URL}/login.html`;
}

function setDashboardMessage(text, type = "") {
    const element = document.getElementById("dashboard-message");
    if (!element) {
        return;
    }

    element.textContent = text;
    element.className = "form-message";

    if (type) {
        element.classList.add(type);
    }
}

async function loadDashboardProfile() {
    const token = getToken();
    if (!token) {
        redirectToLogin();
        return;
    }

    try {
        const response = await fetch(`${API_BASE_URL}/profile`, {
            headers: {
                Authorization: `Bearer ${token}`,
            },
        });

        const data = await response.json().catch(() => ({}));

        if (!response.ok) {
            throw new Error(data.detail || "Unable to load your profile.");
        }

        document.getElementById("dashboard-name").textContent = data.name || "Unknown user";
        document.getElementById("dashboard-email").textContent = data.email || "No email found";
        setDashboardMessage("Profile loaded successfully.", "success");
    } catch (error) {
        setDashboardMessage(error.message || "Session expired. Please login again.", "error");
        if (error.message?.toLowerCase().includes("credential")) {
            localStorage.removeItem("access_token");
            window.setTimeout(redirectToLogin, 1000);
        }
    }
}

function handleLogout() {
    localStorage.removeItem("access_token");
    redirectToLogin();
}

const logoutButton = document.getElementById("logout-button");
if (logoutButton) {
    logoutButton.addEventListener("click", handleLogout);
}

loadDashboardProfile();
