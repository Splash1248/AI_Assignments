from flask import Flask, request, send_file
from PIL import Image, ImageDraw
import random
import io
import uuid

app = Flask(__name__)

captcha_db = {}


def create_captcha_image(question_text):
    img = Image.new('RGB', (120, 50), color=(255, 255, 255))
    d = ImageDraw.Draw(img)

    for _ in range(8):
        x1, y1 = random.randint(0, 120), random.randint(0, 50)
        x2, y2 = random.randint(0, 120), random.randint(0, 50)
        d.line([(x1, y1), (x2, y2)], fill=(150, 150, 150), width=2)

    d.text((20, 18), question_text, fill=(0, 0, 0))
    return img


@app.route('/')
def home():
    captcha_id = str(uuid.uuid4())

    html = f"""
    <h2>CAPTCHA</h2>
    <p>Prove you are human:</p>
    <img src="/captcha-image/{captcha_id}" alt="Captcha Image" style="border: 1px solid black;"><br><br>

    <form action="/verify" method="POST">
        <input type="hidden" name="captcha_id" value="{captcha_id}">
        Answer: <input type="text" name="user_answer" required>
        <button type="submit">Submit</button>
    </form>
    """
    return html


@app.route('/captcha-image/<captcha_id>')
def serve_image(captcha_id):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-'])

    answer = num1 + num2 if operator == '+' else num1 - num2
    captcha_db[captcha_id] = str(answer)

    img = create_captcha_image(f"{num1} {operator} {num2} = ?")

    buf = io.BytesIO()
    img.save(buf, format='PNG')
    buf.seek(0)
    return send_file(buf, mimetype='image/png')


@app.route('/verify', methods=['POST'])
def verify():
    user_answer = request.form.get('user_answer')
    captcha_id = request.form.get('captcha_id')

    correct_answer = captcha_db.get(captcha_id)

    # Clean up the database so it can't be reused
    if captcha_id in captcha_db:
        del captcha_db[captcha_id]

    if correct_answer and user_answer.strip() == correct_answer:
        return "<h3 style='color: green;'>Success! You are human.</h3><a href='/'>Try again</a>"
    else:
        return "<h3 style='color: red;'>Failed! Incorrect or expired.</h3><a href='/'>Try again</a>"


if __name__ == '__main__':
    print("\n\nGo to http://127.0.0.1:5000", end='\n\n\n')
    app.run(debug=True)
