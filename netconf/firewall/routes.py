from flask import render_template, request, Blueprint

firewall = Blueprint('firewall', __name__)

@firewall.route("/firewall")
def info_ip_mx():
    
    return render_template('firewall.html')