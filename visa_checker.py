import requests
import pandas as pd
import streamlit as st
from bs4 import BeautifulSoup

st.set_page_config(page_title='Working visa checker', page_icon='uk')
URL = 'https://www.gov.uk/government/publications/register-of-licensed-sponsors-workers'

if __name__ == '__main__':
    st.title('Working visa checker')
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'lxml')
    download_url = soup.find('span', {'class': 'download'}).find('a')['href']
    user_input = st.text_input('Enter company name:')
    df = pd.read_csv(download_url)
    if user_input:
        st.write(
            f'Last updated {pd.to_datetime(download_url.split("/")[-1][:10], dayfirst=True).strftime("%d %B %Y")}'
        )
        result = pd.DataFrame(columns=df.columns)
        for i in range(len(user_input.split(' '))):
            result = pd.concat([
                result, df[df['Organisation Name'].apply(lambda x: x.lower(
                ).split(' ')).apply(
                    lambda x: user_input.lower().split(' ')[i] in x) == True]
            ])
        st.write(result)