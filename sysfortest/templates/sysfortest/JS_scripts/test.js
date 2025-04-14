const disp = document.getElementById("text")
let but = document.getElementById("but")
disp.textContent = "0"
function clicker(event)
{
    let prev = parseInt(disp.textContent)+1
    disp.textContent = prev
    console.log(parseInt(prev)+1)
}
but.addEventListener("click", clicker)

function getToken(name){
    let cookievalue = null
    if(document.cookie && document.cookie!=""){
        const cookies = document.cookie.split(";")
        for(let i = 0; i < cookies.length; i++){
            const cookie = cookie[i].trim();
            if(cookie.substring(0,name.length+1)===(name+"=")){
                cookievalue = decodeURIComponent(cookie.substring(0,name.length+1))
                break
            }

        }
    }

}
function send()
{
    var csrftoken = getToken("csrftoken")


    var url = "/api/"
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken
        },
        body:JSON.stringify({'post_data': disp.textContent})
    })
    .then((response)=>{
        return response.json()
    })
    .then((data)=>{
        console.log(data)
    })
}

const sub = document.getElementById("SUB")
sub.addEventListener("click", send)