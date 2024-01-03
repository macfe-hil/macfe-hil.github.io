import json
from jinja2 import Template

# File paths
json_file_path = 'historic_tests.json'
output_html_path = 'index.html'
reports_directory = './reports/'

# Read JSON data from the file
with open(json_file_path, 'r') as json_file:
    json_data = json.load(json_file)

# Jinja template for HTML with Bootstrap
template_html = """
{# template.jinja #}
<html>
  <head>
    <title>Test Reports</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
  </head>
  <body class="container mt-5">
    <h1 class="mb-4">Test Reports</h1>
    <div id="example-table"></div>
    <ul class="list-group">
      {% for test in tests %}
        <li class="list-group-item">
            {{ 'Pass' if test.testPassed else 'Fail' }}
          - Test ID: {{ test.testId }} | 
          <a href="{{ reports_directory }}pytest_report_{{ test.date }}.html">
            pytest_report_{{ test.date }}.html
          </a> - {{ test.date }}
        </li>
      {% endfor %}
    </ul>
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
  </body>
</html>
"""

# Load the template
template = Template(template_html)

# Render the template with the JSON data
rendered_html = template.render(tests=json_data, reports_directory=reports_directory)

# Write the rendered HTML to a file
with open(output_html_path, 'w') as output_file:
    output_file.write(rendered_html)