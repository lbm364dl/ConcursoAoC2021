import qualified Data.Sequence as S
import Data.Bits

mostCommon :: [S.Seq Int] -> Int -> Int
mostCommon xs j = fromEnum (2 * s >= n)
  where
      n = length xs
      s = sum [x `S.index` j | x <- xs]

iter :: Int -> [S.Seq Int] -> Int -> [S.Seq Int]
iter least xs j = filter (\x -> x `S.index` j == which) xs
  where
      which = mostCommon xs j `xor` least

toInt :: S.Seq Int -> Int
toInt = foldl (\acc x -> 2 * acc + x) 0

star1 :: [S.Seq Int] -> Int
star1 xs = x * negX
  where
      m = S.length $ head xs
      x = toInt . S.fromList . foldr (\x acc -> (mostCommon xs x):acc) [] $ [0..m-1]
      negX = (shift 1 m) - 1 - x

star2 :: [S.Seq Int] -> Int
star2 xs = (res 0) * (res 1)
  where
      m = S.length $ head xs
      f least acc x
          | length acc > 1 = iter least acc x
          | otherwise      = acc
      res least = toInt . head . foldl (f least) xs $ [0..m-1]

main = do
    inp <- readFile "input.txt"
    let l = [ S.fromList [read [c] | c <- s] | s <- lines inp]
    putStrLn $ "Star 1: " ++ (show . star1 $ l)
    putStrLn $ "Star 2: " ++ (show . star2 $ l)
