from django.shortcuts import render


def get_html_content(request):
    import requests
    ipc = request.GET.get('ipc')
    ipc = ipc.replace(" ", "+")
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html_content = session.get(f'https://google.com/search?q=definition+of+ipc+section+{ipc}').text
    return html_content


def home(request):
    result = None
    if 'ipc' in request.GET:
        # fetch the ipc from Google.
        html_content = get_html_content(request)
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        # print(soup)
        result = dict()
        # result['name_head'] = soup.find("div", attrs={"class": "qrShPb kno-ecr-pt PZPZlf mfMhoc hNKfZe"}).text
        result['temp_now'] = soup.find("div", attrs={"class": "BNeawe s3v9rd AP7Wnd"}).text
    return render(request, 'core/home.html', {'result': result})
