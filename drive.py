from google.oauth2 import service_account
from googleapiclient.discovery import build
import gspread

class AccessDrive:
    def __init__(self):
        self.credenciales_json = 'client.json'
        self.credenciales = service_account.Credentials.from_service_account_file(
            self.credenciales_json, 
            scopes=['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/spreadsheets'] # permisos de spreadhets y drive
        )
        self.drive_service = build('drive', 'v3', credentials=self.credenciales)
        self.client = gspread.authorize(self.credenciales)
    def get_first_requeriment(self,id_data,
        pestaña,
        searchDepartamento,
        searchProvincia,
        searchDistrito):
        # tener una query que se base en la recopilacion
        # de las pestañas especificas y se junte por nombre de pestaña definida
        sheet = self.client.open_by_key(id_data) # nombre de pagina
        sheet7 = sheet.worksheet(pestaña) ## pestaña | CAC | CADENAS | ACD
        data = sheet7.get_all_records()
        data_tiendas = []
        for row in data:
            department = row.get("DEPARTAMENTO")
            provincia = row.get("PROVINCIA")
            distrito = row.get("DISTRITO")
            if department == searchDepartamento and provincia == searchProvincia and distrito == searchDistrito:
                # ACD => NOMBRE DEL DAC
                # CADENAS => 
                # CAC => NOMBRE DEL CAC
                nombre_tienda = row.get("NOMBRE DEL CAC")
                data_tiendas.append(nombre_tienda)
        if(0 < len(data_tiendas)):
            print(data_tiendas)
        else:
            print("no hay tiendas actuales")

    def get_second_requeriment(self,id_data):
        sheet = self.client.open_by_key(id_data).sheet1 # nombre de pagina
        data = sheet.get_all_records()
        i=1
        data_planes=[]
        for row in data:
            plan = row.get('Planes')
            print(f" {i} Plan: {plan}")
            i+=1
            data_planes.append(plan)
        selected = input("Seleccione el plan: ")
        nombre_plan = data_planes[int(selected)-1]
        plan_encontrado = list(filter(lambda x: x['Planes'] == nombre_plan, data))
        if plan_encontrado:
            plan_array = plan_encontrado[0] # acceder al objeto
            # print(plan_array.values()) dict_values(['a', 'b', 'c'])
            key_values =  list(plan_array.values()) # listar y accedera los valores y pasar a array cada valor  [planes,cargo_fijo,descuento,etc]
            cargo_fijo = key_values[1] 
            descuento_3_mes = key_values[2] 
            descuento_12_mes = key_values[3] 
            print(f"Cargo Fijo {cargo_fijo}")
            print(f"Descuento 3° mes {descuento_3_mes}")
            print(f"Descuento 12° mes {descuento_12_mes}")
        else:
            print(f"Plan '{nombre_plan}' no encontrado")
    def get_thrid_requeriment(self):
        pass
