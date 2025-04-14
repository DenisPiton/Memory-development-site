let field = document.getElementById("gr")
let but = document.getElementById("but")
but.addEventListener("click",click)
function click(event)
{

    but.hidden = true
}



// function getToken(name){
//     let cookievalue = null
//     if(document.cookie && document.cookie!=""){
//         const cookies = document.cookie.split(";")
//         for(let i = 0; i < cookies.length; i++){
//             const cookie = cookie[i].trim();
//             if(cookie.substring(0,name.length+1)===(name+"=")){
//                 cookievalue = decodeURIComponent(cookie.substring(0,name.length+1))
//                 break
//             }

//         }
//     }

// }
// function send()
// {
//     var csrftoken = getToken("csrftoken")


//     var url = "/api/"
//     fetch(url,{
//         method:'POST',
//         headers:{
//             'Content-Type':'application/json',
//             'X-CSRFToken':csrftoken
//         },
//         body:JSON.stringify({'post_data': disp.textContent})
//     })
//     .then((response)=>{
//         return response.json()
//     })
//     .then((data)=>{
//         console.log(data)
//     })
// }