// Encapsulation: Using private instance variables and public methods to control access
class Person {
    private String name;
    private int age;

    public void setName(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setAge(int age) {
        if (age >= 0) {
            this.age = age;
        }
    }

    public int getAge() {
        return age;
    }
}

// Inheritance: Creating a subclass (Student) that inherits from a superclass (Person)
class Student extends Person {
    private String studentId;

    public Student(String name, int age, String studentId) {
        setName(name);
        setAge(age);
        this.studentId = studentId;
    }

    public String getStudentId() {
        return studentId;
    }
}

// Polymorphism: Using method overriding to provide different behavior in the subclass
class Teacher extends Person {
    private String employeeId;

    public Teacher(String name, int age, String employeeId) {
        setName(name);
        setAge(age);
        this.employeeId = employeeId;
    }

    public String getEmployeeId() {
        return employeeId;
    }
}

// Abstraction: Defining an abstract class and method
abstract class Shape {
    abstract double calculateArea();
}

class Circle extends Shape {
    private double radius;

    public Circle(double radius) {
        this.radius = radius;
    }

    @Override
    double calculateArea() {
        return Math.PI * radius * radius;
    }
}

public class OOP {
    public static void main(String[] args) {
        // Encapsulation
        Person person = new Person();
        person.setName("John");
        person.setAge(30);
        System.out.println("Name: " + person.getName());
        System.out.println("Age: " + person.getAge());

        // Inheritance
        Student student = new Student("Alice", 20, "12345");
        System.out.println("Student Name: " + student.getName());
        System.out.println("Student Age: " + student.getAge());
        System.out.println("Student ID: " + student.getStudentId());

        // Polymorphism
        Teacher teacher = new Teacher("Mr. Smith", 40, "T9876");
        Person p = teacher; // Polymorphism - a Teacher object can be treated as a Person
        System.out.println("Employee ID: " + p.getEmployeeId());

        // Abstraction
        Shape circle = new Circle(5.0);
        System.out.println("Circle Area: " + circle.calculateArea());
    }
}
