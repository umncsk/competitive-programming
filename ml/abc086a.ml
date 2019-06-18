let pair x y = (x, y)

let judge x y =
  if x * y mod 2 = 0 then
    "Even"
  else
    "Odd"

let () =
  let (x, y) = Scanf.scanf "%d %d" pair in
    Printf.printf "%s\n" (judge x y)
