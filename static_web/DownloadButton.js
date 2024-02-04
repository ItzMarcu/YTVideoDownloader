
const downloadButton = document.getElementById('download');
let linkText = document.getElementById('link-text');

function changeButtonState () {
    if (linkText.value === '') {
        downloadButton.disabled = true;
    } else {
        downloadButton.disabled = false;
    }
}

linkText.addEventListener('input', changeButtonState);
changeButtonState();