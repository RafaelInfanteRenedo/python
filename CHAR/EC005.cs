using System;
using System.Globalization;

class programa
{
    static string name = "";
    static void Main(string[] args)
    {
        double num1 = 321;
        double num2 = 698;
        double result = num1/num2;
        Console.WriteLine($"Resultado: {result:F3}");
    }
}