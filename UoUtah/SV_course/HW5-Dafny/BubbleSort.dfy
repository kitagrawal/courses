method BubbleSort(a:array<int>)
  ensures forall k:: forall l:: 0 <= k < l < a.Length ==> a[k] <= a[l];
  modifies a;
{
  var i:int := a.Length - 1;
  while(i > 0)
	invariant i >= 0;
	invariant forall k :: forall l :: (i < k < l < a.Length) ==> a[k] <= a[l];
	invariant forall k :: forall l :: (0 <= k <= i && i < l < a.Length) ==> a[k] <= a[l];
  {
    var j:int := 0;
    while (j < i)
	invariant j <= i;
	invariant forall k:: forall l:: (0 <= k <= i && i < l < a.Length) ==> a[k] <= a[l];
	invariant forall k:: i < k < a.Length ==> a[j] <= a[k];
	invariant forall k :: 0 <= k < j ==> a[k] <= a[j];
    {
      if (a[j] > a[j + 1])
      {
        var t:int := a[j];
        a[j] := a[j + 1];
        a[j + 1] := t;
      }
      j := j + 1;
    }
    i := i - 1;
  }
}

//referred: Rocco, Maryam, Stack Overflow, Tutorial (Dafny), Chapter 6 (reference Book)
