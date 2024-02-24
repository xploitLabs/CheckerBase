from pyrogram import Client
from moduls.utils.utils import send_postdata

from apps.basics import welcome
from apps.basics import api_sample

from apps.prl412 import querys

@Client.on_callback_query()
async def controler(cliente, data_response):
    data = data_response.data
    function_name, postdata = data.split("-")[0], 0 if len(data.split("-")) == 1 else data.split("-")[1]

    if function_name == "start":
        send_postdata(function_name, postdata)
        await welcome.start(cliente, data_response.message)

    elif function_name == "ipQ":
        send_postdata(function_name, postdata)
        await api_sample.ipQuery(cliente, data_response.message)

    elif function_name == "rm":
        await data_response.message.delete()

    elif function_name == "prl412":
        send_postdata(function_name, postdata)
        await querys.queryPRL(cliente, data_response.message)
    
    else:
        await cliente.answer_callback_query(
            callback_query_id=data_response.id,
            text=f"""⏳ Al parecer este botón no tiene función asignada!. (Función: {function_name}, postdata: {postdata})""",
            show_alert="true"
        )
