interface Shape {
    fun clone(): Shape
}

class Rectangle(private val width: Int, private val height: Int) : Shape {
    fun getWidth(): Int = width
    fun getHeight(): Int = height

    override fun clone(): Shape {
        // Write your code here
        return Rectangle(getWidth(), getHeight())
    }
}

class Square(private val length: Int) : Shape {
    fun getLength(): Int = length

    override fun clone(): Shape {
        // Write your code here
        return Square(getLength());
    }
}

class Test {
    fun cloneShapes(shapes: List<Shape>): List<Shape> {
        val newList = ArrayList<Shape>()
        // Write your code here
        shapes.forEach {
            newList.add(it.clone())
        }
        return newList
    }
}
