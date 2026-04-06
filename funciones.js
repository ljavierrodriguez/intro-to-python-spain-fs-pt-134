/* Funciones */
/* 

1. Funciones de Nombre:

function nombreFuncion(params){
    codigo
}

2. Funciones Declarativas

const nombreFuncion = function(params){
    codigo
}

3. Funcion Flecha

const nombreFuncion = (params) => codigo 

*/

function sumar(a, b){
    return a + b
}

const restar = function(a, b){
    return a - b
}

const multiplicar = (a, b) => a * b

/* 
Manejo de Paramestros
*/

/* 1. Parametros Posicionales */

function sumar(a, b){
    return a + b
}

let resultado = sumar(10, 10) // a = 10, b = 10

/* 2. Parametros por Defecto */
function sumar(a, b = 5){
    return a + b
}

let resultado1 = sumar(10, 12) // 22
let resultado2 = sumar(10) // 15