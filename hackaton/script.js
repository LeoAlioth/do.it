window.jQuery = window.$ = jQuery;
var module_id;
var module_name;
var module_desc;
var cmd;
var type;
var value;
var status_response;
var out;

$( "#dialog" ).hide();
$( "#target" ).click(function() {
      $( "#dialog" ).show();
    $( "#dialog" ).dialog();
});

$(document).ready(function() {
  $.ajax({
   type: "GET",
   dataType: "json",
   url: "/api/modules",
   success: function(data){
     load_modules(data.data);
   }
 });

});


function load_modules(modules) {
  //inesrt api call for modules
  for (i = modules.length - 1; i >= 0; i--) {
    $("#modules_body").append(
      "<tr class='bg-gray' id='" + modules[i].id + "'>" +
      "<td>" + modules[i].name + "</td>" +
      "<td>" + modules[i].desc + "</td>" +
      "</tr>"
    );
    $("#" + modules[i].id).on("click", modules[i], get_cmds);
  }
}

//inserts table of commands for the specific module
function get_cmds(event){
  module_id=event.data.id;
  module_name=event.data.name;
  module_desc=event.data.desc;
    $.ajax({
     type: "GET",
     dataType: "json",
     url: "/api/modules/"+module_id,
     success: function(data){
       cmds(data.data);
     },
     error: function(data){
       console.log("error"+data);
     }
   });

}


function cmds(data) {

var html = "";
$("#commands-default").hide();
$("#commands").empty();
$("#commands").show();
$("#commands").append("<ul> <a id='"+module_id+"-console' class='console card bg-white text-dark'>Console</ul><ul><h4><a id='"+module_id+"-command'>"+module_name+":</a></h4></ul><br>");
  for (i = 0; i < data.cmds.length; i++){
    $("#"+module_id+"-command").append("<ul><button class='btn-primary' id='" + data.cmds[i].name+"-cmd'> "+ data.cmds[i].name+"</button><a id='"+data.cmds[i].name+"-drop'/><a>Description: "+data.cmds[i].desc+"</a></ul>");
        $("#" + data.cmds[i].name+ "-cmd").one("click",data.cmds[i], get_cmd);

  }
  $("#commands").append(html);

}
function get_cmd(data){
  cmd=data.data.name;
  $.ajax({
   type: "GET",
   dataType: "json",
   url: "/api/modules/"+module_id+"/"+cmd,
   success: function(data){
     give_cmd(data);
   },
   error: function(data){
     console.log("error"+data);
   }
 });
}


function give_cmd(data) {
status_response=data.data.status;
out=data.data["out"];
if(data.data["in"]!=0){
  j=data.data;
  $(this).parent().append("<ul id='"+cmd+"-input'><button class='btn-primary' id='" + cmd+"-input-button'> Open inputs</button></ul>");
  openInputs(j);
  }
  else{
    request_post_empty();
    }
}

function openInputs(event){

  var j=event.in;
  for(i=0;i<j.length;i++){
    $("#"+cmd+'-drop').append("<div>payload type: "+j[i].type+"<p><input type='text' id='"+j[i].name+"-payload'></input></p><p><button id='"+j[i].name+"-submit' class='btn-primary'>send to module</button></p>");
    $("#"+j[i].name+"-submit").on("click",{name: j[i].name},request_post);
  }
}


//DOESENT SEND THE DATA
function request_post_empty(){

  jsondata=JSON.stringify({data:[]});

 $.ajax({
   type: "POST",
   contentType: 'text/plain',
   dataType: "text",
   data: jsondata,
   url: "/api/modules/"+module_id+"/"+cmd,
   success: function(data){
     console.log(data);
     request_process(data);
   },
   error: function(data){
     console.log("error"+data);
   }
 });
}


function request_post(data){
console.log(data);
  name=data.data.name;
  value=parseInt($("#"+name+"-payload").val());
  jsondata=JSON.stringify({data:[value]});
 $.ajax({
   type: "POST",
   contentType: 'text/plain',
   dataType: "text",
   data: jsondata,
   url: "/api/modules/"+module_id+"/"+cmd,
   success: function(data){
     request_process(data);
   },
   error: function(data){
     console.log("error"+data);
   }
 });
}

function request_process(data){
  console.log(data);
  var j = JSON.parse(data);
  string="Server returned status: "+j.status;

  for(i=0;i<status_response.length;i++){
  if(status_response[i].hasOwnProperty(j.status)){
  string=status_response[i][j.status];
  for(i=0;i<out.length;i++){

    string=string.replace("$"+out[i].name,j.data[i]);
  }
}
}
$("#"+module_id+"-console").empty();
$("#"+module_id+"-console").append("Server response: "+string);

}
