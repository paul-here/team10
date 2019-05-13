// Name: scripts.js
// Group Members: Chris Mayers, Paul Whipp, Chuy Gomez, David Gin
// Date: 5/12/2019
// Class: CST 205
// Description: JQuery code to link buttons to the iframe

$(document).ready(function() {
  $("button").on("click", function(){
      $("iframe").attr("src", "/" + this.id);
  }); // button click
}); // document ready
