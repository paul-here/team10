$(document).ready(function() {

  $(".nav").on("click", function(){

    let action = this.id;
    alert(action);

    $.ajax({
      method: "GET",
      url: "api/favoritesAPI.php",
      dataType: "json",
      data: { "action": action },
      success: function(data, status) {

      }
    }); // ajax

  }); // nav click

});
