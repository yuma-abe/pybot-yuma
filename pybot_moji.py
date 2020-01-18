import numpy
from PIL import Image,ImageEnhance,ImageOps
import pickle

def moji_command(image):
    if not image:  #画像がアップロードされていない場合
        return '画像を指定してください'

    #学習済みモデルのロード
    with open('traind-model.pickle','rb')as b:
        clf=pickle.load(b)

    #前処理
    im = Image.open(image.file)
    im=ImageEnhance.Brightness(im).enhance(2)
    im=im.convert(mode='L')
    im=im.resize((8,8))
    im=ImageOps.invert(im)
    X_bin=numpy.asarray(im)
    X_bin=X_bin.reshape(1,64)
    X_bin=X_bin*(16/255)

    #予測
    y_pred=clf.predict(X_bin)
    y_pred=y_pred[0]

    return 'この数字は「{}」です。'.format(y_pred)