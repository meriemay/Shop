$(function () {

   $('.reaction-post').on('click', function () {
      var $this = $(this);
      var type = $this.attr('data-reaction');
      var postId = $this.attr('data-id');

      $.ajax({
          url: '/reaction_post/' + postId,
          data: {
              'reaction': type
          },
          success: function (data) {
              if (data.count > 0) {

                    if (data.like > 0){
                     $this.parent().siblings('#likes').text(data.like + 'likes');
                      } else{$this.parent().siblings('#likes').text(data.like);}
                    if (data.dislike > 0){
                     $this.parent().siblings('#dislikes').text(data.dislike + 'dislikes');
                   }else{$this.parent().siblings('#dislikes').text(data.dislike);}
                     
              
}

              else {
                  $this.parent().siblings('#reactions').text('0');
                  $this.parent().siblings('#likes').text('0');
                  $this.parent().siblings('#dislikes').text('0');
                      
              }
              if (data.comment > 0){
              $this.parent().siblings('#comments').text(data.comment + 'comments' );}
              else {$this.parent().siblings('#comments').text(data.comment);}
                         
              }
    });
});
});