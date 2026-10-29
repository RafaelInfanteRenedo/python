
using System;
using System.Globalization;

class programa
{
    static string name = "";

    static void Main(string[] args)
    {
        int[] array = new int[5];
        int contEle = 0;

        while (true)
        {
            Console.WriteLine("----- Menú -----");
            Console.WriteLine("1. Agregar a array dinámico");
            Console.WriteLine("2. Listar");
            Console.WriteLine("3. Mostrar promedio");
            Console.WriteLine("4. Salir");
            Console.WriteLine("Introduce una opcion");

            string opcion = Console.ReadLine();

            if (int.TryParse(opcion, out int opcion2)
                && opcion2 > 0 && opcion2 < 5)
            {
                switch (opcion2)
                {
                    case 1:
                        if (contEle < array.Length)
                        {
                            Console.WriteLine("Dame un numero entero");
                            string num = Console.ReadLine();

                            if (int.TryParse(num, out int numero))
                            {
                                array[contEle] = numero;
                                contEle++;
                                Console.WriteLine("Numero agregado");
                            }
                            else
                            {
                                Console.WriteLine("Necesito un numero entero");
                            }
                        }
                        else
                        {
                            Console.WriteLine("El array esta completo");
                        }
                        break;

                    case 2:
                        if (contEle == 0)
                        {
                            Console.WriteLine("El array esta vacio");
                        }
                        else
                        {
                            for (int i = 0; i < contEle; i++)
                            {
                                Console.WriteLine(array[i]);
                            }
                        }
                        break;

                    case 3:
                        if (contEle == 0)
                        {
                            Console.WriteLine("El array esta vacio");
                        }
                        else
                        {
                            int suma = 0;
                            double promedio = 0;

                            for (int i = 0; i < contEle; i++)
                            {
                                suma += array[i];
                            }

                            promedio = Convert.ToDouble(suma)
                                     / Convert.ToDouble(contEle);

                            Console.WriteLine($"El promedio del array es {promedio}");
                        }
                        break;

                    case 4:
                        return;
                }
            }
            else
            {
                Console.WriteLine("Opcion no valida");
            }
        }
    }
}