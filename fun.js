function INFO(){ 
let t0 = document.getElementById("t0").value;
let g0 = document.querySelector('input[name="g0"]:checked').value; 
let c0 = document.getElementById("c0").value;
let info = t0 + "\n" +g0 + "\n" +c0 + "\n" +"" 
alert(info); 
}
function ENTRADA(){ 
let info = "formulario ~>>[\n    <\n        tipo:\"etiqueta\",\n        valor:\"Nombre:\"\n    >,\n    \n    <\n        tipo:\"texto\",\n        valor: \"nombre\",\n        fondo:\"Ingrese Nombre\"\n    >,\n  \n    <\n        tipo: \"grupo-radio\",\n        nombre: \"sexo\",\n        valores: [\'Masculino\',\'cyan simp\']\n    >,\n    <\n        tipo: \"grupo-option\",\n        nombre: \"pais\",\n        valores: [\'Guatemala\',\'El salvador\',\'Honduras\']\n    >,\n    <\n        tipo:\"boton\",\n        valor: \"Valor\",\n        evento: <entrada>\n    >\n]\n" 
alert(info)
}
