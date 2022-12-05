import json

def load_candidates_from_json():
    with open("candidates.json", "r", encoding="utf-8") as file:
        candidates = json.load(file)

    return candidates


def get_candidate(candidate_id):
    candidates = load_candidates_from_json()
    for candidate in candidates:
        if candidate['id'] == candidate_id:
            return candidate



def get_candidates_by_name(candidate_name):
    needed_candidates = []
    candidates = load_candidates_from_json()
    for candidate in candidates:
        if candidate_name.lower() in candidate['name'].lower():
            needed_candidates.append(candidate)


    return needed_candidates


def get_candidates_by_skill(skill_name):
    needed_candidates = []
    candidates = load_candidates_from_json()
    for candidate in candidates:
        if skill_name.lower() in candidate['skills'].lower():
            needed_candidates.append(candidate)


    return needed_candidates
exp = get_candidate(1)
print(exp)