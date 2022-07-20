
import json

# >>> Ingrese la ruta donde se encuentra el archivo JSON que quiere analizar <<< #
# Formato: with open("ruta.json", "r") as file:

with open("Sprint5//eventos_gold.json", "r") as file:
    contenido = file.read()

a_json = json.loads(contenido) #Cargar el JSON

###################### CREACIÓN DE CLASES ######################

class Razon:
    def __init__(self, type):
        self.type = type

    def resolver(self, razon):
        self.razon = razon
        return razon

    def __repr__(self):
        return f"{self.razon}"

class Transaction:
    def __init__(self, numero, fecha, tipo, estado, monto):
        self.numero = numero
        self.fecha = fecha
        self.tipo = tipo
        self.estado = estado
        self.monto = monto

    def __repr__(self):
        return f"{self.numero, self.fecha, self.tipo, self.estado, self.monto}"
           
class RetiroEfectivo(Razon):
    def __init__(self, type, monto, cupoDiarioRestante, saldoEnCuenta):
        self.type = type
        self.monto = monto
        self.cupoDiarioRestante = cupoDiarioRestante
        self.saldoEnCuenta = saldoEnCuenta

        if(monto<=cupoDiarioRestante and saldoEnCuenta >= monto):
            Razon.resolver(self, "")

        elif (monto>cupoDiarioRestante):
            Razon.resolver(self, "Cupo diario insuficiente.")
        
        elif (type == "GOLD"):
            if(saldoEnCuenta - monto) < -10000:
                Razon.resolver(self, "Fondos insuficientes.")
            else:
                Razon.resolver(self, "")
        elif (type == "BLACK"):
            if(saldoEnCuenta - monto) < -10000:
                Razon.resolver(self, "Fondos insuficientes.")
            else:
                Razon.resolver(self, "")


class AltaTarjetaCredito(Razon):
    def __init__(self, type, totalTarjetas):
        self.type = type
        self.totalTarjetas = totalTarjetas

        if(type == "CLASSIC"):
            Razon.resolver(self, "No puedes tener")
        elif(type == "GOLD"):
            if(totalTarjetas > 1):
                Razon.resolver(self, "Máximo 1 tarjeta!")
            else:
                Razon.resolver(self, "")
        elif(type == "BLACK"):
            if(totalTarjetas > 5):
                Razon.resolver(self, "Máximo 5 tarjetas!")
            else:
                Razon.resolver(self, "")


class AltaChequera(Razon):
    def __init__(self, type, totalChequeras):
        self.type = type
        self.totalChequeras = totalChequeras

        if(type == "CLASSIC"):
            Razon.resolver(self, "No puedes tener")
        elif(type == "GOLD"):
            if(totalChequeras > 1):
                Razon.resolver(self, "Máximo 1 chequera!")
            else:
                Razon.resolver(self, "")
        elif(type == "BLACK"):
            if(totalChequeras > 2):
                Razon.resolver(self, "Máximo 2 chequeras!")
            else:
                Razon.resolver(self, "")
      

class ComprarDolar(Razon):
    def __init__(self, type, monto, saldoEnCuenta):
        self.type = type
        self.monto = monto
        self.saldoEnCuenta = saldoEnCuenta

        if (type == "CLASSIC"):
            Razon.resolver(self, "No puedes comprar dólares")
        elif (type == "GOLD"):
            if(saldoEnCuenta - monto) < -10000:
                Razon.resolver(self, "Saldo insuficiente!")
            else:
                Razon.resolver(self, "")
        elif (type == "BLACK"):
            if(saldoEnCuenta - monto) < -10000:
                Razon.resolver(self, "Saldo insuficiente!")
            else:
                Razon.resolver(self, "")


