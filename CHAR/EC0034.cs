using System;
using System.Globalization;

class programa
{
    static string name = "";
    static void Main(string[] args)
    {
        string cad = "Hola Buenas tardes";
        Console.WriteLine($"Primera letra de la cadena {cad.Substring(0, 1)} y la ultima {cad.Substring(cad.Length-1, 1)}");
    }
}