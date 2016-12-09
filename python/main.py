from datetime import date
import requests
import json

# TODO: harterrt:
# * Set default date to one week ago
# * Add flag to override default active-since date
# * Add changes/comments
def main():
    response = requests.get(
        "https://bugzilla.mozilla.org/rest/bug?include_fields=id,summary" +
        "&email1=rharter@mozilla.com" +
        "&emailassigned_to1=1" +
        "&emailcc1=1"
        "&last_change_time=2016-12-01"
        )
    bugs = json.loads(response.text)['bugs']

    for bug in bugs:
        print "[Bug {id}](http://bugzil.la/{id}): {summary}".format(**bug)

    return bugs

# if __name__ == "__main__":
#     main()
