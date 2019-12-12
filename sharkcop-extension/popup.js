chrome.runtime.onMessage.addListener(function(request, sender) {
    if (request.action == "getSource") {
      message.innerText = request.source;
    }
  });
  
  function onWindowLoad() {
  
    var message = document.querySelector('#message');
    message.innerText = 'You are being protected by SharkCop. We will highlight dangerous links';
  
  }
  
  window.onload = onWindowLoad;