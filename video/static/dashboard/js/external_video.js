var videoEreaStatic = false;
var videoEditArea = $('#video-edit-area');

$('#open-add-video-btn').click(function(){  // Jquery默认写法
    if (!videoEreaStatic) {
    videoEditArea.show();  // show() 显示
    videoEreaStatic = true;
    }
    else {
    videoEditArea.hide();  // hide() 隐藏
    videoEreaStatic = false;
    }
});