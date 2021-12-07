
import json
import Module.postgresql as postgresql

Setting_Dir_Name = "Setting"

def DBInI() :
    settings_path = Setting_Dir_Name + "//" + "settings.json"

    with open(settings_path,'r') as f:
        setting_dict =  json.load(f)

    PDB = postgresql.PostgresDB(
        setting_dict["DbName"],
        setting_dict["DbUser"],
        setting_dict["DbPassword"],
        setting_dict["DbHost"],
        setting_dict["DbPort"]
    )

    # 上線後不與資料庫斷線?
    PDB.ConnectToDB()

    return PDB


    

    