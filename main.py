import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def get_data(currency):
    df = pd.DataFrame()
    # df = pd.DataFrame(columns = ["r030", "txt", "rate", "cc", "exchangedate"])
    if currency == 'usd':  # записуємо дату та валюту в урл
        url = 'https://bank.gov.ua/NBU_Exchange/exchange_site?start=20210101&end=20211231&valcode=usd&sort=exchangedate&order=desc&json'
    else:
        url = 'https://bank.gov.ua/NBU_Exchange/exchange_site?start=20210101&end=20211231&valcode=eur&sort=exchangedate&order=desc&json'
    # записуємо дані у датафрейм
    data =  pd.read_json(url)
    df = df.append(data, ignore_index=True)
    return df

usd_df = get_data("usd")
eur_df = get_data("eur")
df = pd.concat([usd_df, eur_df], axis=1)
df.to_csv("val_rate.csv")
print("file created!")



