using System;
using System.Globalization;

class programa
{
    static string name = "";
    static void Main(string[] args)
    {
        int[] num = new int[5];
        Console.WriteLine("Dame 5 numeros enteros");
        int.TryParse(Console.ReadLine(), out int num1);
        num[0] = num1;
        int.TryParse(Console.ReadLine(), out int num2);
        num[1] = num2;
        int.TryParse(Console.ReadLine(), out int num3);
        num[2] = num3;
        int.TryParse(Console.ReadLine(), out int num4);
        num[3] = num4;
        int.TryParse(Console.ReadLine(), out int num5);
        num[4] = num5;
        Console.WriteLine($"Numeros: {num[0]}, {num[1]}, {num[2]}, {num[3]}, {num[4]}");
    }
}