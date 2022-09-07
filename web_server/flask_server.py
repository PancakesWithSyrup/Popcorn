from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    comp12_occupied = True
    comp13_occupied = False
    comp14_occupied = True
    comp21_occupied = False
    comp22_occupied = True
    comp23_occupied = False
    comp24_occupied = True
    comp25_occupied = False
    comp31_occupied = True
    comp32_occupied = False
    comp33_occupied = True
    comp34_occupied = False
    comp35_occupied = True
    comp36_occupied = False
    return render_template('index.html', comp12_occupied = comp12_occupied, comp13_occupied = comp13_occupied, comp14_occupied = comp14_occupied,
                                        comp21_occupied = comp21_occupied, comp22_occupied = comp22_occupied, comp23_occupied = comp23_occupied,
                                        comp24_occupied = comp24_occupied, comp25_occupied = comp25_occupied, comp31_occupied = comp31_occupied,
                                        comp32_occupied = comp32_occupied, comp33_occupied = comp33_occupied, comp34_occupied = comp34_occupied,
                                        comp35_occupied = comp35_occupied, comp36_occupied = comp36_occupied)

@app.route("/update")
def update():
    pass
