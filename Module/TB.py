import logging
# Importing models and REST client class from Community Edition version
from tb_rest_client.rest_client_ce import *
# Importing the API exception
from tb_rest_client.rest import ApiException

def GetDeviceInfo(url,name,psw) :
    Info = ''

    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(module)s - %(lineno)d - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    # ThingsBoard REST API URL
    url = url
    # Default Tenant Administrator credentials
    username = name
    password = psw

    with RestClientCE(base_url=url) as rest_client:
        try:
            rest_client.login(username=username, password=password)
            user = rest_client.get_user()
            #print(user)

            res = rest_client.get_tenant_device_infos(page_size=str(10), page=str(0))
            
            #logging.info("Device info:\n%r", res)

            for i in range(len(res.data)) :
                Info = Info + str(res.data[i].name) + "<br>" + str(res.data[i].additional_info) + "<br><br>"
                #print(res.data[i].name)
                #print(res.data[i].additional_info)
        except ApiException as e:
            logging.exception(e)

    return Info

        