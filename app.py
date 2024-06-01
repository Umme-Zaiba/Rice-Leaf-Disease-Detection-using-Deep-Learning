from flask import Flask,request,render_template
from keras.utils import load_img
from keras.models import load_model
from keras.utils import img_to_array
from keras.applications.vgg16 import preprocess_input
import numpy as np
import cv2

app=Flask(__name__)

@app.route('/test',methods=['POST','GET'])
def test():
    model = load_model('cnn_dwnld_model.h5', compile=False)

    def check(res):
        p1 = ["brown_spot","healthy", "leaf_scald"]
        path = p1
        pred = model.predict(res)
        res = np.argmax(pred)
        res = path[res]
        print(res)
        return (res)

    def convert_img_to_tensor2(fpath):
        img = cv2.imread(fpath)
        img = cv2.resize(img, (256,256))
        res = img_to_array(img)
        res = np.array(res, dtype=np.float16) / 255.0
        res = res.reshape(-1, 256,256, 3)
        res = res.reshape(1, 256,256, 3)
        # print(res)
        return res

    if request.method == 'POST':
        img = request.files['img']
        img.save('static/h.jpg')
        res = convert_img_to_tensor2("static/h.jpg")
        msg = check(res)
        return render_template('result.html', res=msg)

    else:
        return render_template('rice.html', res="invalid input")

@app.route('/testown',methods=['POST','GET'])
def testown():
    model = load_model("cnn_model.h5", compile=False)



    def check(res):
            p1 = ["brown spot","healthy", "leaf scald"]
            path = p1
            pred = model.predict(res)
            res = np.argmax(pred)
            res = path[res]
            return (res)


    def convert_img_to_tensor2(fpath):
            img = cv2.imread(fpath)
            img = cv2.resize(img, (256,256))
            res = img_to_array(img)
            res = np.array(res, dtype=np.float16) / 255.0
            res = res.reshape(-1, 256,256 , 3)
            res = res.reshape(1, 256,256 , 3)
            return res

    if request.method == 'POST':
        img = request.files['img']
        img.save('static/h.jpg')
        res = convert_img_to_tensor2("static/h.jpg")
        msg = check(res)
        return render_template('result.html', res=msg)

    else:
        return render_template('rice.html', res="invalid input")

@app.route('/a',methods=['POST','GET'])
def choose():
    if request.method == 'POST':
        name = request.form.get("datasets")
        if name ==  "created":
            return render_template('riceown.html')
        else:
            return render_template('rice.html')
    return render_template('choosedataset.html')



@app.route('/',methods=['POST','GET'])
def index():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']

        if username=="admin" and password=="1234":
            return render_template('choosedataset.html')
        else:
            return render_template('login.html',msg="Login failed")

    return render_template('login.html')

if __name__=='__main__':
   app.run(debug=True,host="0.0.0.0")