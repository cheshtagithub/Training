const API_BASE_URL = "http://127.0.0.1:8000";

function goToPage(path) {
    window.location.href = `${API_BASE_URL}${path}`;
}

function setMessage(element, text, type = "") {
    if (!element) {
        return;
    }

    element.textContent = text;
    element.className = "form-message";

    if (type) {
        element.classList.add(type);
    }
}

async function parseResponse(response) {
    const data = await response.json().catch(() => ({}));
    if (!response.ok) {
        throw new Error(data.detail || "Something went wrong. Please try again.");
    }

    return data;
}

async function handleSignup(event) {
    event.preventDefault();

    const form = event.currentTarget;
    const message = document.getElementById("signup-message");
    const submitButton = form.querySelector("button[type='submit']");
    const formData = new FormData(form);

    const payload = {
        name: formData.get("name")?.toString().trim(),
        email: formData.get("email")?.toString().trim(),
        password: formData.get("password")?.toString(),
    };

    setMessage(message, "");
    submitButton.disabled = true;

    try {
        const response = await fetch(`${API_BASE_URL}/signup`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(payload),
        });

        await parseResponse(response);

        setMessage(message, "Signup successful. Redirecting to login...", "success");
        window.setTimeout(() => {
            goToPage("/login.html");
        }, 900);
    } catch (error) {
        const userMessage =
            error instanceof TypeError
                ? "Cannot reach the FastAPI server. Make sure it is running on http://127.0.0.1:8000."
                : error.message || "Unable to sign up";
        setMessage(message, userMessage, "error");
    } finally {
        submitButton.disabled = false;
    }
}

async function handleLogin(event) {
    event.preventDefault();

    const form = event.currentTarget;
    const message = document.getElementById("login-message");
    const submitButton = form.querySelector("button[type='submit']");
    const formData = new FormData(form);

    const payload = {
        email: formData.get("email")?.toString().trim(),
        password: formData.get("password")?.toString(),
    };

    setMessage(message, "");
    submitButton.disabled = true;

    try {
        const response = await fetch(`${API_BASE_URL}/login`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(payload),
        });

        const data = await parseResponse(response);

        localStorage.setItem("access_token", data.access_token);
        setMessage(message, "Login successful. Redirecting to dashboard...", "success");
        window.setTimeout(() => {
            goToPage("/dashboard.html");
        }, 900);
    } catch (error) {
        const userMessage =
            error instanceof TypeError
                ? "Cannot reach the FastAPI server. Make sure it is running on http://127.0.0.1:8000."
                : error.message || "Unable to login";
        setMessage(message, userMessage, "error");
    } finally {
        submitButton.disabled = false;
    }
}

async function handleForgotPassword(event) {
    event.preventDefault();

    const form = event.currentTarget;
    const message = document.getElementById("forgot-message");
    const submitButton = form.querySelector("button[type='submit']");
    const formData = new FormData(form);

    const payload = {
        email: formData.get("email")?.toString().trim(),
    };

    setMessage(message, "");
    submitButton.disabled = true;

    try {
        const response = await fetch(`${API_BASE_URL}/forgot-password`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(payload),
        });

        const data = await parseResponse(response);
        setMessage(
            message,
            data.message || "Reset link sent. Please check your email.",
            "success",
        );
    } catch (error) {
        const userMessage =
            error instanceof TypeError
                ? "Cannot reach the FastAPI server. Make sure it is running on http://127.0.0.1:8000."
                : error.message || "Unable to send reset link";
        setMessage(message, userMessage, "error");
    } finally {
        submitButton.disabled = false;
    }
}

const signupForm = document.getElementById("signup-form");
if (signupForm) {
    signupForm.addEventListener("submit", handleSignup);
}

const loginForm = document.getElementById("login-form");
if (loginForm) {
    loginForm.addEventListener("submit", handleLogin);
}

const forgotPasswordForm = document.getElementById("forgot-password-form");
if (forgotPasswordForm) {
    forgotPasswordForm.addEventListener("submit", handleForgotPassword);
}
