from flask import Flask, render_template, request as req, Response as response, json
from flask_cors import CORS
from model import getProducts
from binascii import a2b_base64
app = Flask(__name__)

res = {
  "Ponds Small":{
        'id': 101,
        'total_number':0,
        'total_rate':0,
        'rate':100,
    },
    "Ponds Large":{
        'id': 102,
        'total_number':0,
        'total_rate':0,
        'rate':200,
    },  
    "Crisp_Shine Small":{
        'id': 108,
        'total_number':0,
        'total_rate':0,
        'rate':50,
    },  
    "Crisp_Shine Large":{
        'id': 109,
        'total_number':0,
        'total_rate':0,
        'rate':100,
    },  
    "Dabur_Red_Tooth_Paste Small":{
        'id': 121,
        'total_number':0,
        'total_rate':0,
        'rate':10,
    },  
    "Dabur_Red_Tooth_Paste Large":{
        'id': 122,
        'total_number':0,
        'total_rate':0,
        'rate':80,
    },  
    "Harpic Small":{
        'id': 154,
        'total_number':0,
        'total_rate':0,
        'rate':100,
    },  
    "Harpic Large":{
        'id': 155,
        'total_number':0,
        'total_rate':0,
        'rate':150,
    },    
}

CORS(app, allow_headers=['Content-Type', 'Set-Cookie', '*'])

@app.route("/identify", methods=['post'])
def Hello():
    image = req.json['image']
    _, encoded = image.split(",", 1)
    fp = open('image.jpg', 'wb+')
    binary_data = a2b_base64(encoded)
    fp.write(binary_data)
    products = getProducts("image.jpg")
    print(products)

    for product in products:
        res[product]['total_number'] += 1
        res[product]['total_rate'] = res[product]['total_number'] * res[product]['rate']

    resp = response(json.dumps(res), status=200, mimetype='application/json')
    return resp

app.run(port=5000, debug=True)
