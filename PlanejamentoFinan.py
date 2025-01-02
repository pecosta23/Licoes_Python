import pandas as pd

#colunas
data = {
    "Data": [],
    "Descrição": [],
    "Valor (R$)": [],
    "Parcelas (nº atual / total)": [],
    "Categoria": [],
    "Observações": []
}

#cria dataframe
df = pd.DataFrame(data)

#salva como xlsx
file_path = "/mnt/data/Planejamento_Financeiro.xlsx"
df.to_excel(file_path, index=False)

file_path