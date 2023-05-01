function summarizer() {
    var text = document.getElementById('text').value.trim();
    
    if (text === '') {
        document.getElementById('summarize_text').innerHTML = 'Please Enter Some Text';
	updateCount();
        return;
    }
    
    fetch('/text-summarizer', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            text: text
        })
    })
    .then(function(response) {
        return response.json();
    })
    .then(function(data) {
        var predictionText = data.summarizeText;
        document.getElementById('summarize_text').innerHTML = predictionText;
        
        const predictionDiv = document.getElementById('summarize_text');
        const animation = anime({
          targets: predictionDiv,
          translateY: ["-100%", 0],
          opacity: [0, 1],
          scale: [0.5, 1],
          duration: 1000,
          easing: "spring(1, 80, 10, 0)",
          delay: 500
        });
	updateCount();
    })
    .catch(function(error) {
        document.getElementById('summarize_text').innerHTML = 'Error: ' + error.message;
    });
}


function updateCount() {
                var text = document.getElementById('text').value;
                var textCount = text.length + ' characters, ' + text.trim().split(/\s+/).length + ' words';
                document.getElementById('text-count').textContent = textCount;

                var summarize = document.getElementById('summarize-container').textContent;
                var summarizeCount =  summarize.trim().split(/\s+/).length + ' words';
                document.getElementById('summarize-count').textContent = summarizeCount;
            }