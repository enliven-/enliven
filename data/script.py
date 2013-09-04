from sample_profile import prof as profile
from random import randint, randrange, choice
from datetime import datetime, timedelta


def construct_sample_profile():
    
    prof = {}

    prof['repos_count']     = randint(1, 5)
    prof['followers_count'] = randint(1, 5)
    prof['prof_created_at'] = random_date('1/1/2005 1:30 PM', '7/1/2013 4:50 AM')

    followers = {}
    for x in range(prof['followers_count']):
        follower_id = randint(1, 5000)
        follower_sc = randint(1, 1000)
        followers[follower_id] = follower_sc

    prof['repos']           = [construct_rand_repo() for x in range(prof['repos_count'])]
    prof['followers']       = followers

    return prof

def construct_rand_repo():

    repo = {}
    commits_count       = randint(1,100)
    forks_count         = randint(1,50)
    watchers_count      = randint(1,50)
    contribs_count      = randint(1,20)
    loc                 = randint(20, 500)
    repo_created_at     = random_date('1/1/2005 1:30 PM', '7/1/2013 4:50 AM')
    repo_last_commit    = random_date(repo_created_at,    '8/1/2013 4:50 AM')
    watchers = {}
    for x in range(watchers_count):
        watcher_id = randint(1, 5000)
        watcher_sc = randint(1, 1000)
        watchers[watcher_id] = watcher_sc

    forkers = {}
    for x in range(forks_count):
        forker_id = randint(1, 5000)
        forker_sc = randint(1, 1000)
        forkers[forker_id] = forker_sc

    contributors = {}
    for x in range(contribs_count):
        contributor_id = randint(1, 5000)
        contributor_sc = randint(1, 1000)
        contributors[contributor_id] = contributor_sc


    commits = []
    ts      = commits_timestamps(repo_created_at, repo_last_commit, commits_count)
    for x in range(commits_count):
        addns = randint(1, 100)
        delns = randint(1, 50)
        commit = { 'ts': ts[x], 'add':addns, 'del': delns }
        commits.append(commit)

    repo['created_at']      = commits[0]['ts']
    repo['updated_at']      = commits[-1]['ts']
    repo['forkers']         = forkers 
    repo['watchers']        = watchers
    repo['contributors']    = contributors
    repo['commits']         = commits
    repo['fork']            = choice([False, True])
    repo['lang_distr']      = get_lang_distr(loc)
    return repo


def construct_rand_commit():
    return None







# ------------------------------------------------------------------------

LANGUAGES = ["JAVA", "C", "C++", "Objective-C", "PHP", "C#", "Visual Basic", "Python", "Javascript", "Ruby", "HTML", "CSS" ]

def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    start = datetime.strptime(start, '%m/%d/%Y %I:%M %p')
    end   = datetime.strptime(end,   '%m/%d/%Y %I:%M %p')
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    result_date = start + timedelta(seconds=random_second)
    return result_date.strftime('%m/%d/%Y %I:%M %p')


def commits_timestamps(sd, ed, n):
    # days      = randint(1, 365)
    # commits_c = n
    
    # # --- randomize ---
    # ps_s      = datetime.strptime('1/1/2005 1:30 PM', '%m/%d/%Y %I:%M %p')
    # ps_e      = datetime.strptime('7/1/2013 4:50 AM', '%m/%d/%Y %I:%M %p')
    # seed_s, seed_e = sorted((random_date(ps_s, ps_e), random_date(ps_s, ps_e)))
    # # -----------------

    # start = random_date(seed_s, seed_e)
    # end   = start + timedelta(days=days)

    commits_ts = []
    for x in range(n):
        commits_ts.append(random_date(sd, ed))
    return sorted(commits_ts)


def get_lang_distr(loc):
    distr = {}
    while loc > 0:
        lang     = choice(LANGUAGES)
        lang_loc = randint(1, loc)
        
        if lang in distr:
            distr[lang] += lang_loc
        else:
            distr[lang] = lang_loc
        
        loc     -= lang_loc
    return distr


