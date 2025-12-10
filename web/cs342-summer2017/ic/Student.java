/**
 * @file
 * Pseudo code for practicing using visibility modifiers (public, private,
 * protected), and "static" for refactoring.
 */

public class Student {

  private String schoolName = "University of Illinois at Chicago 👍";
  private Integer netid;
  private String name;
  private String school;

  Student(Integer anId) {
    this.netid = anId;

    // Create a connection to some database, so that we can learn the
    // name of the student that corresponds to this id.
    DbConnection conn = new DbConnection();
    String sqlQuery = "SELECT * FROM students WHERE id = " + this.netid + " LIMIT 1";

    // Use the netId to query the database and get the students name
    DbRecord databaseRecord = conn.query(sqlQuery);

    this.name = databaseRecord.name;
  }

  public Float currentGPA() {

    // Re-fetch the database record, in case anything has changed since this
    // instance was created.
    DbConnection conn = new DbConnection();
    String sqlQuery = "SELECT * FROM students WHERE id = " + this.netid + " LIMIT 1";

    // Use the netId to query the database and get the students name
    DbRecord databaseRecord = conn.query(sqlQuery);

    // Extract the GPA from the database record.
    Float gpa = new Float(databaseRecord.gpa);

    return gpa;
  }

  public String description() {
    String desc = String.format("%s is a student at %s with a GPA of %f",
                                this.name, this.schoolName, this.currentGPA());
    return desc;
  }
}

/**
 * Sample code that reads in student ids, and then calculates the average
 * GPA for those students.
 */
public class Main {
  public static void main(String[] args) {

    ArrayList<Student> aWholeMessOfStudents = new ArrayList<>();

    // First create a student object for each id passed on the commandline
    for (String anArg : args) {
      int studentID = String.toValue(anArg);
      aWholeMessOfStudents.add(new Student(studentID));
    }

    // Now calculate the average GPA of a group of students.
    int numStudents = aWholeMessOfStudents.size();
    double totalGpas = 0.0;
    for (Student aStudent : aWholeMessOfStudents) {
      totalGpas += aStudent.currentGPA();
    }
    double averageGpa = totalGpas / numStudents;
  }
}
