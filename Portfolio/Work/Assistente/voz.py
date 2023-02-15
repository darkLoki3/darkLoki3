# | fim da tarefa ||IA-10 do jira}}
import RPi.GPIO
import internet
import pandas as pd
import pyttsx3
import speech_recognition as sr
import sockets
from keyboard import is_pressed
import vosk

# from Assistente.rosto.rosto import Window
# from Assistente.sensor import sensor

# configuração da voz e driver usado
@teste
def config():
    engine = pyttsx3.init('sapi5')

    pt_br_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\Ricardo RSI Harpo 22kHz"
    # configuração da voz masculina
    engine.setProperty('voice', pt_br_voice_id)
    # configuração do volume do microfone
    engine.setProperty('volume', 1.)
    # configuração da velocidade da fala
    engine.setProperty('rate', 140)
    # Arruma a configuração desejada
    engine.runAndWait()

@teste
def fala(audio):
    if is_pressed("q"):
        raise SystemExit
    else:
        engine.say(audio)
        engine.runAndWait()

@teste
def get_audio():
    """get_audio():
    Returns:
        Retorna o audio dito no microfone"""
    if is_pressed("q"):
        raise SystemExit
    else:
        r = sr.Recognizer()
        mic = sr.Microphone()
        winsound.Beep(440, 500)
        with mic as source:
            # engine.say("Estou ouvindo")
            # engine.runAndWait()
            r.adjust_for_ambient_noise(source, duration = 0.5)
            audio = r.listen(source, timeout = 9, phrase_time_limit = 0.9)
            try:
                escuta = r.recognize_google(audio, language = 'pt-BR')
                data = escuta.lower()
            except sr.UnknownValueError:
                fala("Não entendi, pode repetir?")
                get_audio()
            else:
                return data

