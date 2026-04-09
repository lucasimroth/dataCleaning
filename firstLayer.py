#firstLayer remove as primeiras partes da limpeza de dados

import pandas as pd
import matplotlib.pyplot as plt
import re
import preProcessamentoWaf

def continuar():
    print("pressione Enter para continuar ou Ctrl+C para sair...")
    while True:
        try:
            input()
            break
        except KeyboardInterrupt:
            print("\nSaindo...")
            exit()



df = pd.read_csv("C:/Users/lucas/Documents/TCC/treinamento/datasets/raw/sqli_data/sqli.csv", encoding='utf-16')

print("colunas:")
print(df.shape)

print("\n\ndistribuição das classes:")
print(df["Label"].value_counts())  # Distribuição das classes
print("\n\nonde tem nulos:")
print(df.isnull().sum())           # Valores nulos

print("primeiras linhas maliciosas exemplo:")
linhas_class_1 = df[df['Label'] == 1]
print(linhas_class_1.head(5))

print("Parte da limpeza, duplicatas, nulos e label 1 com menos de 2 caracteres")
continuar()

df.dropna(inplace=True)  # Remove linhas com valores nulos
df.drop_duplicates(inplace=True)  # Remove linhas duplicadas
df.drop(df[df['Sentence'].str.len() < 2 & df["Label"] == 1].index, inplace=True)  #remove linhas menores que 2 da label 1

print("normalização dos payloads")
continuar()

df['Sentence'] = df['Sentence'].apply(preProcessamentoWaf.pre_processamento_waf)




#Normal,GET,Mozilla/5.0 (compatible	 Konqueror/3.5	 Linux) KHTML/3.5.8 (like Gecko),no-cache,no-cache,"text/xml,application/xml,application/xhtml+xml,text/html	q=0.9,text/plain	q=0.8,image/png,*/*	q=0.5","x-gzip, x-deflate, gzip, deflate","utf-8, utf-8	q=0.5, *	q=0.5",en,localhost:8080,JSESSIONID=1F767F17239C9B670A39E9B10C3825F4,,close,,,0,http://localhost:8080/tienda1/index.jsp HTTP/1.1
