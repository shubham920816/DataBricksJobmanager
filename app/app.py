from flask import Flask, request, jsonify
from flask_restplus import Resource, Api
import datetime
import os
import utili

import json

app = Flask(__name__)
api = Api(app)



@api.route('/Databricks/clustermanager/create')
class Clustercreation(Resource):
    """
    This class creates the databricks cluster on the fly.
    """

    def post(self):
       """
       Submits the request to create/start the
       databricks cluster
       Returns:

       """
       data=request.json
       pass

    def get(self):
        """
        Gets the current status of the cluster on
        the databricks
        Returns:

        """
        data=request.args
        cluster_name=data.get("cluster_name")
        pass

@api.route('/Databricks/clustermanager/delete')
class Clusterdeletion(Resource):
    """
    This class deletes/stop the currently running databricks cluster
    """
    def post(self):
        """
        Deletes/Stops the currently running databricks cluster
        Returns:
        """
        pass
@api.route('/Databricks/submitjob/')
class Submitjob(Resource):
    """
    This class submits the job on the databricks spark cluster
    using the jobs api
    """
    def post(self):
        """
        Submits the batch job using databricks job api
        Returns:

        """
        pass
@api.route('/Databricks/init_scripts/install')
class Initscriptinstall(Resource):
    """
    This class runs the installs the script action
    on the spark cluster
    """
    def post(self):
        """
        Submits the batch job using databricks job api
        Returns:

        """
        pass
api.route('/Databricks/init_scripts/uninstall')
class Initscriptunistall(Resource):
    """
    This class uninstalls the script action
    on the spark cluster
    """
    def post(self):
        """
        Submits the batch job using databricks job api
        Returns:

        """
        pass

if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0")


