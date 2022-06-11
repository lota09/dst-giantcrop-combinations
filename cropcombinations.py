#https://docs.google.com/spreadsheets/d/1ZRg6gjt6NLKYTYlmxZTbfOqly5ibl7rqE8T6P99H9uk/edit#gid=0
#https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home
#https://tgd.kr/s/kmb8787/60537885

from itertools import permutations
from itertools import combinations


#두 리스트를 동시에 정렬하는 함수 - 조합리스트의 원래 순서를 최대한 유지시키기위해 삽입정렬 알고리즘 사용
def parallelsort(pivotlst,slavelst):
    for i in range(len(pivotlst)-1):
        j=i
        while(pivotlst[j]>pivotlst[j+1]):
            pivotlst[j],pivotlst[j+1]=pivotlst[j+1],pivotlst[j]
            slavelst[j],slavelst[j+1]=slavelst[j+1],slavelst[j]
            j-=1
            if(j<0):
                break
    return


#리스트 내 중복항목 지우는 함수
def clearidenticals(lst):
    length=len(lst)#리스트의 길이 - 중복항목이 지워짐에따라 줄어듬
    repeatidx=0#기준이 되는 항목의 인덱스
    for item in lst:#item은 기준항목임
        idx=repeatidx+1#동일여부 확인대상이 되는 항목의 인덱스 (범위: 기준항목의 다음항목 ~ 마지막항목)
        while(idx<length):
            while(lst[repeatidx]==lst[idx]):#삭제한 자리에 또 동일항목이 있을수 있으므로 while문
                del lst[idx]
                length-=1#삭제할때마다 리스트의 길이는 줄어듬
                if(not idx<length):#리스트 마지막 항목을 삭제한경우 list out of range 예방
                    break
            idx+=1
        repeatidx+=1
    return

class crop:
    name=""
    formula=0
    compost=0
    manure=0
    def __init__(self,name="",formula=0,compost=0,manure=0):
        self.name=name
        self.formula=formula
        self.compost=compost
        self.manure=manure

asparagus=crop("아스파라거스",2,-4,2)
carrot=crop("당근",-4,2,2)
corn=crop("옥수수",2,-4,2)
dragonfruit=crop("용과",4,4,-8)
durian=crop("두리안",4,-8,4)
eggplant=crop("가지",2,2,-4)
garlic=crop("마늘",4,-8,4)
onion=crop("양파",-8,4,4)
pepper=crop("고추",4,4,-8)
pomegranate=crop("석류",-8,4,4)
potato=crop("감자",2,2,-4)
pumpkin=crop("호박",-4,2,2)
tomaroot=crop("토마토",-2,-2,4)
watermelon=crop("수박",4,-2,-2)
#양분 요구치가 동일한 작물
eggplantpotato=crop("가지/감자",2,2,-4)
garlicdurian=crop("마늘/두리안",4,-8,4)
onionpomegranate=crop("양파/석류",-8,4,4)
cornasparagus=crop("옥수수/아스파라거스",2,-4,2)
carrotpumpkin=crop("당근/호박",-4,2,2)
pepperdragonfruit=crop("고추/용과",4,4,-8)

dic={
    0:asparagus,
    1:carrot,
    2:corn,
    3:dragonfruit,
    4:durian,
    5:eggplant,
    6:garlic,
    7:onion,
    8:pepper,
    9:pomegranate,
    10:potato,
    11:pumpkin,
    12:tomaroot,
    13:watermelon,
    
    -1:eggplantpotato,
    -2:garlicdurian,
    -3:onionpomegranate,
    -4:cornasparagus,
    -5:carrotpumpkin,
    -6:pepperdragonfruit
    }

autumn=(2,6,7,8,12,-1,-5)
winter=(0,6,10,-5)
spring=(1,3,12,13,-1,-2,-3,-4)
summer=(2,6,12,13,-3,-6)

#비율 입력

try:
    string=input("비율 입력:").split(":")
    ratio=tuple(map(int,string))#ratio=(n,n,n,n...)
except:
    input("입력값을 확인한 후 다시 실행해주십시오.\n종료하려면 아무키나 누르시오...")
    quit()

n=14
r=len(ratio)

#비율 순열 리스트
tmp=list(permutations(ratio,r))
clearidenticals(tmp)#같은것이 있는 순열 - 동일 항목은 지움
ratiolist=tuple(tmp)
del tmp#메모리 절약

#세 양분 균형 확인(true,false 반환)
def isbalanced(citem,ratioitem):
    summation=0
    for i in range(r):
        summation+=(dic[citem[i]].formula)*ratioitem[i]#이때 citem의 항목은 작물의 번호
    if summation!=0:
        return False#한 영양소 요구치가 음수면 이 조합은 이미 실패한 조합
    
    summation=0
    for i in range(r):
        summation+=(dic[citem[i]].compost)*ratioitem[i]
    if summation!=0:
        return False
    
    #위 두 양분이 균형이면 마지막 작물도 균형일것임. 그렇지 않으면 논리적 오류.
    summation=0
    for i in range(r):
        summation+=(dic[citem[i]].manure)*ratioitem[i]
    if summation!=0:
        print("논리적 오류 발생")
        return True#디버깅 목적
    return True
    
def printcombination(season):
    clist=tuple(combinations(season,r))#각 계절 모든 작물조합 clist=((1,2),(1,5),(1,6),(2,5), ... ) (순서는 무시함)
    idx=0#출력시 표시할 조합 번호
    for citem in clist:
        for ratioitem in ratiolist:#각 조합마다 비율의 순서를 달리하여 시도.
            if(isbalanced(citem,ratioitem)):#양분순환이 균형상태인지 확인
                idx+=1
                sortedcitem=list(citem)
                sortedratioitem=list(ratioitem)
                parallelsort(sortedratioitem,sortedcitem)#순서가 뒤죽박죽인 비율리스트를 오름차순으로 정렬, 조합리스트도 비율리스트와 상응하게 정렬
                
                print("%2d."%idx,end=" ")
                for i in range(r-1):
                    print("%s(%d)"%(dic[sortedcitem[i]].name,sortedratioitem[i]),end=" + ")
                print("%s(%d)"%(dic[sortedcitem[r-1]].name,sortedratioitem[r-1]))
    if(idx==0):
        print("-")
    del clist#메모리 절약
    return

print("\n가을")
printcombination(autumn)

print("\n겨울")
printcombination(winter)

print("\n봄")
printcombination(spring)

print("\n여름")
printcombination(summer)
