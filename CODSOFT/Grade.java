import java.util.Scanner;
class Student
{
public static void main(String args[])
{
int comp, phy, chem, math, eng;
double total, p;
Scanner sc =new Scanner(System.in);
System.out.print("Enter marks of Computer Science subject:");
comp=sc.nextInt();
System.out.print("Enter marks of Physics subject:");
phy=sc.nextInt();
System.out.print("Enter marks of Chemistry subject:");
chem=sc.nextInt();
System.out.print("Enter marks of Maths subject:");
math=sc.nextInt();
System.out.print("Enter marks of English subject:");
eng=sc.nextInt();
total = eng + phy + chem + math + comp;
p = (total / 500) * 100;
System.out.println("Total marks ="+total);
System.out.println("Average Percentage = "+p);
if(p>=90)
{
System.out.print("Grade is A");
}
else if(p>=80 && p<=90)
{
System.out.print("Grade is B");
}
else if(p>=70 && p<80)
{
System.out.print("Grade is C");
}
else if(p>=60 && p<70)
{
System.out.print("Grade is D");
}
else if(p>=50 && p<60)
{
System.out.print("Grade is E");
}
else
{
System.out.print("Grade is F");
}sc.close();
}
}