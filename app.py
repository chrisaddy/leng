import gradio as gr
import wikipedia
import requests
from google_images_search import GoogleImagesSearch
import os
from scraper_api import ScraperAPIClient


SCRAPER_API_KEY = os.getenv("SCRAPER_API")


def set_lang(lang):
    wikipedia.set_lang("es")
    wikipedia.set_lang("fr")
    wikipedia.set_lang("zh")
    
    print("yo")
    print(lang)


def load_results(query):

    # search = wikipedia.search(query)
    page = wikipedia.page(title=query)

    return page.content


def load_images(query):
    client = ScraperAPIClient('APIKEY')
    url = "https://www.google.com/search?lang=zn&tbm=isch&q=%E5%85%8B"
    result = client.get(url = url).text
    return result


with gr.Blocks() as app:
    language = gr.Radio(["中文", "English", "Español", "日本語"])
    print(dir(language))
    print(language.value)

    language.change(set_lang, language.value)
    
    with gr.Row():
        wiki = gr.Textbox(label="wiki search")
        url = gr.Textbox(label="url")
        plain_text = gr.Textbox(label="text")

    submit = gr.Button("submit").style(full_width=True)


    with gr.Row():
        words = gr.Textbox(label="words")


    with gr.Row():
        output = gr.Textbox(label="output")
        with gr.Row():
            definition = gr.Textbox(label="definition")
            definition_output = gr.Textbox(label="definition")
            define = gr.Button("define")
            # picture = gr.


    submit.click(load_results, wiki, output)
    # define.click(load_definition, )

app.launch()
