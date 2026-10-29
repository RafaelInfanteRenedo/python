using System;
using System.Globalization;

class programa
{
    static string name = "";
    static void Main(string[] args)
    {
        Console.WriteLine("Dame una frase");
        string frase = Console.ReadLine();
        string vocales = "aeiou";
        String fraseSinMayus = frase.ToLower();
        char[] arrayVocales = vocales.ToCharArray();
        char[] aux = fraseSinMayus.ToCharArray();
        int cont = 0;
        foreach(char v in arrayVocales)
        {
            foreach(char f in aux)
            {
                if (f == v)
                {
                    cont++;
                }
            }
        }
        Console.WriteLine($"El numero de vocales que contiene la frase {frase} es: {cont}");
    }
}