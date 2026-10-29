using System;
using System.Globalization;

class programa
{
    static string name = "";
    static void Main(string[] args)
    {
        Console.WriteLine("Dame un numero de 1 cifra");
        int numero = int.Parse(Console.ReadLine());
        switch (numero)
        {
            case 0:
                Console.Write("Cero");
                break;
            case 1:
                Console.Write("Uno");
                break;
            case 2:
                Console.Write("Dos");
                break;
            case 3:
                Console.Write("Tres");
                break;
            case 4:
                Console.Write("Cuatro");
                break;
            case 5:
                Console.Write("Cinco");
                break;
            case 6:
                Console.Write("Seis");
                break;
            case 7:
                Console.Write("Siete");
                break;
            case 8:
                Console.Write("Ocho");
                break;
            case 9:
                Console.Write("Nueve");
                break;
            default:
                Console.WriteLine("Número no válido");
                break;
        }
    }
}