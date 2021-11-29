using System;
class GFG
{
static int countMultiples(int n)
{
    int res = 0;
    for (int i =200; i> n; i--)
    if (i % 3 == 0)
    Console.Write(i+",");
        res++;
    return res;
}
static public void Main ()
{
   countMultiples(1);
}
}