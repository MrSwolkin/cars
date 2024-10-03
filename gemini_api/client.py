import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def car_gemeni_bio(modelo, marca, ano):
    model = genai.GenerativeModel('gemeni-1.5-flash')
    response = model.generate_content(
        f'Me mostre uma descrição de venda para o carro {modelo} {marca} {ano} em apenas 250 caracteres. Fale coisas específicas desse modelo. Descreva especificações ténicas desse modelo de carro.',
        max_output_tokens=250)
    print(response.text)
    return response.text
