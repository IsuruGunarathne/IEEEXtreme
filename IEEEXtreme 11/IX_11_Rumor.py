from math import log2

def main():
    n = int(input())    
    for i in range(n):
        a,b = map(int,input().split())
        if a == b:
            print(0)
            continue
        else:
            depthA = depth(a)
            depthB = depth(b)
        
            if depthA > depthB:
                larger = a
                smaller = b
                while depth(larger) > depthB:
                    larger = larger//2
                # now larger is at the same level as smaller
                # divide both larger and smaller until they are the same value;
                # i.e. they are the same node
                # caculate the depth of that node
                # answer is (depthA - depth of that node) + (depthB - depth of that node)
                while larger != smaller:
                    larger = larger//2
                    smaller = smaller//2
                print(depthA+depthB-2*depth(larger))
    
            else:
                larger = b
                smaller = a
                while depth(larger) > depthA:
                    larger = larger//2
                while larger != smaller:
                    larger = larger//2
                    smaller = smaller//2
                print(depthA+depthB-2*depth(larger))
            
def depth(node):
    return int(log2(node))
        
if __name__ == '__main__':
    main()