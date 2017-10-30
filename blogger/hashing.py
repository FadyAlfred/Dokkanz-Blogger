import hashlib
import hmac


class Hashing:
    secret = 'asgvsf-sadvbaf.afsgvasf%dsf#F3@&54(fsavf_fbazdfsb+)*FVS'

    def make_secure(self, val):
        secured = [val, hmac.new(self.secret, val).hexdigest()]
        return secured

    def check_secure(self, secured):
        val = secured[0]
        if Hashing().make_secure(val) == secured:
            return val

    def hashPassword(self, email, password):
        email = email.encode('utf-8')
        password = password.encode('utf-8')
        hashed = [hashlib.sha256(email + password).hexdigest()]
        return hashed

    def valiedPassword(self, email, password, hashed):
        return str(hashed) == str(Hashing().hashPassword(email, password))

    def secureCookie(self, val):
        return '%s|%s' % (val, hmac.new(self.secret, val).hexdigest())