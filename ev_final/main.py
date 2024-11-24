from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        name = str(request.form['nombre'])
        edad = int(request.form['edad'])
        tarros = int(request.form['tarros'])
        descuento = 0
        valor = tarros * 9000
        valorTarros = tarros * 9000
        total = 0
        if edad >= 18 and edad <= 30 :
            descuento = valor * 0.15
            total = valor -  descuento
        elif edad > 30 :
            descuento = valor * 0.25
            total = valor -  descuento
        else :
            total = valorTarros     
        return render_template('ejercicio1.html',total=total, name=name, valorTarros=valorTarros, descuento=descuento)
    return render_template('ejercicio1.html')

if __name__ == '__main__':
    app.run()