#  github_languages.py

import sys
import operator
from collections import defaultdict

import requests
from secret import USERNAME, PASSWORD

def git_repositories(user):
	""" Retrieve a list of a users repositories """
	url = "https://api.github.com/users/{user}/repos".format(user=user)
	response = requests.get(url, auth=(USERNAME,PASSWORD))
	return response.json()

def main():
	""" Main function """
	repositories = git_repositories(sys.argv[1])
	print repositories


if __name__ == '__main__':
	main()