method MergeSort(a1:array<int>) returns (a:array<int>)
  requires a1.Length > 0;
  ensures a != null;
  ensures forall k:: forall l:: 0 <= k < l < a.Length ==> a[k] <= a[l];
{
  a := ms(a1, 0, a1.Length-1);
  return;
}

method ms(a1:array<int>, l:int, u:int) returns (a:array<int>)
  requires a1 != null;
  requires a1.Length > 0;
  requires 0 <= l <= u < a1.Length;

  ensures a.Length == a1.Length;
  ensures forall p:: forall q:: (l <=p < q && q <= u) ==> a[p] <= a[q];
  ensures forall p:: (0 <= p < l || u < p < a.length) ==> a[p] == a1[p];
  decreases u-l;
{
  a := new int[a1.Length];
  assume forall k:: 0 <= k < a1.Length ==> a[k] == a1[k];
  if (l >= u)
  {
    return;
  }
  else
  {
    var m:int := (l + u) / 2;
    a := ms(a, l, m);
    a := ms(a, m+1, u);
    a := merge(a, l, m, u);
    return;
  }
}

method merge(a1:array<int>, l:int, m:int, u:int) returns (a:array<int>)
  requires a1 != null && a1.length > 0;
  requires 0 <= l <= m && m <= u < a1.Length;
  requires forall p:: forall q:: (l <= p < q && q <= m) ==> a1[p] <= a1[q];
  requires forall p:: forall q:: (m+1 <= p < q && q <= u) ==> a1[p] <= a1[q];

  // ensuring the conditions similar to in method ms
  ensures a != null && a.Length == a1.Length;
  ensures forall p:: forall q:: (l <= p < q && q <= u) ==> a[p] <= a[q];
  ensures forall p:: (0 <= p < l || u < p < a.length) ==> a[p] == a1[p];
{
  a := new int[a1.Length];
  assume forall k:: 0 <= k < a1.Length ==> a[k] == a1[k];
  var buf := new int[u-l+1];
  var i:int := l;
  var j:int := m + 1;
  var k:int := 0;

  while (k < u-l+1)
	invariant forall k:: 0 <= k < a1.Length ==> a[k] == a1[k];
	invariant 0 <= k <= u-l+1
	invariant l <= i <= m+1;
	invariant (i-1) + (j - (m+1)) == k;

	invariant forall p:: forall q:: (0 <= p < q && q < k) ==> buf[p] <= buf[q];
	invariant forall p:: forall q:: (0 <= p < k && i <= q <= m) || (0 <= p < k && j <= q <= u) ==> buf[p] <= buf[q];
  {
    if (i > m)
    {
      buf[k] := a[j];
      j := j + 1;
    }
    else if (j > u)
    {
      buf[k] := a[i];
      i := i + 1;
    }
    else if (a[i] <= a[j])
    {
      buf[k] := a[i];
      i := i + 1;
    }
    else
    {
      buf[k] := a[j];
      j := j + 1;
    }
    k := k + 1;
  }

  k := 0;
  while (k < u-l+1)
	invariant 0 <= k <= u-l+1;
	invariant forall p:: ((0 <= p < l) || (u < p < a1.Length)) ==> a[p] == a1[p];
	invariant forall p:: forall q:: (0 <= p < q && q < u-l+1) ==> buf[p] <= buf[q];
	invariant forall p:: l <= p < l+k ==> buf[q-l] == a[q];
	invariant forall p:: forall q:: (l <= p < q && q < l+k) ==> a[q] <= a[r];
  {
    a[l + k] := buf[k];
    k := k + 1;
  }
}

//referred: Rocco, Maryam, Stack Overflow, Tutorial (Dafny)

