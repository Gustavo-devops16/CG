from Services.review_service import get_reviews

def asterisk():
    print("********************************************")

def hello():
    asterisk()
    print("Bem vindo ao Casa Grande")
    print("Gerador de comentários para popular a VTEX")
    print("Você está usando a versão 1.0.0")
    asterisk()
    print("Esse codigo é propriedade intelectual da CSP e da autooria de Gustavo Imparato")

hello()
##Change the param in get_reviews to the vtex seller id you want to generated reviews for 
get_reviews("odelli001") 