
        function countCharacters() {
            var text = document.querySelector('textarea').value;
            var charCount = text.length;
            document.querySelector('#charCount').innerHTML = charCount;
        }
        
        function countWords() {
            var text = document.querySelector('textarea').value;
            var wordCount = text.trim().split(/\s+/).length;
            document.querySelector('#wordCount').innerHTML = wordCount;
        }



        function shareOnTwitter() {
            var text = document.querySelector('p').textContent;
            var url = "https://twitter.com/intent/tweet?text=" + encodeURIComponent(text);
            window.open(url, "_blank");
        }
        
        function shareOnFacebook() {
            var text = document.querySelector('p').textContent;
            var url = "https://www.facebook.com/sharer/sharer.php?u=" + encodeURIComponent(text);
            window.open(url, "_blank");
        }
        
        function shareByEmail() {
            var text = document.querySelector('p').textContent;
            var subject = "Check out this summary";
            var body = text;
            var url = "mailto:?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(body);
            window.open(url, "_blank");
        }
