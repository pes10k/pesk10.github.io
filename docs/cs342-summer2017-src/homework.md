---
layout: page
title: Homework
permalink: /homework/
---

<table>
    <thead>
        <tr>
            <th>Assignment</th>
            <th>Topic</th>
            <th>Due Date</th>
        </tr>
    </thead>
    <tbody>
        {% for homework in site.homework %}
            <tr>
                <td>
                    <a href="{{ homework.url | relative_url }}">{{ homework.title }}</a>
                </td>
                <td>
                    {{ homework.topic }}
                </td>
                <td>
                    {{ homework.due_date  | date_to_long_string }}
                </td>
            </tr>
        {% endfor %}
    </tbody>
</table>
