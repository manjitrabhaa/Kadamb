function copyToClipboard() {
  const quoteText = document.getElementById("quote-text");
  const authorText = document.getElementById("author-text");

  const el = document.createElement('textarea');
  el.value = `"${quoteText.innerText}" ${authorText.innerText}`;
  document.body.appendChild(el);
  el.select();
  document.execCommand('copy');
  document.body.removeChild(el);

//   showMessage('Copied!', 'success');
  
}

function showMessage(message, type) {
  const messageDiv = document.createElement('div');
  messageDiv.className = `message ${type}`;
  messageDiv.innerText = message;
  document.body.appendChild(messageDiv);

  // Position the message at the bottom center of the screen
  const messageWidth = messageDiv.offsetWidth;
  const screenWidth = window.innerWidth;
  messageDiv.style.left = `${(screenWidth - messageWidth) / 2}px`;
  messageDiv.style.bottom = '20px';

  setTimeout(() => {
    messageDiv.remove();
  }, 2000);
}


window.onload = () => {
  const copyForm = document.getElementById('copy-form');
  copyForm.onsubmit = (event) => {
    event.preventDefault();
    copyToClipboard();
  };
}
