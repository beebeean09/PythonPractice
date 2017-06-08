# first
import heapq

def addNum(num,lowers,highers):
  if (not lowers) or (-num > lowers[0]):
    heapq.heappush(lowers,-num)
  else:
    heapq.heappush(highers,num)

def rebalance(lowers,highers):
  bigger = lowers if (len(lowers) > len(highers)) else highers
  smaller = highers if (len(lowers) > len(highers)) else lowers
  if len(bigger) - len(smaller) >= 2:
    heapq.heappush(smaller, -heapq.heappop(bigger))

def getMedian(lowers,highers):
  bigger = lowers if (len(lowers) > len(highers)) else highers
  smaller = highers if (len(lowers) > len(highers)) else lowers
  if len(bigger) > len(smaller):
    return float(abs(bigger[0]))
  else:
    return (float(abs(bigger[0]) + abs(smaller[0])) / 2)

def getMedians(a):
  lowers,highers = [],[]
  for num in a:
    addNum(num,lowers,highers)
    rebalance(lowers,highers)
    print(round(getMedian(lowers,highers),1))

getMedians([1,2,3,4,5,6])

# Second
# if even length, idx and idx + 1
# if odd length, idx at half
#
# median = 0
# length = n
# result = []
# for num in a:
#     result.append(num)
#     if len(result) == 1:
#         print(float(result[0]))
#     elif len(result) % 2 == 0:
#         if len(result) == 2:
#             median = (result[0] + result[1]) / 2
#             print(median)
#         else:
#             half = int(len(result) / 2)
#             half2 = int(half - 1)
#             median = (result[half] + result[half2]) / 2
#             print(median)
#     else:
#         half = int(len(result) / 2)
#         median = result[half]
#         print(float(median))
