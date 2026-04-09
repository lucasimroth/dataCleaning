import re
import urllib.parse

def pre_processamento_waf(payload):
    if not isinstance(payload, str):
        return ""

    #decodificando URL com double enconding
    text = urllib.parse.unquote(payload)
    text = urllib.parse.unquote(payload)

    #deixando com lower case, vai acontecer que o modelo nao vai ser case sensitive
    payload = text.lower()

    #tirando espaços e quebras de linhas extras no texto
    payload = re.sub(r"[\r\n\t]+", " ", text)

    # Abstração de Entidades
    # Substituindo números por uma tag ajuda o modelo a focar na SINTAXE do ataque e não no valor específico.
    # Ex: 'OR 1=1' e 'OR 5=5' viram 'OR <NUM>=<NUM>'
    text = re.sub(r"\d+", "<NUM>", text)

    #Abstrai strings hexadecimais longas
    text = re.sub(r"0x[0-9a-f]+", "<HEX>", text)

    # Normalização múltiplos espaços para um só
    text = re.sub(r"\s+", " ", text).strip()

    return text
