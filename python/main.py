from datetime import date, timedelta
import requests
import json

# TODO: harterrt:
# x Set default date to friday at least one week ago
# * Add flag to override default active-since date
# * Figure out how to package the CLI - pinboard links
# * Add changes/comments overview
 
def main():
    response = requests.get(
        "https://bugzilla.mozilla.org/rest/bug?include_fields=id,summary" +
        "&email1=rharter@mozilla.com" +
        "&emailassigned_to1=1" +
        "&emailcc1=1"
        "&last_change_time={start_date}".format(start_date=get_start_day())
        )
    bugs = json.loads(response.text)['bugs']

    for bug in bugs:
        print "[Bug {id}](http://bugzil.la/{id}): {summary}".format(**bug)

    return bugs

def get_start_day(today = date.today()):
    # Decide how far back we want to look for "fresh" bugs
    # Returns Friday, at least a week ago
    last_friday = today - timedelta(((today.weekday() + 3) % 7) + 7)

    return last_friday.isoformat()

if __name__ == "__main__":
    main()
