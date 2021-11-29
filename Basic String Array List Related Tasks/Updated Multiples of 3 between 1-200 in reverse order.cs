using System;
class GFG
{
static int countMultiples(int n,int res)
{
    for (int i =res; i> n; i--)
    if (i % 3 == 0)
    Console.Write(i+",");
        res++;
    return res;
}
static public void Main ()
{
   countMultiples(0,200);
}
}