class Knight:
    __item_limit = 10 #비공개 클래스 속성

    def print_item_limit(self):
        print(Knight.__item_limit)

if __name__ == "__main__":
    x = Knight() #객체생성
    x.print_item_limit()

    #print(Knight.__item_limit) #에러 외부사용금지