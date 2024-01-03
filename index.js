import {Tabulator} from 'tabulator-tables';

$( document ).ready(function() {
    var table = new Tabulator("#example-table", {
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
            {title:"Name", field:"name", editor:"input"},
            {title:"Task Progress", field:"progress", hozAlign:"left", formatter:"progress", editor:true},
            {title:"Gender", field:"gender", width:95, editor:"select", editorParams:{values:["male", "female"]}},
            {title:"Rating", field:"rating", formatter:"star", hozAlign:"center", width:100, editor:true},
            {title:"Color", field:"col", width:130, editor:"input"},
            {title:"Date Of Birth", field:"dob", width:130, sorter:"date", hozAlign:"center"},
            {title:"Driver", field:"car", width:90,  hozAlign:"center", formatter:"tickCross", sorter:"boolean", editor:true},
        ],
    });
});