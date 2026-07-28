async function enviarPregunta(){

    let texto = document.getElementById("pregunta").value;

    if(texto=="")
        return;

    let chat = document.getElementById("chat");

    chat.innerHTML +=
        "<div class='usuario'><div class='burbujaUsuario'>"
        + texto +
        "</div></div>";

    document.getElementById("pregunta").value="";

    const respuesta = await fetch("/preguntar",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({

            pregunta:texto

        })

    });

    const datos = await respuesta.json();

    chat.innerHTML +=
        "<div class='bot'><div class='burbujaBot'>"
        + datos.respuesta +
        "</div></div>";

    chat.scrollTop = chat.scrollHeight;

}
