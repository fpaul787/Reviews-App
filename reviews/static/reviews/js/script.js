function trial() 
{
    document.getElementById("demo").innerHTML = "Hi, I am your javascript from an external source";
} 

window.onload = function() {
    // this.alert('Page is loaded')

    if (this.document.getElementById('messageElement').classList.length > 0){
            
        this.setTimeout( function(){
        this.document.getElementById('messageElement').remove();
        },
        3000);
        

    }
}