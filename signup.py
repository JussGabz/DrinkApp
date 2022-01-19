users = {}

class SignUp:
    def __init__(self, username, fname, lname, email, password):
        self.username = username
        self.fname = fname
        self.lname = lname
        self.email = email
        self.password = password

    def registerUser(self):
        users["username"] = self.username
        users["firstName"] = self.fname
        users["lname"] = self.lname
        users["email"] = self.email
        users["password"] = self.password


Gabriel = SignUp(
    "JussGabz", "Gabriel", "Ifesanya", "gi@hotmail.com", "pass123"
)

print(users)
Gabriel.registerUser()
print(users)
