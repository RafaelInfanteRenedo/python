//“-8 + 6 * 3”, “(2 + 7) % 5” y “2 + ( -1 * 8 ) -5 % 3”
using System;
using System.Globalization;

class programa
{
    static string name = "";
    static void Main(string[] args)
    {
        Console.WriteLine($"op1: {-8 + 6 * 3} / op2: {(2+7)%5} / op3: {2 + ( -1 * 8 ) -5 % 3}");
    }
}