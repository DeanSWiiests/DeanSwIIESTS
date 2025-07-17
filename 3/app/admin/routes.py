from flask import Blueprint, render_template
from flask_login import login_required, current_user
from ..decorators import admin_required

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/")
@login_required
@admin_required
def dashboard():
    return render_template("admin/dashboard.html")