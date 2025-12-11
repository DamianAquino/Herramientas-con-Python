import mercadopago
import json

with open("conf.json", "r") as f:
    conf = json.load(f)

sdk = mercadopago.SDK(conf['token'])

# La preferencia es un objeto que cuenta con la informacion del cobro (monto, expiracion, medios de pago, etc)
preference_data = {
    "items": [
        {
            "title": "ELEMENTO VENTIDO",
            "quantity": 1,
            # Pesos artentinos
            "unit_price": 100.00,
        }
    ],
    "back_urls": {
        "success": "URL A LA QUE SE REDIRIGE AL USUARIO CUANDO MERCADO PAGO ACREDITA EL COBRO",
        "failure": "URL A LA QUE SE REDIRIGE AL USUARIO CUANDO MERCADO PAGO NO ACREDITA EL COBRO",
        "pending": "URL A LA QUE SE REDIRIGE AL USUARIO CUANDO EL PAGO QUEDA PENDIENTE"
    },
    "auto_return": "approved"
}

preference_response = sdk.preference().create(preference_data)
preference = preference_response["response"]
print(preference)
