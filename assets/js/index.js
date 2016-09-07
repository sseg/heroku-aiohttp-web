const evtSource = new EventSource("/tick");

evtSource.addEventListener(
    "tick", 
    function(e) {
        let clock = document.getElementById("clock");
        let obj = JSON.parse(e.data);        
        clock.innerHTML = obj.data;
    }, 
    false
)

