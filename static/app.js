const form = document.getElementById('chatForm');
const input = document.getElementById('messageInput');
const send = document.getElementById('sendButton');
const messagesEl = document.getElementById('messages');
const welcome = document.getElementById('welcome');
const history = [];

function addMessage(role, text) {
  welcome.style.display = 'none';
  const row = document.createElement('div');
  row.className = 'message ' + role;
  const avatar = document.createElement('div');
  avatar.className = 'avatar';
  avatar.textContent = role === 'user' ? 'คุณ' : 'J';
  const bubble = document.createElement('div');
  bubble.className = 'bubble';
  bubble.textContent = text;
  row.append(avatar, bubble);
  messagesEl.append(row);
  return bubble;
}

async function sendMessage(text) {
  if (!text.trim()) return;
  addMessage('user', text);
  history.push({role: 'user', content: text});
  input.value = '';
  send.disabled = true;
  send.textContent = '…';
  const bubble = addMessage('assistant', 'กำลังคิดคำตอบ…');

  try {
    const response = await fetch('/api/chat', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({messages: history})
    });
    const data = await response.json();
    if (!response.ok) throw new Error(data.error || 'เกิดข้อผิดพลาด');
    bubble.textContent = data.reply;
    history.push({role: 'assistant', content: data.reply});
  } catch (err) {
    bubble.textContent = 'แจ้งเตือน: ' + err.message;
  } finally {
    send.disabled = false;
    send.textContent = '➤';
  }
}

form.addEventListener('submit', e => {
  e.preventDefault();
  sendMessage(input.value);
});

document.querySelectorAll('[data-text]').forEach(button => {
  button.addEventListener('click', () => sendMessage(button.dataset.text));
});

document.getElementById('newChat').addEventListener('click', () => {
  history.length = 0;
  messagesEl.innerHTML = '';
  welcome.style.display = 'block';
});

document.getElementById('mobileMenu').addEventListener('click', () => {
  document.querySelector('.sidebar').classList.toggle('open');
});
