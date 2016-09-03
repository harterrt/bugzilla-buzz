import requests
import json

def main():
    response = requests.get(
        "https://bugzilla.mozilla.org/rest/bug?include_fields=id,summary" +
        "&email1=rharter@mozilla.com" +
        "&emailassigned_to1=1" +
        "&emailcc1=1"
        "&last_change_time=2016-08-28"
        )
    bugs = json.loads(response.text)['bugs']

    for bug in bugs:
        print "Bug {id}: {summary}".format(**bug)

    return bugs

# if __name__ == "__main__":
#     main()
