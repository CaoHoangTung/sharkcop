

chrome.tabs.onUpdated.addListener(function() {
    onWindowLoad();
    });
    
    setInterval(function() { 
      
        var a = JSON.parse(localStorage.getItem("link"));
        print(a);
        for (let index = 0, len = a.length; index < len; ++index) {
           if (a[index].status==0){
                a[index].status = check(a[index].url); 
           }       
        }
    },10000);   
    chrome.extension.onMessage.addListener(function(request, sender) {
    if (request.action == "getSource") {
    htmlcontent = request.source;
    }
    
    });

