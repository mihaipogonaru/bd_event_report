"""Helper utilities and decorators."""
from functools import wraps

from flask import flash, redirect, url_for, abort
from flask_login import current_user

def logout_required(view):
    @wraps(view)
    def decorated_view(*args, **kwargs):
        if current_user.is_authenticated:
            return redirect(url_for('manage.manage_index'))
        return view(*args, **kwargs)
    return decorated_view

def flash_errors(form, category="warning"):
    """Flash all errors for a form."""
    for field, errors in form.errors.items():
        for error in errors:
            flash("{0} - {1}"
                  .format(getattr(form, field).label.text, error), category)
