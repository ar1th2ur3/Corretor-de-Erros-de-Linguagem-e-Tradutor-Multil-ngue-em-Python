import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from googletrans import Translator

# Função para corrigir erros de linguagem
def corrigir_erros(frase):
    # Tokenize a frase em palavras
    palavras = word_tokenize(frase, language='portuguese')
    
    # Inicializa o lematizador do WordNet
    lemmatizer = WordNetLemmatizer()
    
    # Corrige os erros de linguagem usando a lematização do WordNet
    palavras_corrigidas = [lemmatizer.lemmatize(palavra) for palavra in palavras]
    
    # Reconstroi a frase corrigida
    frase_corrigida = ' '.join(palavras_corrigidas)
    
    return frase_corrigida

# Função para traduzir para espanhol e inglês
def traduzir(frase):
    translator = Translator()
    
    # Traduz para espanhol
    frase_espanhol = translator.translate(frase, src='pt', dest='es').text
    
    # Traduz para inglês
    frase_ingles = translator.translate(frase, src='pt', dest='en').text
    
    return frase_espanhol, frase_ingles

# Entrada do usuário
frase = input("Digite uma frase em português: ")

# Corrige erros de linguagem
frase_corrigida = corrigir_erros(frase)

# Traduz para espanhol e inglês
frase_espanhol, frase_ingles = traduzir(frase_corrigida)

# Exibe os resultados
print("Frase corrigida:", frase_corrigida)
print("Tradução para Espanhol:", frase_espanhol)
print("Tradução para Inglês:", frase_ingles)
