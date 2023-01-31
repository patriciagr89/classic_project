import requests

class allCoinApi:
    def __init__(self):
        self.criptos=[]

    def getcripto(self, APIKEY, coin_from, coin_to):

        url = "https://rest.coinapi.io/v1/assets/?apikey={APIKEY}" #guardamos la cadena de texto que contiene la direccion que queremos consultar
        data = requests.get(url) #creamos variable que va a recibir el request get

        if data.status_code == 200: #todo correcto podemos continuar
            data = data.json() #convertimos el data en json 
            for item in data:
                print("todo va bien")

        else:
            print("Error")



