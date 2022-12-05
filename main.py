from flask import Flask, render_template
from utils import load_candidates_from_json
from utils import get_candidate
from utils import get_candidates_by_name
from utils import get_candidates_by_skill

app = Flask(__name__)


@app.route("/")
def page_candidates():
    candidates = load_candidates_from_json()
    return render_template("list.html", candidates=candidates)


@app.route('/candidates/<int:profile_id>')
def page_profile(profile_id):
    candidate = get_candidate(profile_id)

    return render_template("card.html", candidate=candidate)


@app.route('/search/<candidate_name>')
def page_name_search(candidate_name):
    candidates = get_candidates_by_name(candidate_name)
    len_search = len(candidates)

    return render_template("search.html", candidates=candidates, len_search=len_search)


@app.route('/skill/<skill_name>')
def page_skills(skill_name):
    candidates = get_candidates_by_skill(skill_name)
    len_search = len(candidates)

    return render_template("skill.html", candidates=candidates, len_search=len_search, skill_name=skill_name)


app.run()
