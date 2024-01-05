import openai
from flask import Flask, render_template, request

app = Flask(__name__)

# Configura tu clave de API de OpenAI
openai.api_key = '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'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        
        # Llama a la API de OpenAI con el input del usuario
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=150
        )

        ai_output = response['choices'][0]['text']

        return render_template('index.html', user_input=user_input, ai_output=ai_output)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
