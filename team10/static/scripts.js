$(document).ready(function() {
  $("button").on("click", function(){
      $("iframe").attr("src", "/" + this.id);
  }); // button click
}); // document ready
