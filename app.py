from flask import Flask, send_from_directory, render_template_string

app = Flask(__name__)

# HTML-шаблон с кнопкой для воспроизведения звука
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sound Button</title>
    <script>
        // Функция для запуска и приостановки звука
        let audio;
        window.onload = function() {
            audio = document.getElementById("audio");
        }

        function toggleAudio() {
            if (audio.paused) {
                audio.play();  // Запускаем звук
                document.getElementById("audioButton").innerText = "Pause Sound";  // Меняем текст кнопки
            } else {
                audio.pause();  // Приостанавливаем звук
                document.getElementById("audioButton").innerText = "Play Sound";  // Меняем текст кнопки
            }
        }
    </script>
</head>
<body>
    <h1>Добро пожаловать!</h1>
    <p>Слушайте звук, нажимая кнопку 🎵</p>
    <audio id="audio" autoplay>
        <source src="/static/sound.mp3" type="audio/mpeg">
        Ваш браузер не поддерживает элемент audio.
    </audio>
    <br>
    <!-- Кнопка для управления звуком -->
    <button id="audioButton" onclick="toggleAudio()">Pause Sound</button>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory("static", filename)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
