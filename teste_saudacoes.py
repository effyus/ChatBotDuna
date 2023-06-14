from robo import *
import unittest

class TestSaudacoes(unittest.TestCase):
    def setUp(self):
        self.robo = iniciar()

    def test_01_oi(self):
        saudacoes = [ "oi", "olá", "tudo bem?"]

        for saudacao in saudacoes:
            print(f"Testando saudação: {saudacao}")

            resposta = self.robo.get_response(saudacao.lower())
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Olá. Qual sua dúvida sobre história? :)", 
                resposta.text
            )

    def test_02_bom_dia(self):
        saudacoes = ["bom dia"]

        for saudacao in saudacoes:
            print(f"Testando saudação: {saudacao}")
 
            resposta = self.robo.get_response(saudacao.lower())
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Bom dia. Qual sua dúvida sobre história? :)",
                resposta.text
            )
        
    def test_03_boa_tarde(self):
        saudacoes = ["boa tarde"]

        for saudacao in saudacoes:
                print(f"Testando saudação: {saudacao}")
 
        resposta = self.robo.get_response(saudacao.lower())
        self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
        self.assertIn(
                "Boa tarde. Qual sua dúvida sobre história? :)",
                resposta.text
            )    
            
    def test_04_boa_noite(self):
            saudacoes = ["boa noite"]

            for saudacao in saudacoes:
                print(f"Testando saudação: {saudacao}")
 
            resposta = self.robo.get_response(saudacao.lower())
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Boa noite. Qual sua dúvida sobre história? :)",
                resposta.text
            )


if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TestSaudacoes))

    exec = unittest.TextTestRunner()
    exec.run(testes)