from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
	if request.method == 'POST':
		# Pull data from html
		first_entry = request.form['first_entry']
		second_entry = request.form['second_entry']
		# Ensure the data is numeric and not a string or an invalid character
		try:
			float(first_entry)
			float(second_entry)
			result = float(first_entry) + float(second_entry)
			# To ensure integers are not displayed as decimals
			if result.is_integer():
				result = int(result)
				return render_template('add.html', result=result)
			else:
				return render_template('add.html', result=result)
		except ValueError:
			return render_template('add.html', result="Error")
	return render_template('add.html')

@app.route('/subtract', methods=['GET', 'POST'])
def subtract():
	if request.method == 'POST':
		first_entry = request.form['first_entry']
		second_entry = request.form['second_entry']
		try:
			float(first_entry)
			float(second_entry)
			result = float(first_entry) - float(second_entry)
			if result.is_integer():
				result = int(result)
				return render_template('subtract.html', result=result)
			else:
				return render_template('subtract.html', result=result)
		except ValueError:
			return render_template('subtract.html', result="Error")
	return render_template('subtract.html')

@app.route('/multiply', methods=['GET', 'POST'])
def multiply():
	if request.method == 'POST':
		first_entry = request.form['first_entry']
		second_entry = request.form['second_entry']
		try:
			float(first_entry)
			float(second_entry)
			result = float(first_entry) * float(second_entry)
			if result.is_integer():
				result = int(result)
				return render_template('multiply.html', result=result)
			else:
				return render_template('multiply.html', result=result)
		except ValueError:
			return render_template('multiply.html', result="Error")
	return render_template('multiply.html')

@app.route('/divide', methods=['GET', 'POST'])
def divide():
	if request.method == 'POST':
		first_entry = request.form['first_entry']
		second_entry = request.form['second_entry']
		try:
			float(first_entry)
			float(second_entry)
			result = float(first_entry) / float(second_entry)
			if result.is_integer():
				result = int(result)
				return render_template('divide.html', result=result)
			else:
				return render_template('divide.html', result=result)
		except ValueError:
			return render_template('divide.html', result="Error")
	return render_template('divide.html')

if __name__ == '__main__':
	app.run(debug=True)

