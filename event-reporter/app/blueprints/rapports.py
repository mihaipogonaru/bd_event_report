from flask import Blueprint, flash, render_template, request, redirect, url_for

from app.database import Database as db


blueprint = Blueprint("rapports", __name__, url_prefix='/rapports')


@blueprint.route("/", methods=['get'])
def rapports_index():
    counties = db.get_counties()

    births = {}
    deaths = {}

    total_b = 0
    total_d = 0

    for county in counties:
        name = county['name']

        births[name] = len(db.get_births_in_county(name))
        deaths[name] = len(db.get_deaths_in_county(name))

        total_b += births[name]
        total_d += deaths[name]

    return render_template('rapports/index.html',
                           counties=counties, births=births, deaths=deaths,
                           total_b=total_b, total_d=total_d)
