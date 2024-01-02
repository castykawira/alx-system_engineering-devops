#!/usr/bin/python3
"""Script to get and display an employee's TODO list progress"""

import requests
import sys


if __name__ == '__main__':
    employee_id = sys.argv[1]
    api_url = "https://jsonplaceholder.typicode.com/users"
    url = api_url + "/" + employee_id

    response = requests.get(url)
    employeeName = response.json().get('name')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()
    done = 0
    done_tasks = []

    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task)
            done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employeeName, done, len(tasks)))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))
