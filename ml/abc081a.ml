let pair x y z = (x, y, z)
let solve x y z = x + y + z

let () =
  let (x, y, z) = 
    Scanf.scanf "%1d%1d%1d" pair
    |> Printf.printf "%d\n" (solve x y z)
