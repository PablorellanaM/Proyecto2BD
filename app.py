from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    lineas = []

    if request.method == 'POST':
        aislamiento = request.form['aislamiento']
        usuarios = request.form['usuarios']

        resultado = subprocess.run(
            ['python', 'simulador.py', aislamiento, usuarios],
            capture_output=True,
            text=True
        )

        print("🧪 STDOUT:")
        print(resultado.stdout)
        print("🧪 STDERR:")
        print(resultado.stderr)

        # Combinamos salida estándar + errores para mostrarlos todos
        lineas = resultado.stdout.strip().split('\n') + resultado.stderr.strip().split('\n')

    return render_template('resultados.html', lineas=lineas)

if __name__ == '__main__':
    app.run(debug=True)
