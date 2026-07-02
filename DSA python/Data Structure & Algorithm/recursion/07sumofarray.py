class Summ:
    def add(self, arr, length, total, n):
        if length == 0:
            return total
        total = total+arr[n]
        return self.add(arr, length-1, total, n+1)

arr = [2, 3, 5, 55]
ans = Summ().add(arr, len(arr), 0, 0)
print(ans)
