function trial() 
{
    document.getElementById("demo").innerHTML = "Hi, I am your javascript from an external source";
} 

window.onload = function() {
    // this.alert('Page is loaded')
    // print(this.document.getElementById('messageElement'))
    if(this.document.getElementById('messageElement')){
        if (this.document.getElementById('messageElement').classList.length > 0){            
            this.setTimeout( function(){
            this.document.getElementById('messageElement').remove();
            },
            3000);
        }
    }
      
}


setState = function(state) {
    localStorage.setItem('checked', state);
}
  
getState = function() {
   return localStorage.getItem('checked');
}

function changeCSS(cssFile, cssLinkIndex) {

    var oldlink = document.getElementsByTagName("link").item(cssLinkIndex);
    var newlink = document.createElement("link");
    newlink.setAttribute("rel", "stylesheet");
    newlink.setAttribute("type", "text/css");
    newlink.setAttribute("href", `/static/reviews/css/${cssFile}` );

    document.getElementsByTagName("head").item(0).replaceChild(newlink, oldlink);
}

function init(){
    var dark_theme = getState();
    var checkbox = document.getElementById('cb1');

    if(dark_theme == 'true'){
        changeCSS("dark-theme.css", 1)
        checkbox.checked = true;    
    }

    checkbox.addEventListener('click', function() {
        //alert('Page is loaded')
        
        setState(checkbox.checked)

        dark_theme = getState();
        
        if(dark_theme == 'true'){
            // console.log(state)
            console.log("Dark theme is on")
            checkbox.checked = true;
            changeCSS("dark-theme.css", 1)
            
        }else{
            console.log("Dark theme is false")
            checkbox.checked = false;
            changeCSS("style.css", 1)
        }
        // location.reload();
    })
    
}

init();