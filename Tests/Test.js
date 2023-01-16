class Animal {

	#noise

	constructor(name, type) {
		this.name = name
		this.type = type
        switch(this.type) {
            case "Guinea Pig":
                this.#noise = "Squeak"
                break
            default:
                this.#noise = "Unknown"
        }
		
	}

	sayHello() {
		console.log(this.#noise)
	}
}

let huihui = new Animal("Hui Hui", "Guinea Pig")

huihui.sayHello()

//having the # in front (needs to be declared first) means you cant change ferom outside the classd













//get lets it be returned like any other property
//set happens when you set that property
//get and set don't take () at the end

class Square{
    
	constructor(sideLength) {
		this.sideLength = sideLength
	}

	get perimeter() {
		return this.sideLength * 4
	}

    get area() {
        return this.sideLength * this.sideLength
    }

    set area(newArea) {
        this.sideLength = Math.sqrt(newArea)
    }

}

let five = new Square(5)

console.log("Area: " + five.area)
console.log("Perimeter: " + five.perimeter)

five.area = 49
console.log("new Side Length: " + five.sideLength)






//static lets you call on the class, but not an instance of the class

class CommonMath{
    static square(number){
        return number * number
    }
}

console.log(CommonMath.square(5))



class Square2{

    #sideLength
    
	constructor(sideLength) {
		this.#sideLength = sideLength
	}

	get perimeter() {
		return this.#sideLength * 4
	}

    get area() {
        return this.#sideLength * this.#sideLength
    }

    set area(newArea) {
        this.#sideLength = Math.sqrt(newArea)
    }

    get sl(){
        return this.#sideLength
    }

}

let three = new Square2(3)

console.log("Area: " + three.area)
console.log("Perimeter: " + three.perimeter)

three.area = 49
console.log("new Side Length: " + three.sl)
