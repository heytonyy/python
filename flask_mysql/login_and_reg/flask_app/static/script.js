function reg_success(){
    alert('You have successfully created an account!');
}

// Toasts success alert
function toastSuccessAlert() {
    halfmoon.initStickyAlert({
        content: "You have successfully created an account!",
        title: "Success!",
        alertType: "alert-success",
        fillType: "filled-lm"
    });
}