using System;
using System.Globalization;

class programa
{
    static string name = "";
    static void Main(string[] args)
    {
        int[] numeros1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        int[] numeros2 = {1, 2, 3, 4, 5, 6, 7};
        int suma = 0;
        int suma2 = 0;
        for (int i = 0; i < numeros1.Length; i++)
        {
            suma+=numeros1[i];
        }
        foreach (int n in numeros2)
        {
            suma2+=n;
        }
        Console.WriteLine($"La suma de los 10 primeros numeros hecho con un for es: {suma}");
        Console.WriteLine($"La suma de los 7 primeros numeros hecho con un foreach es: {suma2}");
    }
}