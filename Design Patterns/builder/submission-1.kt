class Meal {
    private var cost: Double = 0.0
    private var takeOut: Boolean = false
    private var main: String? = null
    private var drink: String? = null

    fun getCost(): Double = cost
    fun getTakeOut(): Boolean = takeOut
    fun getMain(): String? = main
    fun getDrink(): String? = drink

    fun setCost(cost: Double) { this.cost = cost }
    fun setTakeOut(takeOut: Boolean) { this.takeOut = takeOut }
    fun setMain(main: String) { this.main = main }
    fun setDrink(drink: String) { this.drink = drink }
}

class MealBuilder {
    private val meal: Meal = Meal()

    fun addCost(cost: Double): MealBuilder {
        this.meal.setCost(cost)
        return this 
    }

    fun addTakeOut(takeOut: Boolean): MealBuilder {
        this.meal.setTakeOut(takeOut)
        return this 
    }

    fun addMainCourse(main: String): MealBuilder {
         this.meal.setMain(main)
        return this
    }

    fun addDrink(drink: String): MealBuilder {
        this.meal.setDrink(drink)
        return this
    }

    fun build(): Meal {
        return this.meal;
    }
}
