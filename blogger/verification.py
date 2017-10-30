import re


class Verification:
    def nameValied(self, name):
        USER_RE = re.compile(r"^[a-zA-Z0-9\s]{3,20}$")
        return USER_RE.match(name)

    def passwordValied(self, pasword):
        PASS = re.compile("^.{3,20}$")
        return PASS.match(pasword)

    def verfiyPassword(self, pasword, verfiy):
        if pasword == verfiy:
            return True
        else:
            return False

    def emailValied(self, email):
        MAIL = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
        return MAIL.match(email)