def constboard(board):
    print("Current state of the board:\n\n ")
    for i in range(0,9):
        if ((i>0) and (i%3==0)):
            print("\n");
        if (board[i])==0:
            print("_",end =" ");
        if (board[i])==-1:
            print("X",end =" ");
        if (board[i])==1:
            print("O",end =" ")
    print("\n\n");

def User1turn(board):
    pos = input("Enter X's position from [1,2,3.....9]: ");
    pos = int(pos)
    if(board[pos-1]!=0):
        print("This is a Wrong move");
        exit(0);
    board[pos-1]= -1;


def User2turn(board):
    pos = input("Enter O's position from [1,2,3.....9]: ");
    pos = int(pos)
    if (board[pos - 1] != 0):
        print("This is a Wrong move");
        exit(0)
    board[pos-1] = 1;

def minmax(board,player):
    x = analyzeboard(board);
    if (x!=0):
        return (x*player);
    pos = -1
    value = -2;
    for i in range(0, 9):
        if (board[i] == 0):
            board[i] = player;
            score = -minmax(board, player*-1);
            board[i] = 0;
            if(score > value):
                value = score;
                pos = i;
    if (pos==-1):
        return 0
    return value ## here we are propogating the value back to the tree to know what's the highest possible value

def Compturn(board):
    pos = -1
    value = -2; #We are taking -2 as the lowest value and it's not possible and we need to find the highestg value to play the comp turn.
    for i in range(0,9):
        if(board[i]==0):
            board[i]=1;   # 1 indicates that comp will play its chance
            score = -minmax(board,-1);
            board[i]= 0; #after getting the minmax score we will remove the O from the place and make it agian empty
            if (score>value):  #comparing the minmax score and and the value we took as -2.
                value = score;
                pos = i;
    board[pos] = 1



def analyzeboard(board):
    Cb = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];

    for i in range(0, 8):
        if (board[Cb[i][0]]!= 0 and
                board[Cb[i][0]] == board[Cb[i][1]] and
                board[Cb[i][0]] == board[Cb[i][2]]):
            return board[Cb[i][0]];


    return 0;


def main():
    choice = int(input("enter 1 for single player,2 for multiplayer:"));
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0];
    if choice==1:
        print("Computer:0 Vs. You:X");
        player = int(input("enter to play 1(st) or 2(nd): "));
        for i in range(0,9):
            if(analyzeboard(board)!=0):
                # analyzeboard is a function to tell us someone has won or it is a draw at every step of the game.
                break;
            if((i + player)%2==0):
                Compturn(board);
            else:
                constboard(board);
                #constboard is a function which will show the current status of the board
                User1turn(board);

    else:
        for i in range(0,9):
            if(analyzeboard(board)!=0):
                 break;
            if(i%2==0):
                constboard(board)
                User1turn(board);
            else:
                constboard(board);
                User2turn(board);

    x = analyzeboard(board);
    if x == 0:
        constboard(board);
        print("DRAW!!!")

    if x == 1:
        constboard(board);
        print("Player O wins!! X looses!")

    if x == -1:
        constboard(board);
        print("Player X wins!! O looses!");


print(main())