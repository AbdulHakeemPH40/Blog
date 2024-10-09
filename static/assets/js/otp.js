document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll(".otp-input").forEach((input, index, inputs) => {
        input.addEventListener("input", function() {
            if (input.value.length === input.maxLength && index < inputs.length - 1) {
                inputs[index + 1].focus();
            }
        });

        // Ensure that only numeric input is allowed
        input.addEventListener("keypress", function(event) {
            if (event.which < 48 || event.which > 57) {
                event.preventDefault();
            }
        });

        // Handle backspace for previous input
        input.addEventListener("keydown", function(event) {
            if (event.key === "Backspace" && input.value.length === 0 && index > 0) {
                inputs[index - 1].focus();
            }
        });
    });
});
