def get_contacts():
    from private import secret
    RSA_KEY_FILE="private/privatekey.pem"
    CONSUMER_KEY= secret.consumer_key
    
    rsa_key=''
    with open(RSA_KEY_FILE) as keyfile:
        rsa_key = keyfile.read()
        
        
    from xero import Xero
    from xero.auth import PrivateCredentials
    
    credentials = PrivateCredentials(secret.consumer_key, secret.rsa_key_data)
    xero = Xero(credentials)
    
    all_contacts = xero.contacts.all()
    return all_contacts