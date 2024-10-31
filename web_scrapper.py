import requests
from readability import Document

# URL of the web page you want to retrieve
def get_url_content(url) -> str:
    # Sending a GET request to the URL
    try:
        response = requests.get(url)
        response.encoding = response.apparent_encoding

        # Check if the request was successful (status code 200)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Use readability to parse and get the main content
        doc = Document(response.text)
        main_content = doc.summary()

        return main_content

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
