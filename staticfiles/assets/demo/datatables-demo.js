$(document).ready(function() {
    $('#datatablesSimple').dataTable( {
            "oLanguage": {
                "sLengthMenu": "Display _MENU_ records per page",
                "sZeroRecords": "Nothing found - sorry",
                "sInfo": "Showing _START_ to _END_ of _TOTAL_ records",
                "sInfoEmpty": "Showing 0 to 0 of 0 records",
                "sInfoFiltered": "(filtered from _MAX_ total records)"
            }
        } );
    } );



// Call the dataTables jQuery plugin
$(document).ready(function() {
  $('#dataTable').DataTable();
});
