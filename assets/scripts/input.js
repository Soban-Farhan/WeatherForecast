$(document).ready( function() {

    $('input[name="cities"]').select2({
        data: CA,
        placeholder: "Search new place",
        multiple: false,
        // query with pagination
        query: function(q) {
        var pageSize,
            results,
            that = this;
        pageSize = 20; // or whatever pagesize
        results = [];
            if (q.term && q.term !== '') {
                // HEADS UP; for the _.filter function i use underscore (actually lo-dash) here
                results = _.filter(that.data, function(e) {
                    return e.text.toUpperCase().indexOf(q.term.toUpperCase()) >= 0;
                });
            } else if (q.term === '') {
                results = that.data;
            }
            q.callback({
                results: results.slice((q.page - 1) * pageSize, q.page * pageSize),
                more: results.length >= q.page * pageSize,
            });
        },
    });

    $("#s2id_autogen1").css({ 'width': '75%', 'border': 'none' })

    $('#citySearchForm').on('submit', function(e) { 

        $('#searchError').text("")

        if ( $('input[name="cities"]').val() == "" ) {
            $('#searchError').text("*Please select a city. Try Again.")
            return e.preventDefault()
        } 
        // else {
        //     $("#dataSection").remove()
        //     return e.preventDefault()
        // }
        return true
    });
    

});