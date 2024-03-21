from flask import Flask, render_template, request

app = Flask(__name__)

# Define your model function here
def process_inputs(data):
    # Here you would put your model code to process the input data
    # For demonstration purposes, let's just return the input data as it is
    return data

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        date_of_birth = request.form['date_of_birth']
        cycle = int(request.form['cycle'])
        weight_gain = bool(request.form['weight_gain'])
        hair_growth = bool(request.form['hair_growth'])
        skin_darkening = bool(request.form['skin_darkening'])
        fast_food = bool(request.form['fast_food'])
        follicle_no_l = int(request.form['follicle_no_l'])
        follicle_no_r = int(request.form['follicle_no_r'])

        input_data = {
            'name': name,
            'date_of_birth': date_of_birth,
            'cycle': cycle,
            'weight_gain': weight_gain,
            'hair_growth': hair_growth,
            'skin_darkening': skin_darkening,
            'fast_food': fast_food,
            'follicle_no_l': follicle_no_l,
            'follicle_no_r': follicle_no_r
        }

        processed_data = process_inputs(input_data)
        return render_template('result.html', input_data=input_data, processed_data=processed_data)
    return render_template('index.html')    

if __name__ == '__main__':
    app.run(debug=True)
