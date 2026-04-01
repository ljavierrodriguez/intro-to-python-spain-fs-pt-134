/* Ciclos */
/* 

for

for in

for of

while

do-while

*/

let numeros = [1, 2, 3]

for(let i = 1; i <= 10; i++){
    console.log(i)
}

for(let i = 0; i < numeros.length; i++){
    console.log(numeros[i])
}

for(let indice in numeros){
    console.log(numeros[indice]) // 1 2 3
}

for(let valor of numeros){
    console.log(valor) // 1 2 3
}

let indice = 0;
while(indice < numeros.length){
    console.log(numeros[indice])
    indice++
}