@teste
def main():
    # principal
    if is_pressed("q"):
        raise SystemExit
    else:
        df = pd.DataFrame(
            {
                'nomes': ["Miguel", "Davi", "Gabriel", "Arthur", "Lucas", "Matheus", "Pedro", "Guilherme", "Gustavo",
                          "Rafael",
                          "Felipe", "Bernardo", "Enzo", "Nicolas", "João Pedro", "Pedro Henrique", "Cauã", "Vitor",
                          "Eduardo",
                          "Daniel", "Henrique", "Murilo", "Vinicius", "Samuel", "Pietro", "João Vitor", "Leonardo",
                          "Caio",
                          "Heitor", "Lorenzo", "Isaac", "Lucca", "Thiago", "João Gabriel", "João", "Theo", "Bruno",
                          "Bryan",
                          "Carlos Eduardo", "Luiz Felipe", "Breno", "Emanuel", "Ryan", "Vitor Hugo", "Yuri", "Benjamin",
                          "Erick", "Enzo Gabriel", "Fernando", "Joaquim", "André", "Tomás", "Francisco", "Rodrigo",
                          "Igor",
                          "Antonio", "Ian", "Luiz Otávio", "Juan", "João Guilherme", "Diogo", "Otávio", "Nathan",
                          "Calebe",
                          "Danilo", "Luan", "Luiz Henrique", "Kaique", "Alexandre", "João Miguel", "Iago", "Ricardo",
                          "Raul",
                          "Marcelo", "Julio César", "Cauê", "Benício", "Vitor Gabriel", "Augusto", "Pedro Lucas",
                          "Luiz Gustavo", "Giovanni", "Renato", "Diego", "João Paulo", "Renan", "Luiz Fernando",
                          "Anthony",
                          "Lucas Gabriel", "Thales", "Luiz Miguel", "Henry", "Marcos Vinicius", "Kevin", "Levi",
                          "Enrico",
                          "João Lucas", "Hugo", "Luiz Guilherme", "Matheus Henrique", "Julia", "Sophia", "Isabella",
                          "Maria Eduarda", "Manuela", "Giovanna", "Alice", "Laura", "Luiza", "Beatriz", "Mariana",
                          "Yasmin",
                          "Gabriela", "Rafaela", "Maria Clara", "Maria Luiza", "Ana Clara", "Isabelle", "Lara",
                          "Ana Luiza",
                          "Letícia", "Ana Julia", "Valentina", "Nicole", "Sarah", "Vitória", "Isadora", "Lívia",
                          "Helena",
                          "Ana Beatriz", "Lorena", "Clara", "Larissa", "Emanuelly", "Heloisa", "Marina", "Melissa",
                          "Gabrielly",
                          "Eduarda", "Maria Fernanda", "Rebeca", "Amanda", "Alícia", "Bianca", "Lavínia", "Fernanda",
                          "Ester",
                          "Carolina", "Emily", "Cecília", "Maria Júlia", "Pietra", "Ana Carolina", "Milena", "Marcela",
                          "Laís",
                          "Natália", "Maria", "Bruna", "Camila", "Luana", "Ana Laura", "Catarina", "Maria Vitória",
                          "Maria Alice", "Olivia", "Agatha", "Mirella", "Sophie", "Stella", "Stefany", "Isabel",
                          "Kamilly",
                          "Elisa", "Luna", "Eloá", "Joana", "Mariane", "Bárbara", "Juliana", "Rayssa", "Alana",
                          "Ana Sophia",
                          "Ana Lívia", "Caroline", "Brenda", "Evelyn", "Débora", "Raquel", "Maitê", "Ana", "Nina",
                          "Maria Sophia", "Maria Cecília", "Luiz", "Antonella", "Jennifer", "Betina", "Mariah",
                          "Sabrina",
                          "Maurício", "Antenor", "Juliano", "Sérgio", "Fábio", "Sílvio", "Kléber", "José", "César",
                          "Romeu",
                          "Mário", "Álvaro", "Reginaldo", "Manoel", "Marcos", "Cristiano", "Hugo", "Mário", "Arnoldo",
                          "Benedito", "Elísio", "Neto", "Augusto", "Romeu", "Edgar", "Cauê", "Émerson", "Roberto",
                          "Mateus",
                          "Erasmo", "Geraldo", "Amélia", "Estela", "Elza", "Inês", "Vanuza", "Shirlei", "Roberta",
                          "Letícia",
                          "Valéria", "Valentina", "Nicole", "Juliana", "Tânia", "Miriam", "Clarice", "Leila", "Suzana",
                          "Luciana", "Inês", "Jaqueline", "Lívia", "Cláudia", "Elza", "Priscila", "Arlene", "Roberta",
                          "Marli",
                          "Sônia", "Rita", "Zilda", "Maiara", "Eduarda", "Poliane", "Marina", "Emília", "Bárbara",
                          "Poliana",
                          "Isadora", "Nina", "Lavínia", "Luana", "Lorena", "Larissa", "Fernanda", "Sônia", "Shirlei",
                          "Liana",
                          "Carlos", "Mariana Castro", "Lara da Costa", "João Guilherme da Costa", "Lorena Peixoto",
                          "Fernanda Moreira", "Evelyn Correia", "Gabrielly Peixoto", "Julia Oliveira",
                          "Evelyn Oliveira",
                          "Alana Moreira", "Lucas Cardoso", "Felipe Barbosa", "Davi Lucas da Rosa", "Nicole Novaes",
                          "Breno Moreira", "Carlos Eduardo Barbosa", "Fernando Cavalcanti", "Bruna Cardoso",
                          "Maria Lima",
                          "Maria Vitória Martins", "Luiz Fernando Costa", "Agatha Azevedo", "Helena Freitas",
                          "Antônio Nascimento", "Lucas Gabriel Barros", "Juliana Fogaça", "Pietro Alves",
                          "Isabelly Teixeira",
                          "Luigi Fernandes", "Clarice Fernandes", "Pedro Teixeira", "Ana Julia Fernandes",
                          "Sofia Sales",
                          "André Nunes", "Daniela Cardoso", "Heloísa Ramos", "Miguel Fogaça", "Luiz Felipe Lima",
                          "Catarina Gonçalves", "Bruno Caldeira", "Mariana da Luz", "Nathan da Luz",
                          "João Felipe da Conceição",
                          "Nicole Melo", "Eduardo Gomes", "Murilo Cardoso", "Nathan Cardoso", "Luiz Otávio Caldeira",
                          "Heloísa Silva", "Igor Carvalho", "Arthur Rocha", "Kaique da Rocha", "Larissa da Mota",
                          "Enzo Costa",
                          "Larissa da Mata", "Miguel Lima", "Maria Eduarda Barbosa", "Enzo Gabriel Dias",
                          "Antônio Melo",
                          "Melissa Almeida", "Matheus Nogueira", "Davi Lucca das Neves", "Vinicius Rocha",
                          "Luiz Fernando Castro", "Felipe Campos", "Bianca Barbosa", "Arthur Sales", "Antônio Campos",
                          "Luna da Luz", "Thales Barbosa", "Maria Sophia Araújo", "Marcos Vinicius Souza",
                          "Thales Monteiro",
                          "Nina Duarte", "Letícia Carvalho", "Yuri Sales", "Rebeca Azevedo", "Fernando Pires",
                          "Rafael Santos",
                          "Stephany Moreira", "Stephany Melo", "Natália Moreira", "João Guilherme da Rosa",
                          "Ana Julia Nunes",
                          "Vitor Costa", "Luiz Henrique Souza", "Larissa Cardoso", "Emanuelly Dias", "Laís Moreira",
                          "Giovanna Fogaça", "Fernando Moreira", "Lorenzo Santos", "Matheus Mendes", "Isadora Barros",
                          "Otávio Aragão", "Letícia Novaes", "Joaquim Araújo", "Marina Barros", "Paulo Freitas",
                          "Carolina Pinto", "Esther Porto", "Fernanda da Luz", "Caio Rodrigues", "Caroline Campos",
                          "Beatriz Farias", "Maria Julia Viana", "Maria Alice da Mota", "Marcelo da Costa",
                          "Igor Oliveira",
                          "Bruno das Neves", "Maria Luiza Martins", "Gabriela das Neves", "Luana Lopes",
                          "Heitor Farias",
                          "Cauê Souza", "João Miguel Oliveira", "Mariane Lima", "Lorena Monteiro",
                          "Maria Cecília Farias",
                          "Igor Rocha", "Diogo Pinto", "Isaac Moura", "Benício Oliveira", "João Felipe Almeida",
                          "Larissa Silveira", "Vicente Ferreira", "Lucas Souza", "Isadora Martins", "Sofia da Luz",
                          "Vitor Gomes", "Lucca Jesus", "Fernando Porto", "Davi Lucca Carvalho", "Lucas Souza",
                          "Eduardo Castro", "João Gabriel Pires", "Heloísa Moreira", "Ryan Campos",
                          "Luiz Otávio Martins",
                          "João Felipe Carvalho", "Gabriel da Luz", "Natália Costela", "Ana Júlia Aragão",
                          "Thales Carvalho",
                          "Vitor Gabriel Duarte", "Valentina da Paz", "Leonardo Cardoso", "Emanuella da Mota",
                          "Henrique Moraes", "Eduardo Barros", "Manuela Barros", "Agatha Nascimento",
                          "Maria Vitória Fogaça",
                          "Valentina da Conceição", "Ryan da Costa", "Igor Correia", "Laura da Mata", "Nina Novaes",
                          "João Lucas Moura", "Maitê Moreira", "Nicolas Porto", "Milena Duarte", "Paulo Cardoso",
                          "Luiz Otávio Nogueira", "Luna Pereira", "Larissa Cardoso", "Thales Oliveira",
                          "Gustavo Henrique Azevedo", "Calebe Vieira", "Giovanna da Costa", "Lucas Gabriel Porto",
                          "Olivia Pereira", "Yasmin Cunha", "Maria Aragão", "Letícia Barbosa", "Kevin Carvalho",
                          "Bernardo Cardoso", "Vitor Pires", "Bernardo da Mota", "Amanda Melo", "Marina Monteiro",
                          "Sophie da Costa", "Lucas Gabriel Araújo", "João Lucas Moura", "Eduarda Jesus",
                          "Marcela Cavalcanti",
                          "Marina Ferreira", "Francisco Oliveira", "Marcelo Jesus", "Maria Luiza da Paz",
                          "Guilherme Costa",
                          "Pedro Henrique Cardoso", "Juliana Fogaça", "João Gabriel Novaes", "Lara Mendes",
                          "Pietro Teixeira",
                          "Helena Campos", "Vitor Hugo Souza", "Nicole Cardoso", "Bernardo Dias", "Luna Campos",
                          "Abigail",
                          "Rodinei", "Tetsuo", "Adriana", "Alexandra", "Soldi", "Valdir"],
            })
        df['nomes'] = df['nomes'].str.lower()
        df2 = pd.DataFrame(
            {
                'idade': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17',
                          '18',
                          '19', '20', '21',
                          '22',
                          '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37',
                          '38',
                          '39', '40', '41',
                          '42',
                          '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57',
                          '58',
                          '59', '60', '61',
                          '62',
                          '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77',
                          '78',
                          '79', '80', '81',
                          '82',
                          '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97',
                          '98',
                          '99']
            })
        fala("Oi, eu sou o Doutor Kids, fui criado para te ajudar a escolher a palmilha ideal para seu pezinho")
        fala("Diga o seu nome?")
        frase = get_audio()
        print(frase)

        while True:
            if frase == 0:
                continue
            if str(frase) in df.values:
                fala("Quantos anos você tem?")
                frase = get_audio()
                print(frase)
                continue
            if str(frase) in df2.values:
                fala("Você quer fazer uma experiência comigo?")
                fala("Diga Sim ou Não.")
                frase = get_audio()
                print(frase)
                continue
            if 'sim' in str(frase):
                fala("Então vamos lá,")
                fala("ande naturalmente sobre o tapete iluminado que está ao lado,")
                fala("seguindo as instruções do nosso pessoal.")
                fala("Obrigado pela participação.")
                fala("A kids está sempre preocupada em desenvolver o melhor calçado para as crianças")
                break
            if 'não' in str(frase):
                fala("Aaaaahh... que pena, fica para próxima então!")
                fala("Obrigado.")
                fala("A kids está sempre preocupada em desenvolver o melhor calçado para as crianças.")
                break
