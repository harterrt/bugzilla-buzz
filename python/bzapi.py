from datetime import date, timedelta
import requests
import json

# TODO: harterrt:
# x Set default date to friday at least one week ago
# * Add flag to override default active-since date
# * Figure out how to package the CLI - pinboard links
# * Add changes/comments overview

API_BASE = "https://bugzilla.mozilla.org/rest/bug?include_fields=id,summary" + \
             "&email1=rharter@mozilla.com" + \
             "&emailassigned_to1=1"

def get_bugs(additional_args = ""):
    response = requests.get(API_BASE + additional_args)
    return json.loads(response.text)['bugs']
 
def summarize_bugs(bugs):
    """Summarizes a list of bugs for snippets"""
    fmt_str = "[Bug {id}](http://bugzil.la/{id}): {summary}"

    return "\n".join(map(lambda xx: fmt_str.format(**xx), bugs))

def get_current_bugs():
    return get_bugs("&priority=P1&o1=notequals&v1=RESOLVED&f1=bug_status")

def get_recently_active_bugs(start_date):
    return get_bugs(
        "&emailcc1=1" + 
        "&last_change_time={start_date}".format(start_date=start_date)
    )

def get_start_day(today = date.today()):
    # Decide how far back we want to look for "fresh" bugs
    # Returns Friday, at least a week ago
    last_friday = today - timedelta(((today.weekday() + 3) % 7) + 7)

    return last_friday.isoformat()
