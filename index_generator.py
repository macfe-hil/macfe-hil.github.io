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
    <link href="https://unpkg.com/tabulator-tables@5.5.2/dist/css/tabulator.min.css" rel="stylesheet"> 
  </head>
  <body class="container mt-5">
    <h1 class="mb-4">Test Reports</h1>
    <div id="example-table"></div>
    
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
    <script type="text/javascript" src="https://unpkg.com/tabulator-tables@5.5.2/dist/js/tabulator.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/luxon@3.4.4/build/global/luxon.min.js"></script>
    <script type="module">
      import TabulatorFull from './assets/tabulator-master/src/js/core/TabulatorFull.js';
      import {DateTime} from './assets/luxon.js'

      $( document ).ready(function() {
        window.DateTime = DateTime

        var tabledata = [
          {% for test in tests %}
            {id: {{ loop.index }}, name:"Test Name Goes Here", ispassed:"{{ 'Pass' if test.testPassed else 'Fail' }}", linkname:"hil_report_{{ test.date }}_{{test.time}}.html", link:"{{ reports_directory }}hil_report_{{ test.date }}_{{test.time}}.html", datetime:"{{ test.date }} {{ test.time }}"},
          {% endfor %}
        ];
              
        var table = new TabulatorFull("#example-table", {
          data:tabledata,           //load row data from array
          layout:"fitColumns",      //fit columns to width of table
          responsiveLayout:"hide",  //hide columns that don't fit on the table
          addRowPos:"top",          //when adding a new row, add it to the top of the table
          history:true,             //allow undo and redo actions on the table
          pagination:"local",       //paginate the data
          paginationSize:7,         //allow 7 rows per page of data
          paginationCounter:"rows", //display count of paginated rows in footer
          movableColumns:true,      //allow column order to be changed
          initialSort:[             //set the initial sort order of the data
              {column:"name", dir:"asc"},
          ],
          columnDefaults:{
              tooltip:true,         //show tool tips on cells
          },
          columns:[                 //define the table columns
              {title:"Id", field:"id", width:30},
              {title:"Name", field:"name"},
              {title:"Link", field:"link", formatter:"link", formatterParams:{
                  labelField:"linkname",
                  urlPrefix:"",
                  target:"_blank",
              }},
              {title:"DateTime", field:"datetime", width:250, sorter:"datetime", hozAlign:"center", sorterParams:{
                  format:"dd-MM-yyyy HH-mm-ss",
                  alignEmptyValues:"top",
              }},
              {title:"Pass or Fail", field:"ispassed"},
          ],
        });
      });
    </script>
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