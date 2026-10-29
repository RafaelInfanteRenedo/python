using System;
using System.Globalization;

class programa
{
    static string name = "";
    static void Main(string[] args)
    {
        Console.WriteLine("Dame una palabra o frase");
        string palabra = Console.ReadLine();
        palabra = palabra.Replace(" ", "").ToLower();
        char[] aux = palabra.ToCharArray();
        Array.Reverse(aux);
        string palabra2 = newstring(aux);
        Console.WriteLine(palabra==palabra2 ? "Son palindromas" : "No son palindromas");
    }
}