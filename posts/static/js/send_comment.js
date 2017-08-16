
  $(function () {
    $("#send_comment").submit(function (e) {
      e.preventDefault();
      var data=new FormData(this);
      var postId= $(this).attr('data-post-id');
      console.log(postId);
      $.ajax({
        url: '/post/commenter/' + postId,
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


