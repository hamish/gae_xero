def get_contacts():
    from private import secret
    from xero import Xero
    from xero.auth import PrivateCredentials
    credentials = PrivateCredentials(secret.consumer_key, secret.rsa_key_data)
    xero = Xero(credentials)
    
    all_contacts = xero.contacts.all()
    return all_contacts