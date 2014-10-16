#  github_languages.py

import sys
import operator
from collections import defaultdict

import requests
from secret import USERNAME, PASSWORD

def get_repositories(user):
	""" Retrieve a list of a users repositories """
	url = "https://api.github.com/users/{user}/repos".format(user=user)
	#  https://api.github.com/users/Caduc/repos
	response = requests.get(url, auth=(USERNAME,PASSWORD))
	#module called python gnu pgp - check it out.  another is hashlib. getpass is a module and function
	return response.json()

def get_language_dictionaries(repositories):
	#return list of dictionaries
	language_dictionaries = []
	for repository in repositories:
		url = "https://api.github.com/repos/{owner}/{repo}/languages"
		owner = repository["owner"]["login"]
		repo = repository["name"]
		url = url.format(owner,repo)
		response = requests.get(url, auth=(USERNAME,PASSWORD))
		language_dictionaries.append(response.json())
	return language_dictionaries
	

def main():
	""" Main function """
	repositories = get_repositories(sys.argv[1])
	language = get_language_dictionaries(repositories)
	print repositories
	print language


if __name__ == '__main__':
	main()