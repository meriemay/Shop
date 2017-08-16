
  $(function () {
    $("#send_post").submit(function (e) {
      e.preventDefault();
      var data=new FormData(this);
      $.ajax({
        url: '/post/create_post/',
        data: data,
        cache: false,
        type: 'post',
        contentType : false,
        processData : false,

        success: function (data) {
        $(".post").prepend(data);
        }
      });
      return false;
    });
  });


