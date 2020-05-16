$(document).ready( function() {

    var test = $("#test").parent().width()
    $("#test").css('width')

    if (window.innerWidth <= 990) {
        $('#detailedView').css( "border-radius", "20px 20px 0px 0px" )
        $('#cityView').css( "border-radius", "0px 0px 20px 20px" )
        $('#content').attr( "style", "" )
    }
    $(window).on('resize', function() {
        if (window.innerWidth <= 990) {
            $('#detailedView').css( "border-radius", "20px 20px 0px 0px" )
            $('#cityView').css( "border-radius", "0px 0px 20px 20px" )
            $('#content').attr( "style", "" )
        } else {
            $( "#spacing" ).remove()
            $('#detailedView').css( "border-radius", "20px 0px 0px 20px" )
            $('#cityView').css( "border-radius", "0px 20px 20px 0px" )
            $('#content').attr( "style", "margin: 0; position: absolute; top: 50%; left: 50%; -ms-transform: translate(-50%, -50%); transform: translate(-50%, -50%);" )
        }
    })

});