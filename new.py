from newspaper import Article
import streamlit as st
import openai
from newspaper import Config

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
config = Config()
config.browser_user_agent = user_agent


def Summarize(news_data):
    openai.api_key = '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'
    summarize = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f'Summarize in 30 words "{news_data}"',
        max_tokens=1000,
        temperature=0.7,
    )
    return summarize.choices[0].text

Url=st.text_input('Enter the URL')
if st.button('Summarize'):
    news_data = Article(Url,config=config)
    news_data.download()
    news_data.parse()
    title=news_data.title
    summary=news_data.text
    st.title(title)
    st.image(news_data.top_image, width=500)
    s="".join(summary).replace('\n','')
    summarized=Summarize(s)
    st.write(summarized)
    

