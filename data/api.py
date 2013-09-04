from script import construct_sample_profile
import json

# profile = construct_sample_profile()
# f = open("profile.txt", "w")
# f.write(json.dumps(profile))
# f.close()

# f = open("profile.txt", "r")
# raw_prof = f.readlines()[0]
# # print raw_prof
# prof = json.loads(raw_prof)

#------------------------------------------------------------

def process_profile():

    p = construct_sample_profile()

    repos = p.get('repos')

    overall_lang_distr = {}
    for repo in repos:
        for lang, distr in repo.get('lang_distr').items():
            if lang in overall_lang_distr:
                overall_lang_distr[lang] += distr
            else:
                overall_lang_distr[lang] = distr

    repos_scores = {}
    for index, repo in enumerate(repos):
        
        loc_add = 0
        loc_del = 0
        for commit in repo.get('commits'):
            loc_add += commit.get('add')
            loc_del += commit.get('del')

        repos_scores[index] = loc_add - loc_del/2

        for w_id, w_sc in repo.get('watchers').items():
            repos_scores[index] += w_sc/100.0

        for c_id, c_sc in repo.get('contributors').items():
            repos_scores[index] += c_sc/100.0

        for f_id, f_sc in repo.get('forkers').items():
            repos_scores[index] += f_sc/100.0

    return repos_scores, overall_lang_distr




def lang_distr_pie(raw_lang_dic):

    total_loc = sum([int(v) for (k,v) in raw_lang_dic.items()])
    distr     = []
    for k,v in raw_lang_dic.items():
        perc = v*100.0/total_loc
        distr.append([k, perc])

    return distr

# print lang_distr_pie(proces_profile()[1])
