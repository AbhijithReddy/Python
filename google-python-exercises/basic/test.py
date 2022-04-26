#!/usr/bin/env python
def front_x(words):
  # +++your code here+++
  x_list = [element for element in words if element[0] == 'x']
  y_list = [element for element in words if element not in x_list]
  print([x for x in x_list])
  print([y for y in y_list])
  print([w for w in words])
  return sorted(x_list) + sorted(y_list)

def twoSum(arr, target,exclude):
  result = []
  s = {}
  for i in range(len(arr)):
    if i == exclude: 
      continue
    else:
      complement = target - arr[i]
      if complement in s:
        result.append([i, s[complement]])
        break
      else:
        s[arr[i]] = i
  return result

def addTwoNumbers(one: list[int], two: list[int]):
  i, j = 1, 1
  m, n = 0, 0
  for x in range(len(one)):
    if i <= len(one):
      m += one[-i]*pow(10, x)
      i+=1
  for y in range(len(two)):
    if j <= len(two):
      n += two[-j]*pow(10, y)
      j+=1
  sm = m+n
  result = [int(digit) for digit in str(sm)]
  return result

def isPalindrome(s: str) -> bool:
  ln = len(s)
  lt, rt = int(ln/2 - 1), int(-(ln/2))
  while lt >= 0:
    if s[lt] == s[rt]:
      lt, rt = lt-1, rt+1
      continue
    else: 
      return bool(False)
  return bool(True)

def longestPalindrome(s: str) -> str:
  ln = len(s)
  hstry = {}
  result = ""
  maxlength = 0
  for index, element in enumerate(s):
    if element in hstry:
      if ln > 1 and element == s[index-1]:
        lt, rt = index-1, index
        while (lt >= 0 and rt < ln) and s[lt] == s[rt]:
          if (rt-lt+1) > maxlength:
            maxlength = rt-lt+1
            result = s[lt: rt+1]
            lt, rt = lt-1, rt+1
          else: break
            # continue
      elif ln > 2 and element == s[index-2]:
        lt, rt = index-2, index
        while (lt >= 0 and rt < ln) and s[lt] == s[rt]:
          if(rt-lt+1) > maxlength:
            maxlength = rt-lt+1
            result = s[lt: rt+1]
            lt, rt = lt-1, rt+1
          else: break
            # continue
    hstry[element] = index
  return result

def longestPalindromeSubstring(s: str) -> str:
  ln = len(s)
  result = ""
  maxlength = 0
  for index, element in enumerate(s):
    lt, rt = index, index # odd case
    while lt >= 0 and rt < ln and s[lt] == s[rt]:
      if (rt-lt+1) > maxlength:
        maxlength = rt-lt+1
        result = s[lt+1: rt]
        lt, rt = lt-1, rt+1
      else:
        break
    lt, rt = index, index+1 # even case
    while lt >= 0 and rt < ln and s[lt] == s[rt]:
      if(rt-lt+1) > maxlength:
        maxlength = rt-lt+1
        result = s[lt+1: rt]
        lt, rt = lt-1, rt+1
      else:
        break
  return result

def convert(s: str, numRows: int) -> str:
  tmp = []
  for e in range(numRows):
    tmp.append("")
  result = ""
  i = 0
  ln = len(s)
  while i < ln:
    k = 0
    while i < ln and k < numRows-1:
      tmp[k] += s[i]
      k += 1
      i += 1
    l = numRows-1
    tmp[l] += s[i]
    i += 1
    while i < ln and l:
      tmp[l-1] += s[i]
      l -= 1
      i += 1       
  # return result.join(tmp)
  return tmp

def loopUntill(i, n):
  y = 0
  step = 1
  for x in range(i):
    print(y)
    if y == 0:
      step = 1
    elif y == n - 1:
      step = -1
    y += step
  
# def reverseInt(x: int) -> int:
#   int_max = pow(2, 31) - 1
#   int_min = -pow(2, 31)
#   if x > int_max or x < int_min: return None
#   sign = 1
#   if x < 0 : sign = -1
#   x_str = str(abs(x))
#   x_rev_str = x_str[::-1]
#   return sign*int(x_rev_str)

def reverseInt(x: int) -> int:
  sign = 1
  if x < 0: sign = -1
  x = abs(x)
  rev_x = 0
  while int(x / 10) > 0:
    rev_x = rev_x * 10 + x % 10
    x = int(x / 10)
  rev_x = rev_x * 10 + x % 10
  return sign * rev_x

def isPalindromeInt(x: int) -> bool:
  int_max = pow(2, 31) - 1
  if x < 0 or x > int_max: return False
  n = x
  rev_x = 0
  while int(n / 10) > 0:
    rev_x = rev_x * 10 + n % 10
    n = int(n / 10)
  rev_x = rev_x * 10 + n % 10
  return (rev_x == x)

def main():
  # front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
  # nums = [1, 2, 3, 3, -4]
  # result = twoSum(nums, -nums[4], 1)
  # flat_list = [element for item in result for element in item]
  # print([i for i in flat_list])
  # print(addTwoNumbers([4, 0, 0, 1], [3, 2, 0]))
  # print(isPalindrome("aba"))
  # print(isPalindrome("abc"))
  # print(isPalindrome("abba"))
  # print(isPalindrome("abcba"))
  # print(isPalindrome("abbc"))
  # print(isPalindrome("abcbd"))

  # print(longestPalindrome("abbba"))
  # print(longestPalindromeSubstring("ababa"))
  # print(longestPalindrome("cabcbad"))
  # print(longestPalindrome("cabcbab"))
  # print(longestPalindrome("dabcbab"))
  # print(longestPalindrome("aabcbdbcb"))

  # print(convert("PAYPALISHIRING", 3))
  # print(loopUntill(10, 3))
  print(isPalindromeInt(-121))
  print(isPalindromeInt(121))

if __name__ == '__main__':
  main()