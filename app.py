from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculadora():
    resultado = None
    error = None
    
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operacion = request.form['operacion']
            
            if operacion == 'suma':
                resultado = num1 + num2
            elif operacion == 'resta':
                resultado = num1 - num2
            elif operacion == 'multiplicacion':
                resultado = num1 * num2
            elif operacion == 'division':
                if num2 == 0:
                    error = "Error: No se puede dividir entre cero"
                else:
                    resultado = num1 / num2
            else:
                error = "Operación no válida"
                
        except ValueError:
            error = "Error: Ingresa números válidos"
        except Exception as e:
            error = f"Error: {str(e)}"
    
    return render_template('index.html', resultado=resultado, error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

