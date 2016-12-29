from flask import Flask, render_template, request
import dropbox

app = Flask(__name__)

app_key = '7l8ffoj7zzz8p1j'
app_secret = '8w15ijlf5037y6u'
access_token = '4K6vAJC9MA4AAAAAAAACAO77hjgpiwlHMCqyWJ0mxwZvjKaiUu7nq7sg0A76gwT3'

flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)

@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/search", methods = ["POST"])
def search():
    authorize_url = flow.start()
    client = dropbox.client.DropboxClient(access_token)
    file_name = request.form['search-input']
    data =  client.search("", file_name, file_limit=1000, include_deleted=False)
    return render_template("results.html", data = data)
