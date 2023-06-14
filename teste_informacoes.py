from robo import *
import unittest

class TestInformacoes(unittest.TestCase):
    def setUp(self):
        self.robo = iniciar()

    def test_01_o_que_e_guerra(self):
        perguntas = ["O que é uma guerra?", "o que é uma guerra?", "O que é guerra?"]

        for pergunta in perguntas:
            print(f"Testando pergunta: {pergunta}")

            resposta = self.robo.get_response(pergunta.lower())
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "É um conflito armado entre duas ou mais partes que envolve o uso da violência e das forças militares para atingir objetivos específicos. Durante uma guerra, as partes envolvidas lutam entre si com o objetivo de derrotar o oponente, seja em termos territoriais, ideológicos, políticos ou outros.", 
                resposta.text
            )

    def test_02_objetivo_guerra(self):
        perguntas = [
            "Qual o objetivo de uma guerra?", "Qual o objetivo?"
        ]

        for pergunta in perguntas:
            print(f"Testando pergunta: {pergunta}")

            resposta = self.robo.get_response(pergunta.lower())
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "O objetivo de uma guerra é prevalecer sobre o oponente e alcançar a vitória. Isso pode significar defender interesses, conquistar território, impor ideologias ou obter recursos. No entanto, é importante destacar que a guerra é uma forma extrema de conflito que envolve consequências graves e humanas, e a resolução pacífica de disputas é sempre preferível.",
                resposta.text
            )
    
    def test_03_tipo_guerra(self):
        perguntas = [
            "Quais são os tipos de guerra?", "Quais os tipos?"
        ]

        for pergunta in perguntas:
            print(f"Testando pergunta: {pergunta}")

            resposta = self.robo.get_response(pergunta.lower())
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
              "Guerra com armamento usual; Guerra psicológica; Guerra econômica; Guerra radiológica, nuclear ou radioativa; Guerra biológica, bacteriológica ou virótica; Guerra cibernética, eletrônica ou informática; Guerra química.",
                resposta.text
            )

    def test_04_piores_guerras(self):
        perguntas = [
           "Quais foram as piores guerras?", "Quais as piores?"
        ]

        for pergunta in perguntas:
            print(f"Testando pergunta: {pergunta}")

            resposta = self.robo.get_response(pergunta.lower())
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "1°- Segunda Guerra mundial(1939-1945): Causou a morte de 60 a 70 milhões de pessoas. 2°- Primeira Guerra Mundial(1914-1918): Causou a morte de 15 a 20 milhões de pessoas. 3°- Segunda Guerra Sino-Japonesa(1937-1945): Causou a morte de cerca de 20 milhões de pessoas. 4°- Guerra dos Trinta Anos(1618-1648): Causou a morte de 5 a 8 milhões de pessoas. Guerra dos Cem Anos(1337-1453): Causou a morte de 5 a 8 milhões de pessoas.",
                resposta.text
            )

    def test_05_brasil(self):
        perguntas = [
            "Houve conflito no Brasil?"
        ]

        for pergunta in perguntas:
            print(f"Testando pergunta: {pergunta}")

            resposta = self.robo.get_response(pergunta.lower())
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
              "Sim, a Guerra do Paraguai foi o maior conflito armado internacional ocorrido na América Latina. Foi travada entre o Paraguai e a Tríplice Aliança, composta pelo Império do Brasil, Argentina e Uruguai. Ela se estendeu de dezembro de 1864 a março de 1870.",
                resposta.text
            )
      
if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TestInformacoes))

    exec = unittest.TextTestRunner()
    exec.run(testes)