from maze import *
from exception import *
from stack import *
import copy
class PacMan:
    def __init__(self, grid : Maze) -> None:
        ## DO NOT MODIFY THIS FUNCTION
        self.navigator_maze = grid.grid_representation
    def find_path(self, start: tuple[int,int] , end:tuple[int,int]) -> list[tuple[int, int]]:
        # IMPLEMENT FUNCTION HERE
        temp=copy.deepcopy(self.navigator_maze)
        if (self.navigator_maze[start[0]][start[1]]==1 or self.navigator_maze[end[0]][end[1]]==1):
            raise PathNotFoundException
        
        rows=len(self.navigator_maze)
        columns=len(self.navigator_maze[0])

        answer_stack=Stack()
        answer_stack.push(start)
        found_End=False

        while(answer_stack.top()!=-1):
            if (answer_stack.top()==end):#checking if at end already
                found_End=True
                break
            else:
                x=answer_stack.top()[0]
                y=answer_stack.top()[1]

                temp[x][y]=1

                if(x<rows-1 and temp[x+1][y]==0):
                    answer_stack.push(tuple([x+1,y]))
                    continue
                if(x>0 and temp[x-1][y]==0):
                    answer_stack.push(tuple([x-1,y]))
                    continue
                if(y<columns-1 and temp[x][y+1]==0):
                    answer_stack.push(tuple([x,y+1]))
                    continue
                if(y>0 and temp[x][y-1]==0):
                    answer_stack.push(tuple([x,y-1]))
                    continue

                answer_stack.pop()

        if (not(found_End)):
            raise PathNotFoundException
        else:
            ans_list=[]
            while(answer_stack.top()!=-1):
                ans_list.append(answer_stack.top())
                answer_stack.pop()
            return ans_list[::-1]