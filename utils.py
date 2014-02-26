import logging
def get_contacts():
    rsa_key_file='private/privatekey.pem'
    rsa_key_data=''
    with open(rsa_key_file) as keyfile:
        rsa_key_data = keyfile.read()
    logging.info ("rsa_key_data:\n%s" % rsa_key_data)
    from private import secret
    from xero import Xero
    from xero.auth import PrivateCredentials
    credentials = PrivateCredentials(secret.consumer_key, rsa_key_data)
    xero = Xero(credentials)
    
    all_contacts = xero.contacts.all()
    return all_contacts