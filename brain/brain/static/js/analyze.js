$(document).ready(function() {
    // 从后端获取文本内容
    $.get("/your-backend-endpoint", function(data) {
        // 将获取到的文本插入到#backendText div中
        $("#backendText").text(data);
    });
});