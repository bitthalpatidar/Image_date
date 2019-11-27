<textarea id="textarea" rows=10 cols=80></textarea>
  <button id="button" onclick="toggleStartStop()"></button>

  <script type="text/javascript">
    var recognizing;
    var recognition = new SpeechRecognition();
    recognition.continuous = true;
    reset();
    recognition.onend = reset;

    recognition.onresult = function (event) {
      for (var i = resultIndex; i < event.results.length; ++i) {
        if (event.results.final) {
          textarea.value += event.results[i][0].transcript;
        }
      }
    }

    function reset() {
      recognizing = false;
      button.innerHTML = "Click to Speak";
    }

    function toggleStartStop() {
      if (recognizing) {
        recognition.stop();
        reset();
      } else {
        recognition.start();
        recognizing = true;
        button.innerHTML = "Click to Stop";
      }
    }
  </script>

