using System;
using System.Globalization;

class programa
{
    static string name = "";
    static void Main(string[] args)
    {
        Console.WriteLine("Dame tres numeros y te hago la suma");
        string a = Console.ReadLine();
        string b = Console.ReadLine();
        string c = Console.ReadLine();
        int c3 = 0;
        int a2 = Convert.ToInt32(a);
        int b2 = int.Parse(b);
        bool c2 = int.TryParse(c, out int c3);
        int resultado = a2+b2+c3;
        Console.WriteLine($"{a} + {b} + {c} = {resultado}");
    }
}