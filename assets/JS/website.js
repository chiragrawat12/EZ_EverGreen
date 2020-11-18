var state = false;
const spinner = document.querySelector('#loading');
const content = document.querySelector('#content');

function hide_show_password() {
    const password = document.getElementById('password');
    const toggle = document.getElementById('toggle');
    if (state) {
        password.setAttribute('type', 'password');
        toggle.setAttribute('value', 'Show');
        state = false;
    }
    else {
        password.setAttribute('type', 'text');
        toggle.setAttribute('value', 'Hide');
        state = true;
    }
}


function remember_me() {
    const remember = document.getElementById('remember');
    if (remember.checked) {
        remember.value = "yes";
    }
    else {
        remember.value = "no"
    }

}


window.addEventListener('load', function () {
    spinner.parentElement.removeChild(spinner);
    content.style.display = 'block';
})