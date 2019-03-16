# Launch with
#
# gunicorn -D --threads 4 -b 0.0.0.0:5000 --access-logfile server.log --timeout 60 server:app glove.6B.300d.txt bbc

from flask import Flask, render_template
from doc2vec import *
import sys

app = Flask(__name__)

@app.route("/")
def articles():
    """Show a list of article titles"""
    return render_template('articles.html',list=articles[1:])


@app.route("/article/<topic>/<filename>")
def article(topic,filename):
    """
    Show an article with relative path filename. Assumes the BBC structure of
    topic/filename.txt so our URLs follow that.
    """
    file_name=topic+'/'+filename
    index=[w[0] for w in articles].index(file_name)
    article=articles[index]
    reco = recommended(article, articles, 5)
    return  render_template('article.html',article=article,reco=reco)

# initialization
i = sys.argv.index('server:app')
glove_filename = sys.argv[i+1]
articles_dirname = sys.argv[i+2]

#glove_filename = "/home/jyoti/MSDS/Course data MSDS692/msds692/data/glove.6B/glove.6B.300d.txt"
#articles_dirname = "/home/jyoti/MSDS/Course data MSDS692/msds692/data/bbc"

gloves = load_glove(glove_filename)
articles = load_articles(articles_dirname, gloves)

#app.run()
