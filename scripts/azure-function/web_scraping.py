import logging
import azure.functions as func
import requests
from bs4 import BeautifulSoup

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="rebrickable")
def rebrickable(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    url = "https://rebrickable.com/downloads/"
    try:
        # Realizar la solicitud HTTP
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción si la solicitud no fue exitosa
        html_content = response.text

        # Parsear el contenido HTML
        soup = BeautifulSoup(html_content, "html.parser")
        enlaces = soup.find_all('a')
        enlaces_descarga = [enlace['href'] for enlace in enlaces if '.gz' in enlace.get('href', '')]

        # Devolver los enlaces como respuesta
        return func.HttpResponse(str(enlaces_descarga), status_code=200)
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)
