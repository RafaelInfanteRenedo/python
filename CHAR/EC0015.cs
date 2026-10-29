using System;
using System.Globalization;

class programa
{
    static string name = "";
    static void Main(string[] args)
    {
        Console.WriteLine("Dame tres numeros");
        int n1 = int.Parse(Console.ReadLine());
        int n2 = int.Parse(Console.ReadLine());
        int n3 = int.Parse(Console.ReadLine());
        if (n1 > n2 && n1 > n3)
        {
            Console.WriteLine($"El mayor es {n1}");
            if (n2 > n3)
            {
                Console.WriteLine($"El menor es {n3}");
            }
            else
            {
                Console.WriteLine($"El menor es {n2}");
            }
        }else if(n2 > n1 && n2 > n3)
        {
            Console.WriteLine($"El mayor es {n2}");
            if (n1 > n3)
            {
                Console.WriteLine($"El menor es {n3}");
            }
            else
            {
                Console.WriteLine($"El menor es {n1}");
            }
        }
        else
        {
            Console.WriteLine($"El mayor es {n3}");
            if (n1 > n2)
            {
                Console.WriteLine($"El menor es {n2}");
            }
            else
            {
                Console.WriteLine($"El menor es {n1}");
            }
        }
    }
}