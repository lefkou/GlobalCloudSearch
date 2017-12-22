from flask import Flask, render_template, request
import dropbox

app = Flask(__name__)

app_key = ''
app_secret = ''
access_token = ''

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
