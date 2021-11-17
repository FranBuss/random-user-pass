import string

# Se crea una clase que va a llamar a la generacion de distintos caracteres
class CharGenerator:

    def all_characters(self):
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        num = string.digits
        symbols = string.punctuation
        all = lower + upper + num + symbols
        return all

    def letters(self):
        upper = string.ascii_uppercase
        lower = string.ascii_lowercase
        all = lower + upper
        return all

    # Los mails se me hicieron bonitos
    def email(self):
        emails  = ("@gmail.com", "@hotmail.com", "@yahoo.com")
        return emails