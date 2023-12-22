import java.util.*;
import java.lang.Math;
class Numbergame {
public static void guessNumberGame()
{
Scanner sc = new Scanner(System.in);
int number = 1 + (int)(100* Math.random());
int n = 7;
int i, guess;
System.out.println("WELCOME TO THE NUMBER GUESSING GAME");
System.out.println("You Have To Guess a Number Between 1 and 100");
System.out.println("Guess Correct Number Within 7 Attempts");
System.out.println("Let's Begin The Game");
for (i = 0; i < n; i++) {
System.out.println("Guess the number:");
guess = sc.nextInt();
if (number == guess)
{
System.out.println("Congratulations!"+ " You guessed the number.");
break;
}
else if (number > guess && i != n - 1)
{
System.out.println("The guess is too low");
}
else if (number < guess && i != n - 1)
{
System.out.println("The guess is too high");
}
}
if (i == n)
{
System.out.println("The limit of attempts is over");
System.out.println("The number was " + number);
}
}
public static void main(String arg[])
{
guessNumberGame();
}
}