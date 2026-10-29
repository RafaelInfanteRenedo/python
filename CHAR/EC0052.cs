using System;
using System.Dynamic;
using System.Globalization;

class programa
{
    static string name = "";
    static void Main(string[] args)
    {
        string[] cad = {"Barça", "Betis", "Malaga", "Elche", "Betis", "Malaga"};
        bool repe = false;
        int posicion1=0;
        foreach(string a in cad)
        {
            int posicion2 = 0;
            foreach (string b in cad)
            {
                if(posicion1 != posicion2 && a == b)
                {
                    repe=true;
                    break;
                }
                posicion2++;
            }
            if(repe)
            {
                Console.WriteLine($"{a} esta repetido en la posicion {posicion2+1}");
                break;
            }
            posicion1++;
        }

        //Con LINQ
        bool repetido = cad.Length != cad.Distinct().Count();
        int numRepes = cad.Length - cad.Distinct().Count();
        Console.WriteLine(repetido ? $"Hay {numRepes} valores repetidos" : "No hay valores repetidos");

        //Con hashSet
        HashSet<string> cad2 = new HashSet<string>();
        bool repes = false;
        foreach(string a in cad)
        {
            if (!cad2.Add(a))
            {
                repes = true;
                break;
            }
        }
        Console.WriteLine(repes ? "Hay valores repetidos" : "No hay valores repetidos");
    }
}