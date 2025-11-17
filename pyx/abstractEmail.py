#abstraction

class EmailsService:
    def  _connect(self):
        print("connecting to email server")

    def _authentication(self):
        print("auth..")
# public def
    def send_email(self):
        self._connect()
        self._authenticate
        print("sending email..")
        self._discounnect()

    def _discounnect(self):
        print("Disconnecting from server...")

# next step
email = EmailsService()
email.send_email()
