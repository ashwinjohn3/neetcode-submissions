abstract class Coffee {
    abstract fun getCost(): Double
}

class SimpleCoffee : Coffee() {
    override fun getCost(): Double = 1.1
}

abstract class CoffeeDecorator(protected val decoratedCoffee: Coffee) : Coffee() {
    override fun getCost(): Double = decoratedCoffee.getCost()
}

class MilkDecorator(coffee: Coffee) : CoffeeDecorator(coffee) {
    // Implement the Milk decorator
    override fun getCost(): Double {
        return super.getCost() + 0.5
    }
}

class SugarDecorator(coffee: Coffee) : CoffeeDecorator(coffee) {
    // Implement the Sugar decorator
    override fun getCost(): Double {
        return super.getCost() + 0.2
    }
}

class CreamDecorator(coffee: Coffee) : CoffeeDecorator(coffee) {
    // Implement the Cream decorator
    override fun getCost(): Double {
        return super.getCost() + 0.7
    }
}
