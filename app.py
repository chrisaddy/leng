import gradio as gr
import wikipedia
import requests
import os
from scraper_api import ScraperAPIClient
import emoji


SCRAPER_API_KEY = os.getenv("SCRAPER_API_KEY")



def load_results_chinese(query):

    wikipedia.set_lang("zh")
    # search = wikipedia.search(query)
    page = wikipedia.page(title=query)

    return page.content


def load_results_spanish(query):

    wikipedia.set_lang("es")
    # search = wikipedia.search(query)
    page = wikipedia.page(title=query)

    return page.content


def load_results_french(query):
    wikipedia.set_lang("fr")

    # search = wikipedia.search(query)
    page = wikipedia.page(title=query)

    return page.content



def load_results_japanese(query):

    # search = wikipedia.search(query)
    page = wikipedia.page(title=query)

    return page.content


def load_definition(query):
    client = ScraperAPIClient(SCRAPER_API_KEY)
    url = f"https://www.google.com/search?lang=es&tbm=isch&q={query}"
    result = client.get(url = url)
    print(result.json())
    return result




with gr.Blocks() as app:
    with gr.Row():
        wiki = gr.Textbox(label="wiki search")
        url = gr.Textbox(label="url")
        plain_text = gr.Textbox(label="text")

    with gr.Row():
        submit_chinese = gr.Button(emoji.emojize(":China:")).style(full_width=True)
        submit_spanish = gr.Button(emoji.emojize(":Mexico:")).style(full_width=True)
        submit_french = gr.Button(emoji.emojize(":France:")).style(full_width=True)
        submit_japanese = gr.Button(emoji.emojize(":Japan:")).style(full_width=True)


    with gr.Row():
        words = gr.Textbox(label="words")


    with gr.Row():
        output = gr.Textbox(label="output")
        with gr.Row():
            definition = gr.Textbox(label="definition")
            definition_output = gr.Textbox(label="definition")
            define = gr.Button("define")
            # picture = gr.


    submit_spanish.click(load_results_spanish, wiki, output)
    submit_chinese.click(load_results_chinese, wiki, output)
    submit_french.click(load_results_french, wiki, output)
    submit_japanese.click(load_results_japanese, wiki, output)

    define.click(load_definition, definition)

app.launch()
