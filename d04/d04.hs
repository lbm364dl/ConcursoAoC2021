import qualified Data.Set as S

type Board = [[Int]]
type Nums = [Int]
type Time = Int
type Score = Int

split :: String -> [String]
split = foldr (\c acc@(y:ys) -> if c == ',' then []:acc else (c:y):ys) [[]]

tables :: [String] -> [Board]
tables xs = tables' xs 5
  where 
      tables' [] _ = [[]] 
      tables' (_:xs) 0 = [] : tables' xs 5
      tables' (x:xs) i = let (h:t) = tables' xs (i-1) in ((map read $ words x):h) : t

win :: Nums -> Int -> Board -> (Time, Score)
win xs def b = win' b xs S.empty 0
  where
      win' _ [] _ _ = (def, 0)
      win' b (x:xs) s t
        | check b x newS = (t, x * (score b newS))
        | otherwise = win' b xs newS (t+1)
          where
              newS = S.insert (pos b x) s

pos :: Board -> Int -> (Int, Int)
pos b x = head $ [(i, j) | (xs, i) <- zip b [0..4], (el, j) <- zip xs [0..4], el == x] ++ [(-1, 1)]

check :: Board -> Int -> S.Set (Int, Int) -> Bool
check b x s = checkRow || checkCol
  where
      checkRow = any (\i -> all (\j -> (i,j) `S.member` s) [0..4]) [0..4]
      checkCol = any (\j -> all (\i -> (i,j) `S.member` s) [0..4]) [0..4]

score :: Board -> S.Set (Int, Int) -> Int
score b s = sum [el | (xs, i) <- zip b [0..4], (el, j) <- zip xs [0..4], (i, j) `S.notMember` s]

ans :: [Board] -> Nums -> ([(Int, Int)] -> (Int, Int)) -> Int -> Int
ans b xs cmp def = snd . cmp . map (win xs def) $ b

main = do
    inp <- readFile "input.txt"
    let ls = lines inp
    let nums = map read (split $ head ls) :: [Int]
    let tabs = tables (drop 2 ls)
    putStrLn $ "Star 1: " ++ (show $ ans tabs nums minimum 10000)
    putStrLn $ "Star 2: " ++ (show $ ans tabs nums maximum (-1))
