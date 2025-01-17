from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Função para conectar ao banco de dados
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Rota principal para exibir dados da tabela
@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sat_bd")
    data = cursor.fetchall()
    conn.close()
    return render_template('index.html', data=data)

# Rota para criar um novo registro
@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        dbn = request.form['DBN']
        school_name = request.form['School Name']
        num_of_test_takers = request.form['Number of Test Takers']
        reading_score = request.form['Critical Reading Mean']
        math_score = request.form['Mathematics Mean']
        writing_score = request.form['Writing Mean']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO sat_bd (DBN, "School Name", "Number of Test Takers", "Critical Reading Mean", "Mathematics Mean", "Writing Mean") VALUES (?, ?, ?, ?, ?, ?)',
                     (dbn, school_name, num_of_test_takers, reading_score, math_score, writing_score))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('create.html')

# Rota para atualizar um registro
@app.route('/update/<dbn>', methods=('GET', 'POST'))
def update(dbn):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM sat_bd WHERE DBN = ?', (dbn,))
    record = cursor.fetchone()
    conn.close()

    if request.method == 'POST':
        school_name = request.form['School Name']
        num_of_test_takers = request.form['Number of Test Takers']
        reading_score = request.form['Critical Reading Mean']
        math_score = request.form['Mathematics Mean']
        writing_score = request.form['Writing Mean']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE sat_bd SET "School Name" = ?, "Number of Test Takers" = ?, "Critical Reading Mean" = ?, "Mathematics Mean" = ?, "Writing Mean" = ? WHERE DBN = ?',
                     (school_name, num_of_test_takers, reading_score, math_score, writing_score, dbn))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    return render_template('update.html', record=record)

# Rota para deletar um registro
@app.route('/delete/<dbn>', methods=('POST',))
def delete(dbn):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM sat_bd WHERE DBN = ?', (dbn,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)