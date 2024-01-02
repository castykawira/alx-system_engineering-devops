#!/usr/bin/python3
"""Script to get and display an employee's TODO list progress"""

import requests
import sys


if __name__ == '__main__':
    employee_id = sys.argv[1]
    api_url = "https://jsonplaceholder.typicode.com/users"
    url = api_url + "/" + employee_id

    response = requests.get(url)
    username = response.json().get('username')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()

    with open('{}.csv'.format(employeeId), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(employeeId, username, task.get('completed'),
                               task.get('title')))
