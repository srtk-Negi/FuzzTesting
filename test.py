import requests


def test(challenge):
    session = requests.Session()
    form_page_url = "http://50.112.61.219:8000/fuzzme/"
    response = session.get(form_page_url)

    csrf_token = session.cookies.get("csrftoken")

    submit_url = "http://50.112.61.219:8000/fuzzme/"

    data = {
        "csrfmiddlewaretoken": csrf_token,
        "abc123": "egs622",
        "challenge": challenge,
    }

    response = session.post(submit_url, data=data)

    if "success" in response.text.lower():
        print(f"Found the string: {challenge}")


def main():
    with open("fuzzed.txt", "r") as f:
        for line in f:
            test(line.strip())


if __name__ == "__main__":
    main()
