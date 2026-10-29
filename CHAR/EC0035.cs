using System;
using System.Globalization;

class programa
{
    static string name = "";
    static void Main(string[] args)
    {
        Console.WriteLine("Dame una cadena");
        string cad = Console.ReadLine();
        string vocales = "aeiou";
        int cont = 0;
        foreach(char voc in cad)
        {
            if (vocales.Contains(voc))
            {
                cont++;
            }
            
        }
        Console.WriteLine($"La cadena {cad} contiene {cont} vocales");
    }
}