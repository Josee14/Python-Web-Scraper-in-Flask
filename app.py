from flask import (
    Flask,
    render_template,
    request,
    redirect,
    flash,
    url_for
)
import urllib.request 
from urllib.parse import urlparse,urljoin
from bs4 import BeautifulSoup
import requests,validators,uuid,pathlib,os

app = Flask(__name__)
app.secret_key = "secret-key"

'''The function checks if the provided tag is an image tag, then extracts the
images' src attribute value and verifies it to see if it's an absolute path.
If else, it joins the relative path to the target's base URL.'''
def image_handler(tag,specific_element,requested_url):
    image_paths = []

    if tag == 'img':
        images = [img['src'] for img in specific_element]
        for i in specific_element:
            image_path = i.attrs['src']
            valid_imgpath = validators.url(image_path)
            if valid_imgpath == True:
                full_path = image_path
            else:
                full_path = urljoin(requested_url, image_path)
                image_paths.append(full_path)

    return image_paths
    

@app.route("/",methods=("GET", "POST"), strict_slashes=False)
def index():
    if request.method == "POST":

        try:
            '''we are writing a function to accept image paths and generate a complete URL from them, 
            the form field inputs must be available globally, so we define them as global variables.'''
            global requested_url,specific_element,tag
           
            #set values to the two global variables from our form fields
            requested_url = request.form.get('urltext')
            tag = request.form.get('specificElement')

            '''We send HTTP request to the user-specified URL - requested_url. The server answers
             the request by delivering the raw HTML content of the webpage, which we then 
             transform to text- .text() and assign to the variable source.'''
            source = requests.get(requested_url).text

            '''Parse the page after we've extracted the HTML content in text format, and we'll 
            utilize html.parser as our parsing library'''
            soup = BeautifulSoup(source, "html.parser")

            '''we navigate through the tree to discover the element we require. The tag that
             the user will enter in the form field'''
            specific_element = soup.find_all(tag)
            
            counter = len(specific_element)

            image_paths = image_handler(
                tag,
                specific_element,
                requested_url
                )
            
            '''pass the results of our parsing along with the return statement to make them
             available on the HTML template.'''
            return render_template("index.html",
                url = requested_url,
                counter=counter,
                image_paths=image_paths,
                results = specific_element
                )

        except Exception as e:
            flash(e, "danger")
            
    return render_template("index.html")


@app.route("/download",methods=("GET", "POST"), strict_slashes=False)
def downloader():
    try:
        for img in image_handler(tag,specific_element,requested_url):
            image_url = img
            
            #The uuid library is used by the download function above to produce unique names for the downloaded files.
            filename = str(uuid.uuid4())
            #strip the image extension from the image path
            file_ext = pathlib.Path(image_url).suffix

            picture_filename = filename + file_ext

            downloads_path = str(pathlib.Path.home() / "Downloads")

            picture_path  = os.path.join(downloads_path, picture_filename)
            
            #actual image download
            urllib.request.urlretrieve(image_url, picture_path)


        flash("Images sucessfully downloaded", "success")

    except Exception as e:
        flash(e, "danger")

    return redirect(url_for('index'))