class TransferenciaEnviada(Razon):
    def __init__(self, type, monto, saldoEnCuenta):
        self.type = type
        self.monto = monto
        self.saldoEnCuenta = saldoEnCuenta

        if (type == "CLASSIC"):
            if saldoEnCuenta < (monto + 0.1*saldoEnCuenta):
                Razon.resolver(self, "Saldo insuficiente!")
            else:
                Razon.resolver(self, "")
        elif (type == "GOLD"):
            if (saldoEnCuenta - (monto + 0.05*saldoEnCuenta)) < -10000:
                Razon.resolver(self, "Saldo insuficiente!")
            else:
                Razon.resolver(self, "")
        elif (type == "BLACK"):
            if (saldoEnCuenta - monto) < -10000:
                Razon.resolver(self, "Saldo insuficiente!")
            else:
                Razon.resolver(self, "")
                    

class TransferenciaRecibida(Razon):
    def __init__(self, type, monto):
        self.type = type
        self.monto = monto

        if (type == "CLASSIC"):
            if monto > 150000:
                Razon.resolver(self, "Máx. transferencia $150000")
            else:
                Razon.resolver(self, "")
        elif (type == "GOLD"):
            if monto > 500000:
                Razon.resolver(self, "Máx. transferencia $500000")
            else:
                Razon.resolver(self, "")
        else:
            Razon.resolver(self, "")


