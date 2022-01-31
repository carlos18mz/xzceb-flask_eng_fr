from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench/<param>")
def englishToFrench(param):
    #textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return translator.english_to_french(param)

@app.route("/frenchToEnglish/<param>")
def frenchToEnglish(param):
    #textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return translator.french_to_english(param)

@app.route("/")
def renderIndexPage():
    pass
    # Write the code to render template

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
