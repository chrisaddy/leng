import gradio as gr
import wikipedia
import requests

wikipedia.set_lang("es")
wikipedia.set_lang("fr")
wikipedia.set_lang("zh")


def load_results(query):

    # search = wikipedia.search(query)
    page = wikipedia.page(title=query)

    return page.content


with gr.Blocks() as app:
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

        define = gr.Button("define")


    submit.click(load_results, wiki, output)
    # define.click(load_definition, )

app.launch()
