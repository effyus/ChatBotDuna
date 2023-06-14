from chatterbot import ChatBot
from difflib import SequenceMatcher

CONFIANCA_MINIMA = 0.50


def comparar_mensagens(mensagem_digitada, mensagem_candidata):
    confianca = 0.0

    digitada = mensagem_digitada.text
    candidata = mensagem_candidata.text
    if digitada and candidata:
        confianca = SequenceMatcher(None, 
            digitada,
            candidata)
        confianca = round(confianca.ratio(), 2)

    return confianca

def iniciar():
    robo = ChatBot("ChatBot Duna",
                   read_only=True,
                   statement_comparison_function=comparar_mensagens,     
                   logic_adapters=[
                       {
                           "import_path": "chatterbot.logic.BestMatch"
                       }
                   ])

    return robo


def executar_robo(robo):
    mensagem = input("ChatBot Duna, seja bem-vindo :)\n")
    while True:
        
        resposta = robo.get_response(mensagem.lower())
        
        if resposta.confidence >= CONFIANCA_MINIMA:
            print(">>", resposta.text)
            
        else:
            print("Desculpe, mas não consegui entender a sua dúvida.","\n Pergunte outra coisa")
            
        mensagem = input()


if __name__ == "__main__":
    robo = iniciar()

    executar_robo(robo)
