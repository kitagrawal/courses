method LinearSearch(a:array<int>, l:int, u:int, e:int) returns (r:bool)
  requires 0 <= l && l <= u && u < a.Length;
  ensures r <==> exists k:: l <= k && k <= u && a[k] == e;
{
  var i := l;
  while (i <= u)
	invariant l <= i && i <= u+1;
	invariant forall k :: l <= k <= i ==> a[k] != e;
  {
    if (a[i] == e)
    {
      return true;
    }
    i := i + 1;
  }
  return false;
}


//referred: Stack Overflow, Tutorial (Dafny), ch 6 (Book)
