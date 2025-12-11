
############ Uso: python emailgoogle.py <asunto> <mensaje> <destino>

from email.message import EmailMessage
import smtplib
import logging
import json
import sys

logging.basicConfig(
        filename='emailgoogle.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def enviar(config):
    ASUNTO = sys.argv[1]
    MENSAJE = sys.argv[2]
    DESTINO = sys.argv[3]

    msg = EmailMessage()
    msg['From'] = config['CORREO']
    msg.set_content(MENSAJE)
    msg['Subject'] = ASUNTO
    msg['To'] = DESTINO

    try:
        with smtplib.SMTP_SSL(config['SERVIDOR'], config['PUERTO']) as smtp:
            smtp.login(config['CORREO'], config['API_KEY'])
            smtp.send_message(msg)
    
    except Exception as e:
        logging.error(f'EXCEPCION NO MANEJADA: {e}')
        sys.exit(1)
    
    logging.info(f'CORREO ENVIADO DE [ {config['CORREO']} ] A [ {DESTINO} ]')

if __name__ == '__main__':
    if len(sys.argv) == 4:
        try:
            with open('config.json') as arch_conf:
                config = json.load(arch_conf)

            for i in range(100):
                enviar(config)
        except Exception as e:
            logging.error(f'ERROR EN ARCHIVO DE CONFIGURACION. {e}')
    else:    
        print('Uso: python enviar_email.py <asunto> <mensaje> <destino>')
        logging.error('ERROR DE PARAMETROS.')
        sys.exit(2)