class Cliente(object):
    direccion = ""
    transaccion = [] #array de objetos, donde cada objeto es una transaccion
    razon = [] #array de todas las razones sobre por qué fue rechazado
    def __init__(self, nombre, apellido, numero, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.numero = numero
        self.dni = dni
  
    
class Classic(Cliente):
    def __init__(self, nombre, apellido, numero, dni):
        Cliente.__init__(self, nombre, apellido, numero, dni)
        
class Gold(Cliente):
    def __init__(self, nombre, apellido, numero, dni):
        Cliente.__init__(self, nombre, apellido, numero, dni)

class Black(Cliente):
    def __init__(self, nombre, apellido, numero, dni):
        Cliente.__init__(self, nombre, apellido, numero, dni)

class Direccion(object):
    def __init__(self, calle, numero, ciudad, provincia, pais):
        self.calle = calle
        self.numero = numero
        self.ciudad = ciudad
        self.provincia = provincia
        self.pais = pais
    
    def __repr__(self):
        return f"{self.calle} {self.numero} {self.ciudad} {self.provincia} {self.pais}"

###################### FILTRAR SEGÚN TIPO DE CLIENTE ######################

if a_json["tipo"] == "CLASSIC":
    client = Classic(
        a_json["nombre"],
        a_json["apellido"],
        a_json["numero"],
        a_json["dni"],        
    )
elif a_json["tipo"] == "GOLD":
    client = Gold(
        a_json["nombre"],
        a_json["apellido"],
        a_json["numero"],
        a_json["dni"],  
    )
elif a_json["tipo"] == "BLACK":
    client = Black(
        a_json["nombre"],
        a_json["apellido"],
        a_json["numero"],
        a_json["dni"],  
    )    
else:
    raise Exception(f"Cliente {a_json['tipo']} no válido.")

client.direccion = Direccion(
    a_json["direccion"]["calle"],
    a_json["direccion"]["numero"],
    a_json["direccion"]["ciudad"],
    a_json["direccion"]["provincia"],
    a_json["direccion"]["pais"],
)


i = 0   #Iterador para acceder a una cada transacción

for t in a_json["transacciones"]:

    #Cargar todas las transacciones en un array client.transaccion[]
    transaccion_x = Transaction(        
        a_json["transacciones"][i]["numero"],
        a_json["transacciones"][i]["fecha"],
        a_json["transacciones"][i]["tipo"],
        a_json["transacciones"][i]["estado"],
        a_json["transacciones"][i]["monto"],
    )
    client.transaccion.append(transaccion_x)

###################### VALIDACIONES ######################

    #Cargar todas las razones en un array client.razon[]

    if a_json["transacciones"][i]["tipo"] == "RETIRO_EFECTIVO_CAJERO_AUTOMATICO":
        razon_x = RetiroEfectivo(
            a_json["tipo"],
            a_json["transacciones"][i]["monto"],
            a_json["transacciones"][i]["cupoDiarioRestante"],
            a_json["transacciones"][i]["saldoEnCuenta"],
        )
        client.razon.append(razon_x)   

    if a_json["transacciones"][i]["tipo"] == "ALTA_TARJETA_CREDITO":
        razon_x = AltaTarjetaCredito(
            a_json["tipo"],
            a_json["transacciones"][i]["totalTarjetasDeCreditoActualmente"],
        )
        client.razon.append(razon_x)

    if a_json["transacciones"][i]["tipo"] == "ALTA_CHEQUERA":
        razon_x = AltaChequera(
            a_json["tipo"],
            a_json["transacciones"][i]["totalChequerasActualmente"],
        )
        client.razon.append(razon_x)

    if a_json["transacciones"][i]["tipo"] == "COMPRA_DOLAR":
        razon_x = ComprarDolar(
            a_json["tipo"],
            a_json["transacciones"][i]["monto"],
            a_json["transacciones"][i]["saldoEnCuenta"],
        )
        client.razon.append(razon_x)

    if a_json["transacciones"][i]["tipo"] == "TRANSFERENCIA_ENVIADA":
        razon_x = TransferenciaEnviada(
            a_json["tipo"],
            a_json["transacciones"][i]["monto"],
            a_json["transacciones"][i]["saldoEnCuenta"],
        )
        client.razon.append(razon_x)

    if a_json["transacciones"][i]["tipo"] == "TRANSFERENCIA_RECIBIDA":
        razon_x = TransferenciaRecibida(
            a_json["tipo"],
            a_json["transacciones"][i]["monto"],
        )
        client.razon.append(razon_x)

    i+=1 #Incrementa el iterador



###################### GENERAR HTML ######################


table_rows = ''

for i in range(0, len(client.transaccion)):
    table_rows += '<tr>'
    
    table_rows += f"<td>{client.transaccion[i].numero}</td>"
    table_rows += f"<td>{client.transaccion[i].fecha}</td>"
    table_rows += f"<td>{client.transaccion[i].tipo}</td>"
    table_rows += f"<td>{client.transaccion[i].estado}</td>"
    table_rows += f"<td>{client.transaccion[i].monto}</td>"
     
    table_rows += f"<td>{client.razon[i]}</td>"
   
    table_rows += '</tr>'
    table_rows += '<tr class="spacer"><td colspan="100"></td></tr>'

import codecs

with codecs.open("Sprint5//test.html", "w", "utf-8") as file:
    html_content = f"""

<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link href="https://fonts.googleapis.com/css?family=Roboto:300,400&display=swap" rel="stylesheet">

    <link rel="stylesheet" href="fonts/icomoon/style.css">

    <link rel="stylesheet" href="css/owl.carousel.min.css">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css">
    
    <!-- Style -->
    <link rel="stylesheet" href="style.css">

    <title>Reporte ITBANK</title>
  </head>
  <body>
  
  <div class="content">   
    <div class="container">
      <h1 class="mb-5">Reporte Transacciones - Cliente {type(client).__name__}</h1>
      <div class="container">
        <table class="table custom-table">
            <thead>
              <tr>  
                <th scope="col">Nombre</th>
                <th scope="col">Número</th>
                <th scope="col">DNI</th>
                <th scope="col">Dirección</th> 
              </tr>
            </thead>

            <tbody>
                <tr scope="row">
                  <td>{client.nombre}</td>
                  <td>{client.numero}</td>
                  <td>{client.dni}</td>
                  <td>{client.direccion}</td>
                </tr>
            </table>
      </div>


      <div class="table-responsive custom-table-responsive">
        
        <table class="table custom-table">
            
            <br><br><br><br>
            <h2 class="mb-5">Historial de Transacciones</h2>
          <thead>
            <tr>  
              <th scope="col">Número</th>
              <th scope="col">Fecha</th>
              <th scope="col">Tipo</th>
              <th scope="col">Estado</th>
              <th scope="col">Monto</th>
              <th scope="col">Razón Rechazo</th>
            </tr>
          </thead>

          <tbody>
            <tr scope="row">
              
              {table_rows}
            </tr>

            <tr class="spacer"><td colspan="100"></td></tr>

          </tbody>
        </table>
      </div>

    </div>

  </div>
  </body>
</html>

file.write(html_content)

"""

    file.write(html_content)
