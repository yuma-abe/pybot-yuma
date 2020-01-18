import pandas
import pickle

def temp_command(command):
    temp,station=command.split()

    with open('trained-reg-model.pickle','rb')as b:
        reg=pickle.load(b)

    df=pandas.read_csv('data.csv',encoding='Shift_JIS')
    df_station=pandas.read_csv('amedas_stations.csv',encoding='Shift_JIS',index_col=0)

    df=df.join(df_station,on='station')

    row=df[df['station']==station]

    if len(row)>0:
        mean=row['temp'].mean()
        rounded_mean=round(mean,1) #小数をまとめる
        response='平均気温は{}度でした。'.format(rounded_mean)

    else:
        try:
            latitude=float(station)
            predicted=reg.predict([[latitude]])
            predicted_temp=predicted[0]
            rounded_temp=round(predicted_temp,1)
            responce='たぶん{}度くらい。'.format(rounded_temp)
        except ValueError:
            response='緯度を入力してください。'

    return response