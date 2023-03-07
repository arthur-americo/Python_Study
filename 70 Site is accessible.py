'''Python code that tests if the Github site is accessible by the used computer.
This code uses the requests library to send an HTTP GET request to the Github website. 
If the request is successful and returns a 200 status code, it means that the Github site is accessible. 
Otherwise, an error message will be printed.
'''
import requests

def test_github_access():
    url = 'https://github.com'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print('Github site is accessible.')
        else:
            print(f'Github site returned status code {response.status_code}.')
    except requests.exceptions.RequestException as e:
        print(f'An error occurred while trying to access Github: {e}')

test_github_access()