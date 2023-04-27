document.addEventListener('DOMContentLoaded', function() {
    const messageTextarea = document.getElementById('message');
    const charCountSpan = document.getElementById('char-count');
    const analyzeBtn = document.getElementById('analyze-btn');

    function updateCharCount() {
        const charCount = messageTextarea.value.length;
        charCountSpan.textContent = `${charCount} characters`;
    }

    function toggleAnalyzeButton() {
        analyzeBtn.disabled = messageTextarea.value.trim().length === 0;
    }

    messageTextarea.addEventListener('input', function() {
        updateCharCount();
        toggleAnalyzeButton();
    });

    // Initialize character count and button state
    updateCharCount();
    toggleAnalyzeButton();
});
