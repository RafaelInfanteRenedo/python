using System;
using System.Globalization;

class programa
{
    static string name = "";
    static void Main(string[] args)
    {
        while (true)
        {
            Console.WriteLine("Introduzca un numero entero");
            string numero = Console.ReadLine();
            if (int.TryParse(numero, out int numero2))
            {
                Console.WriteLine($"El {numero2} me sirve. ¡Muchas gracias!");
                break;
            }
            else
            {
                Console.WriteLine("Necesito un numero entero, gracias");
            }
        }
    }
}