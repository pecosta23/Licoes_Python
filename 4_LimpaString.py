import re
entrada = input("\n")

def limpa_string(entrada):
    string_limpa = re.sub(r'[\/()_| ]','', entrada)
    return string_limpa

aaaa = limpa_string(entrada)
print(aaaa)
