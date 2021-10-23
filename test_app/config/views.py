from django.http import HttpResponse


def index(request, *args, **kwargs):
    content = """
    <html>
    <head>
        <title>Django Homepage</title>
    </head>
    <body>
        <h1>안녕</h1>
    </body>
    </html>
    """
    response = HttpResponse(content)
    response.write('<h2>Django Hello<h2>')
    response['Custom-Header'] = 'Custom Header Value'
    return response
