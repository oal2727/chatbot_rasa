import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
import gspread
from access_drive import AccessDrive

# Ruta al archivo JSON de credenciales descargado
# credenciales_json = 'client.json'
id_data_first="12A3H_oObBcuFZNw87rUv8ABsNT06AQIOQK1RN0IFBHU"
id_data_two = "1e_X0EDRha5_cegrHyPFptrKRHmrgenr8m7nQPOMliGk" # descuentos
# credenciales = service_account.Credentials.from_service_account_file(
#     credenciales_json, 
#     scopes=['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/spreadsheets'] # permisos de spreadhets y drive
# )
# Crear una instancia del servicio de Google Drive
# drive_service = build('drive', 'v3', credentials=credenciales)
# client = gspread.authorize(credenciales)

# sheet = client.open_by_key(id_data).sheet1 # nombre de pagina
# data = sheet.get_all_records()

ad = AccessDrive()
pestaña = "CAC"
departamento = "LIMA"
provincia = "LIMA"
distrito = "CERCADO"

ad.get_first_requeriment(id_data_first,pestaña,departamento,provincia,distrito)
# ad.get_second_requeriment(id_data)





## acceso a drive y google sheet
## para trabajar con json crear una cuenta de servicio

# recordar que el json lo obtengo del servicio mismo de la cuenta(seccion de classes)
# video : https://www.youtube.com/watch?v=jeZWv5PQJAk
# caso para acceder directamente al archivo
# 1. crear cuenta de servcio , definir el rol y depues de esto ir al mismo servicio , seccion claves para agregar como json

# recordar compartir la cuenta de correo servicio para visualizar