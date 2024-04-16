document.getElementById("uploadButton").addEventListener("click", function() {
    // 这里是处理文件上传的代码
});


// 连接设备的函数
function connectDevice() {
  // 在这里执行选择连接设备的操作
  alert('选择连接设备');
}

// 页面加载完成后执行的操作
document.addEventListener('DOMContentLoaded', function() {
  // 提交按钮点击事件
  document.getElementById('submit-btn').addEventListener('click', function() {
    window.location.href = '../../content.html'; // 点击提交按钮时跳转到content.html页面
  });

  // 连接按钮点击事件
  document.getElementById('connect-btn').addEventListener('click', function() {
    connectDevice(); // 点击连接按钮时调用连接设备的函数
  });
});

