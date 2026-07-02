class sayDigit:
    def sdigit(self,n,arr):
        if n==0:
            return 0
        digit = n % 10
        n = n // 10
        self.sdigit(n, arr)
        print(arr[digit],end=" ")

Array=['zero','one','two','three','four','five','six','seven','eight','nine']
sayDigit().sdigit(412, Array)