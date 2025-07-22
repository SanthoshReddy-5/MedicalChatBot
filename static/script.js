const form = document.getElementById('chat-form');
const input = document.getElementById('user-input');
const chatContainer = document.getElementById('chat-container');

// Get formatted time
function getTime() {
  const now = new Date();
  return now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
}

function appendMessage(sender, text) {
  const msgDiv = document.createElement('div');
  msgDiv.classList.add('message', sender);

  // Convert markdown to HTML
  const content = sender === 'bot' ? marked.parse(text) : text;

  msgDiv.innerHTML = `
    <div class="content">${content}</div>
    <div class="meta">${getTime()}</div>
  `;
  chatContainer.appendChild(msgDiv);
  chatContainer.scrollTop = chatContainer.scrollHeight;
}

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const userMessage = input.value.trim();
  if (!userMessage) return;

  appendMessage('user', userMessage);
  input.value = '';

  try {
    const res = await fetch('/getAnswer', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: userMessage })
    });

    const data = await res.json();
    appendMessage('bot', data.response);
  } catch (err) {
    appendMessage('bot', 'Bot is not responding, please try again later!.');
    console.error(err);
  }
});
