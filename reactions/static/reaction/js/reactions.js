$(function () {
  
  
   $('.reaction-button').on('click', function () {
      var $this = $(this);
      var type = $this.attr('data-reaction');
      var productId = $this.attr('data-id');

      $.ajax({
          url: '/reaction/' + productId,
          data: {
              'reaction': type
          },
          success: function (data) {
              if (data.count > 0) {
                  if (data.count > 1) {
                      $this.parent().siblings('#reactions').text(data.count + ' reactions');
                      $this.parent().siblings('#normals').text(data.normal);
                      $this.parent().siblings('#smile').text(data.smile);
                      $this.parent().siblings('#love').text(data.love);
                      $this.parent().siblings('#wish').text(data.wish);
                      
                  } else {
                      $this.parent().siblings('#reactions').text(data.count + ' reaction');
                     $this.parent().siblings('#normals').text(data.normal);
                     $this.parent().siblings('#smile').text(data.smile);
                      $this.parent().siblings('#love').text(data.love);
                      $this.parent().siblings('#wish').text(data.wish);
                     
                  }
              } else {
                  $this.parent().siblings('#reactions').text('0');
                  $this.parent().siblings('#normals').text('0');
                     $this.parent().siblings('#smile').text('0');
                      $this.parent().siblings('#love').text('0');
                      $this.parent().siblings('#wish').text('0');
                      
              }
          }
      })
    });
});