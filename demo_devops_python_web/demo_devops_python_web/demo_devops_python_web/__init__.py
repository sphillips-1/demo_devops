"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

import demo_devops_python_web.views
