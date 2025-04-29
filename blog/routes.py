import os
import time
from datetime import datetime
from flask import Blueprint, render_template, url_for, redirect, abort

home = Blueprint('home', __name__, template_folder='templates')


def read_metadata(folder):

    # Check that the metadata file exists
    path = f"{folder}/metadata.txt"
    if not os.path.isfile(path):
        abort(404)

    # Read the metadata file
    metadata = {}
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            (key, val) = line.split(";")
            metadata[key.strip()] = val.strip()

    return metadata


def generate_index():

    # List all directories
    path = "blog/templates"
    pages = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

    # Get the metadata for each directory
    data = []
    for page in pages:
        metadata = read_metadata(f"{path}/{page}")
        metadata["endpoint"] = page
        data.append(metadata)

    # Sort data by date created
    return sorted(data, key=lambda x: x["created"], reverse=True)


# Redirect root to home
@home.route('/')
def root():
    return redirect(url_for('home.page', title="home"))


# General endpoint for serving pages
@home.route('/<title>')
def page(title):

    # Get the folder path
    folder = f"blog/templates/{title}"

    # Check that the post exists
    post_path = f"{folder}/post.html"
    if not os.path.isfile(post_path):
        abort(404)

    # Read the HTML post file
    with open(post_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Get the timestamp of the last modification
    time_modified = datetime.fromtimestamp(os.path.getmtime(post_path))
    date_modified = time_modified.strftime("%Y/%m/%d")

    # Get the metadata for the file and render the endpoint
    metadata = read_metadata(folder)
    metadata["modified"] = date_modified

    # Get data for the index table (if necessary)
    index = []
    if title == "index":
        index = generate_index()

    return render_template('base.html', content=content, metadata=metadata, index=index)




