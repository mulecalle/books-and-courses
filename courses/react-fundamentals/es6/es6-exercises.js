// Arrow Functions Exercise
// https://github.com/varoonsahgal/react-fundamentals/blob/main/es6exercises.md#arrow-functions-exercise

const factorial =  n => n === 0 ? 1 : n * factorial(n - 1);
//console.log(factorial(3))

// Destructuring Exercise 1a
// https://github.com/varoonsahgal/react-fundamentals/blob/main/es6exercises.md#destructuring-exercise-1a


const bio = {
    title: 'Developer',
    department: 'GEC'
}

const isDeveloper = ({title, department}) => title === 'Developer' && department === 'GEC';
//console.log(isDeveloper(bio))


// Destructuring and Map() Exercise 1b
// https://github.com/varoonsahgal/react-fundamentals/blob/main/es6exercises.md#destructuring-and-map-exercise-1b

const cart = [
    [ 'Hersheys Bar', '1.00', '504' ],
    [ 'Almonds', '5.00', '321'],
    [ 'Lotion', '2.50', '287' ]
]
// const cartAsObjects = (input) => input.map(([item, price, sku]) => ({item, price, sku}));
// console.log(cartAsObjects(cart))

// ES6 Classes Exercise 1a
// https://github.com/varoonsahgal/react-fundamentals/blob/main/es6exercises.md#es6-classes-exercise-1a

class Homosapien {
    constructor(name, age) {
        this.age = age;
        this.name = name;
    }

    speak(){
        console.log("UNGH!");
    }

}

// const homo = new Homosapien('seba', '30');
// console.log(homo)
// homo.speak()

// ES6 Classes Exercise 1b
// https://github.com/varoonsahgal/react-fundamentals/blob/main/es6exercises.md#es6-classes-exercise-1b

class JavascriptDeveloper extends Homosapien {
    constructor(name, age) {
        super(name, age);
        this.company = 'Salesforce';
    }

    speak(){
        console.log("JavaScript is the most popular programming language!");
    }
}

// const jsDev = new JavascriptDeveloper('seba', '30');
// console.log(jsDev)
// jsDev.speak()

// Rest Operator Exercise
// https://github.com/varoonsahgal/react-fundamentals/blob/main/es6exercises.md#es6-classes-exercise-1b

const product = (...numbers) => numbers.reduce((acc, number) => acc * number, 1)
//console.log(product(1,2,3,4,5))

// Rest Operator Exercise #2
// https://github.com/varoonsahgal/react-fundamentals/blob/main/es6exercises.md#rest-operator-exercise-2

const unshift = (array, ...beg) => beg.concat(array);
// console.log(unshift([5,6],1,2,3))

// Spread Operator Exercise
// https://github.com/varoonsahgal/react-fundamentals/blob/main/es6exercises.md#spread-operator-exercise

const join = (arr1, arr2) => [...arr1, ...arr2];
// console.log(join([1,2], [2,3]))

// Spread Operator Exercise #2
// https://github.com/varoonsahgal/react-fundamentals/blob/main/es6exercises.md#spread-operator-exercise-2

const arr2 = [1, 2, 3, 4, 5]
const [first, ...tail] = arr2;
// console.log(first)
// console.log(tail)

// Spread Operator Exercise #3
// https://github.com/varoonsahgal/react-fundamentals/blob/main/es6exercises.md#spread-operator-exercise-3

const shallowCopyArray = (arr) => [...arr];
const arr = [1, 2, 3]
const copy = shallowCopyArray(arr)
// console.log(arr === copy)  // false
copy[0] = 'yo'
// console.log(arr) // [1, 2, 3]
// console.log(copy) // ['yo', 2, 3]

// Spread Operator Exercise #4
// https://github.com/varoonsahgal/react-fundamentals/blob/main/es6exercises.md#spread-operator-exercise-4

const shallowCopyObject = (obj) => ({...obj});
const obj = { name: 'Andrew' }
const copy2 = shallowCopyObject(obj)
// console.log(obj === copy2)  // false
copy2.name = 'Billy'
// console.log(obj) // { name: 'Andrew' }
// console.log(copy2) // { name: 'Billy' }

// Spread Operator Exercise #5
// https://github.com/varoonsahgal/react-fundamentals/blob/main/es6exercises.md#spread-operator-exercise-5

const person = { name: 'Andrew', age: 33, position: 'Software Developer' }
const {age, ...agelessPerson} = person;
// console.log(agelessPerson)

// Spread Operator Exercise #6
// https://github.com/varoonsahgal/react-fundamentals/blob/main/es6exercises.md#spread-operator-exercise-6

const merge = (obj1, obj2) => ({...obj1, ...obj2});
const obj1 = { name: 'Andrew' };
const obj2 = { asd: 'asd' };

//console.log(merge(obj1, obj2));
