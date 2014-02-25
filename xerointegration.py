import webapp2
import jinja2
import os
from google.appengine.ext import ndb
import logging

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class Contact(ndb.Model):
    name=ndb.StringProperty()
    email=ndb.StringProperty()
    xero_guid = ndb.StringProperty()

class InvoiceLine(ndb.Model):
    description = ndb.StringProperty()
    amount_cents = ndb.IntegerProperty()

class Invoice(ndb.Model):
    contact_key = ndb.KeyProperty()
    line_items = ndb.LocalStructuredProperty(InvoiceLine, repeated=True)

class MakeInvoice(webapp2.RequestHandler):
    def get(self):
        from private import secret
        template_values={}
        template = JINJA_ENVIRONMENT.get_template('make_invoice.html')
        RSA_KEY_FILE="private/privatekey.pem"
        CONSUMER_KEY= secret.consumer_key
        
        from xero.api import Xero
        from xero.auth import PrivateCredentials
        with open(RSA_KEY_FILE) as keyfile:
            rsa_key = keyfile.read()
        credentials = PrivateCredentials(CONSUMER_KEY, rsa_key)
        logging.info(rsa_key)
        logging.info(CONSUMER_KEY)
        xero = Xero(credentials)
        
        all_contacts = xero.contacts.all()
        logging.info(all_contacts)
        self.response.write(template.render(template_values))        
 
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        
        template_values={
        'all_contacts' : Contact.query().fetch(),
        'all_invoices' : Invoice.query().fetch(),
        }
        
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/make_invoice', MakeInvoice),
], debug=True)
