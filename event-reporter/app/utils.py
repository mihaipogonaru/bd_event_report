"""Helper utilities and decorators."""
from functools import wraps

from flask import flash, redirect
from flask_login import current_user
from app.extensions import login_manager


def admin_required(view):
    @wraps(view)
    def decorated_view(*args, **kwargs):
        if not current_user.is_admin():
            return login_manager.unauthorized()
        return view(*args, **kwargs)
    return decorated_view


def flash_errors(form, category="warning"):
    """Flash all errors for a form."""
    for field, errors in form.errors.items():
        for error in errors:
            flash("{0} - {1}"
                  .format(getattr(form, field).label.text, error), category)
