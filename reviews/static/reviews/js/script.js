function trial() 
{
    document.getElementById("demo").innerHTML = "Hi, I am your javascript from an external source";
} 

function checkboxClick(e)
{
    e.preventDefault();

    if (e.target.checked){
        localStorage.setItem('checked', true)
        // localStorage.checked = true;
    }else{
        localStorage.setItem('checked', false)
        // localStorage.checked = false;
    }
}

window.onload = function() {
    //this.alert('Page is loaded')
    if (this.document.getElementById('messageElement').classList.length > 0){            
        this.setTimeout( function(){
        this.document.getElementById('messageElement').remove();
        },
        3000);
    }  
}


setState = function(state) {
    localStorage.setItem('checked', state);
}
  
getState = function() {
   return localStorage.getItem('checked');
}

function init(){
    // var app = new App();
    var state = getState();
    var checkbox = document.getElementById('cb1');
    


    if(state == 'true'){
        checkbox.checked = true;
    }

    checkbox.addEventListener('click', function() {
        setState(checkbox.checked)
    })
}

init();