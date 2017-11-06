package com.pepperlang;

public static void Parse(string pl)
{
  private Array l = pl.Split("\n");
  for(p in l)
  {
    private Array x = p.split(" ");
    private string cmd = x[0];
    x.Remove(0);
    switch(cmd)
    {
      case "Command.Print":
        Console.WriteLine(x.join(" "));
      break;
      case "Command.Echo":
        Console.WriteLine(x.join(" "));
        Console.WriteLine(x.join(" "))
      break;
      default:
        Console.WriteLine("Internal Error: Invalid Syntax")
      break;
    }
  }
}

namespace pepper
{
  public static void Main(string[] args)
  {
    
  }
}
