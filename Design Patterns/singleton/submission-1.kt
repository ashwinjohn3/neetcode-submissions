class Singleton private constructor() {
    private var value: String? = null 

    companion object {
        private var uniqInstance: Singleton? = null

        fun getInstance(): Singleton {
            if (uniqInstance == null ){
                uniqInstance = Singleton();
            }
            return uniqInstance!! 
        }
    }

    fun getValue(): String? {
        return this.value
    }

    fun setValue(value: String) {
        this.value = value;
    }
}
