function getLast(number){
$.getJSON( "http://7ol.eu/api/api.php/connection/last/"+number, function( data ) {
  var items = [];
  $.each( data, function( key, val ) {
    items.push( "<tr>"+ "<td>"+val.id+"</td>" + "<td>"+val.time+"</td>"+ "<td>"+"<a href='http://www.ipvoid.com/scan/"+val.ip+"/'>"+val.ip+"</a>"+"</td>"+ "<td>"+val.port+"</td>"+ "<td>"+val.portHacker+"</td>" + "</tr>" );
  });
 
  $( "<tbody/>", {
    html: items.join( "" )
  }).appendTo( "table" );
});
}

getLast(10);

$("#ipInput").keyup(function(event){
    if(event.keyCode === 13){
        $("#serachip").click();
    }
});

function getIP() {
$( "#hiddenth" ).removeClass( "hide" );
$( "tbody" ).remove();

if (!$("#ipInput").val()) {
$( "#hiddenth" ).addClass( "hide" );
getLast(10);
} else { 
$.getJSON( "http://7ol.eu/api/api.php/cinput/ip/"+$("#ipInput").val(), function( data ) {
  var items = [];
  $.each( data, function( key, val ) {
    items.push( "<tr>"+ "<td>"+val.id+"</td>" + "<td>"+val.time+"</td>"+ "<td>"+"<a href='http://www.ipvoid.com/scan/"+val.ip+"/'>"+val.ip+"</a>"+"</td>"+ "<td>"+val.port+"</td>"+ "<td>"+val.input+"</td>"+ "<td>"+val.portHacker+"</td>" + "</tr>" );
  });
 
  $( "<tbody/>", {
    html: items.join( "" )
  }).appendTo( "table" );
});}


$( "table" ).hide();
$( "table" ).show( "slow" );
}