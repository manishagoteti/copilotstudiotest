"""
Purpose: Setting up a Flask web application with RESTful API endpoints to interact with Azure Blob Storage and add metadata.

Imports:
- Flask - For building web applications.
- request - Used to handle HTTP requests.
- Resource - Helps in creating RESTful APIs by defining resources.
- Api - Adds RESTful support to the Flask application.
- Constants - imported from Constants.py for accessing constant values used across the application.

"""

from flask import Flask
from flask_restful import Api, Resource, reqparse
import blobaddmetadata
from config import DefaultConfig
import http
import requests
import CpalExcludeUrls


# Initialize a Flask application and RESTful API
app = Flask(__name__)
api = Api(app)
CONFIG = DefaultConfig()

# Create a parser instance
parser = reqparse.RequestParser()
parser.add_argument('ExcludeUrl', type=str, required=True, help='Exluded urls')

class metadatacreation(Resource):
    def get(self):
        blobdata = blobaddmetadata.addmedatatoblob()
        print("completed")
        return blobdata


class CPalExcludeUrl(Resource):
    def get(self):
        CPalExUrl = CpalExcludeUrls.CpalGetExURL()
        return CPalExUrl 


api.add_resource(metadatacreation, '/api/cpablobmetadata')
api.add_resource(CPalExcludeUrl, '/api/cpapalexcludeurl')

if __name__ == '__main__':
    app.run(host='127.0.0.1',debug=True, port=9311, threaded=True, use_reloader=False)













# url = DefaultConfig.rest_
# header = DefaultConfig.header
# auth = DefaultConfig.token
# uploadDocData = requests.get(url, headers=header, auth=auth)
