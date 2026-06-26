const topicInput = document.getElementById('topicInput');
const searchBtn = document.getElementById('searchBtn');
const statusDiv = document.getElementById('status');
const resultsDiv = document.getElementById('results');
const feedHeader = document.getElementById('feedHeader');
const emptyState = document.getElementById('emptyState');

const BACKEND_URL = 'http://127.0.0.1:5000';

async function summarizeTopic() {
    const topic = topicInput.value.trim();

    if (!topic) {
        showStatus('enter a topic to search', true);
        return;
    }

    resultsDiv.innerHTML = '';
    feedHeader.style.display = 'none';
    emptyState.style.display = 'none';
    showStatus('fetching articles and summarizing...', false);
    setLoading(true);

    try {
        const response = await fetch(`${BACKEND_URL}/summarize`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ topic })
        });

        const data = await response.json();

        if (!response.ok) {
            showStatus(data.error || 'something went wrong. please try again.', true);
            emptyState.style.display = 'block';
            return;
        }

        showStatus(`done — ${data.summaries.length} stories on "${data.topic}"`, false);
        feedHeader.style.display = 'flex';
        renderResults(data.summaries);

    } catch (err) {
        showStatus('could not reach the server — is the backend running?', true);
        emptyState.style.display = 'block';
        console.error(err);
    } finally {
        setLoading(false);
    }
}

function renderResults(summaries) {
    resultsDiv.innerHTML = summaries.map((item, i) => `
        <div class="card" style="animation-delay: ${i * 60}ms">
            <span class="card-index">STORY ${String(i + 1).padStart(2, '0')}</span>
            <h3>${escapeHtml(item.title)}</h3>
            <p class="summary">${escapeHtml(item.summary)}</p>
            <div class="meta">
                <span class="source">${escapeHtml(item.source)}</span>
                <a href="${item.url}" target="_blank" rel="noopener noreferrer">Read full article &rarr;</a>
            </div>
        </div>
    `).join('');
}

function showStatus(message, isError) {
    statusDiv.textContent = message;
    statusDiv.className = isError ? 'status-line error' : 'status-line';
}

function setLoading(isLoading) {
    searchBtn.disabled = isLoading;
    searchBtn.classList.toggle('loading', isLoading);
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text || '';
    return div.innerHTML;
}

searchBtn.addEventListener('click', summarizeTopic);
topicInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') summarizeTopic();
});