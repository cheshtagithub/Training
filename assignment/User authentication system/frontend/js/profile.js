const API_BASE_URL = "http://127.0.0.1:8000";

function redirectToLogin() {
    window.location.href = `${API_BASE_URL}/login.html`;
}

function setProfileMessage(text, type = "") {
    const element = document.getElementById("profile-message");
    if (!element) {
        return;
    }

    element.textContent = text;
    element.className = "form-message";

    if (type) {
        element.classList.add(type);
    }
}

async function loadProfile() {
    const token = localStorage.getItem("access_token");
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

        document.getElementById("profile-name").textContent = data.name || "Unknown user";
        document.getElementById("profile-email").textContent = data.email || "No email found";
        setProfileMessage("Your profile details are up to date.", "success");
    } catch (error) {
        setProfileMessage(error.message || "Please login again.", "error");
        if (error.message?.toLowerCase().includes("credential")) {
            localStorage.removeItem("access_token");
            window.setTimeout(redirectToLogin, 1000);
        }
    }
}

loadProfile();
