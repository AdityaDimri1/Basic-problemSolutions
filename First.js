                                             // Variable
var a=10
console.log(a)

var b=23
console.log(b)

                                    // Array & It's builtin method
arr=[1,'aadi',2.3,false,4,5,6,1]
console.log(arr)
console.log(arr[3])
console.log(arr.length)

arr.pop()                   
console.log(arr)           //(remove last element)

arr.push(12)             
console.log(arr)
                        //(shift method remove element from starting)
arr.shift()
console.log(arr)

arr.unshift(24)
console.log(arr)

                                        // Objects In JS (key value pair)

// person = {
//     name : "Aadi",
//     Age:22,
//     Language :'Hindi' 
// }
                             // All values of the object 
// console.log(person)         
                                // print some key of the object 2-ways
                        // 1st is Dot notation (Good )
// console.log(person.Age)
                        // 2nd is bracket notation
// console.log(person['name'])

                          // object with multiple feature

// per = {
//     name:'Adi',
//     age: 20,
//     city:{
//         name:'Delhi',
//         code:123456
//     },
//     friend:['Mohit','Labbi']
// }
                        // Access array print index  
// console.log(per.friend[1])
                        // Access nested object
// console.log(per.city.code)
                        // update object 
// per.age=22
// console.log(per)
                        // add one more key value
// per.sports=['cricket','football','chess']
// console.log(per)

                                            
                                            // Conditional & Control Flow
                                            
                                // Takes user input 
// const prompt=require("prompt-sync")({sigint:true});     
// let score = prompt('What is the score?');

// if(score>90){
//     console.log('A')
// }
// else if(score>80){
//     console.log('B')
// }
// else if (score>70){
//     console.log('C')
// }
// else{
//     console.log('F')
// }
        
                                                // LOOP's

// for (i=0;i<=10;i++){
//         console.log(i)
// }
                        // square the number 
                
// num=[2,4,6,8,9]
// square =[]
// for(i=0;i<num.length;i++){
//         square.push(num[i]*num[i])
// }
//  console.log(square)

                        // while Loop & D0-while
// i =1
// n=10
// while(i<=10){
//         console.log(i)
//         i++
// }

// i=10
// n=10
// do{
//         console.log(i)
//         i++
// }while(i<=n)

                        // For Loop in 
// a={
//         primary:'Red',
//         secondary:'Green',
//         tertiary:'Blue'
// }
// for(color in a){
//         console.log(color ,'->',a.color)
// }

// a=['green', 'blue' , 'red' , 'yellow' ,'skyblue']
// for(color in a){
//         console.log(a[color])
// }


                        // For loop of 

// scores=[49,23,53,55]
// for (score of scores){
//         console.log(score)
// }

// colors = ['red','green','blue']
// for ([index,color] of colors.entries()){
//         console.log(index,'->',color)
// }

// str='Hello'
// for(c of str){
//         console.log(c)
// }