using System;
using System.Globalization;

class programa
{
    static string name = "";
    static void Main(string[] args)
    {
        Console.WriteLine($"Introduce un nombre");
        string nombre = Console.ReadLine();
        Console.WriteLine($"El nombre es: {nombre}");
    }
}