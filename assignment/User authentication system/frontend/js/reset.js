const API_BASE_URL = "http://127.0.0.1:8000";

function setResetMessage(text, type = "") {
    const element = document.getElementById("reset-message");
    if (!element) {
        return;
    }

    element.textContent = text;
    element.className = "form-message";

    if (type) {
        element.classList.add(type);
    }
}

function getResetToken() {
    const params = new URLSearchParams(window.location.search);
    return params.get("token");
}

async function handleReset(event) {
    event.preventDefault();

    const token = getResetToken();
    if (!token) {
        setResetMessage("Reset token is missing from the link.", "error");
        return;
    }

    const form = event.currentTarget;
    const submitButton = form.querySelector("button[type='submit']");
    const formData = new FormData(form);
    const payload = {
        token,
        new_password: formData.get("new_password")?.toString(),
    };

    setResetMessage("");
    submitButton.disabled = true;

    try {
        const response = await fetch(`${API_BASE_URL}/reset-password`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(payload),
        });

        const data = await response.json().catch(() => ({}));

        if (!response.ok) {
            throw new Error(data.detail || "Unable to reset password.");
        }

        setResetMessage("Password reset successful. Redirecting to login...", "success");
        window.alert("Your password has been reset successfully.");
        window.setTimeout(() => {
            window.location.href = `${API_BASE_URL}/login.html`;
        }, 900);
    } catch (error) {
        setResetMessage(error.message || "Reset password failed.", "error");
        window.alert(error.message || "Reset password failed.");
    } finally {
        submitButton.disabled = false;
    }
}

const resetForm = document.getElementById("reset-form");
if (resetForm) {
    resetForm.addEventListener("submit", handleReset);
}
