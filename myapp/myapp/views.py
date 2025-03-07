from django.http import HttpResponse
import os
import datetime
import subprocess

def htop_view(request):
    name = "Sample name"
    username = os.getenv("USER", "unknown")  
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    top_output = subprocess.getoutput("top -b -n 1 | head -10")

    response = f"""
    <html>
    <head><title>/htop</title></head>
    <body>
        <h2>Name: {name}</h2>
        <h2>Username: {username}</h2>
        <h2>Server Time (IST): {ist_time.strftime('%Y-%m-%d %H:%M:%S')}</h2>
        <pre>{top_output}</pre>
    </body>
    </html>
    """
    return HttpResponse(response)
