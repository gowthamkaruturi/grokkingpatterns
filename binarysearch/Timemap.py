class TimeMap:
  def __init__(self) -> None:
    self.dict = {}
  
  def set(self, key: str, value: str, timestamp: int) -> None: 
    if key not in self.dict:
      self.dict[key] =[]
    self.dict[key].append([value,timestamp])
  
  def get(self, key: str, timestamp: int) -> str:
    res =""
    values = self.dict.get(key,[])
    l, r = 0, len(values)-1
    while l <=r:
      mid = (l+r)>>1
      if values[mid][1] <= timestamp:
        l = mid+1
        res = values[mid][0]
      else: 
        r = mid-1
    return res

if __name__ == "__main__":
  tm = TimeMap()
  tm.set("foo","bar",1)
  tm.set("foo","bar",2)
  print(tm.get("foo",5))