#!/usr/bin/env python 
# -*- coding: utf-8 -*-
from flask import Flask,render_template,request
from utils.Checker import Checker
from utils.Helper import Helper
from model.functions import Functions
import threading
import requests
app = Flask(__name__)
feature_count = 30

# NOTES:
# THE API WILL RETURN -1/2/1 -> normal / undetectable / phishing

@app.route("/",methods=["GET"])
def main():
    return render_template("index.html")

@app.route("/api/check",methods=["GET"])
# Params only include url of websites we need to check
def check():
    # return -1/2/1 -> normal / undetectable / phishing

    submit_url = request.args["url"]
    if not Checker.check_connection(submit_url):
        print("Connection unavailable")
        return "2" # unable to detech
        
    if(Checker.Statistical_report(submit_url) == 1):
        return "1"
    try:
        print("Getting info for",submit_url)
        
        input_array = Helper.embed_url(submit_url)
        print(input_array)
        if "2" in input_array:
            # if cannot get some features
            print("Cannot get some features")
            return "2"

        result = Functions.check_vector(input_array)
        
        # this code is used to logged into the database file. Uncomment when needed
        # if (result == 1):
        #     f = open("model/data/urls.csv","a",encoding="UTF-8")
        #     f.write(submit_url+"\n")
        
        return str(result)
    except:
        print("Unable to detech")
        return "2" # unable to detect

# remove cache for development purpose
@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

if __name__ == "__main__":
    app.run(threaded=True,debug=False,ssl_context='adhoc',port=8080)
