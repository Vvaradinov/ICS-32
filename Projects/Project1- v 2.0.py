# Zachary Cloutier 38485403
if __name__ == '__main__':
    from pathlib import Path

    def First_Line()->"Path":
        """Checks if the first input exists and is a directory. Returns True/False"""
        Input_str = input()
        Input = Path(Input_str)
        if Input.exists():
            if Input.is_dir():
                return Input
            else:
                print("ERROR")
                Input = First_Line()
                return Input
        else:
            print("ERROR")
            Input = First_Line()
            return Input

    def Second_Line()->[str]:
        """Asks for second input then checks if input is valid"""
        Second_input = input().strip().split()
        Letter = Second_input[0].upper()
        if Letter in ['N','E','S']:
            if Letter == 'S':
                try:
                    float(Second_input[1])
                    return Second_input
                except:
                    print("ERROR")
                    Second_input = Second_Line()
                    return Second_input
            elif Letter == 'N':
                return Second_input
            elif Letter == 'E':
                return Second_input
        else:
            print("ERROR")
            Second_input = Second_Line()
            return Second_input

    def Third_Line()->str:
        """Asks for input and checks if third input is valid"""
        Third = input().upper().strip()
        if Third in ['P','F','D','T']:
            return Third
        else:
            print("ERROR")
            Third = Third_Line()
            return Third
    def Search_Files (Root:"Path",Search:[str])->list:
        """Executes search in the given directory based on search instructions"""
        Files = []
        if Search[0] == 'N':
            All_files = []
            for child in Root.iterdir():
                try:
                    if child.is_file():
                        All_files.append(child)
                    elif child.is_dir():
                        for item in Child_Search(child):
                            All_files.append(item)
                except:
                    print("Error occured accessing {}".format(child))
            for file in All_files:        
                if Search[1] in str(file):
                    Files.append(file)
        elif Search[0] == 'E':
            All_files = []
            for child in Root.iterdir():
                try:
                    if child.is_file():
                        All_files.append(child)
                    elif child.is_dir():
                        for item in Child_Search(child):
                            All_files.append(item)
                except:
                    print("Error occured accessing {}".format(child))
            for file in All_files:        
                if Search[1] in str(file):
                    Files.append(file)
        elif Search[0] == 'S':
            All_files = []
            for child in Root.iterdir():
                try:
                    if child.is_file():
                        All_files.append(child)
                    elif child.is_dir():
                        for item in Child_Search(child):
                            All_files.append(item)
                except:
                    print("Error occured accessing {}".format(child))
            for file in All_files:        
                if float(Search[1]) < file.stat().st_size:
                    Files.append(file)
        if Files == []:
            print("Search found nothing please enter new inputs")
            Root = First_Line()
            Search = Second_Line()
            Files = Search_Files(Root,Search)
            return Files
        else:
            return Files

    def Child_Search(child:"Path")->list:
        """Recursive function"""
        All_files = []
        try:
            for path in child.iterdir():
                if path.is_dir():
                    for file in Child_Search(path):
                        All_files.append(file)
                elif path.is_file():
                    All_files.append(path)
        except:
            print("Error occured accessing {}".format(path))
        return All_files

    def Take_Action(Results:list,Action:str)->None:
        """Perform specified action"""
        if Action == 'P':
            for file in Results:
                print(str(file))
        elif Action == 'T':
            for file in Results:
                try:
                    file.touch(exist_ok=True)
                except:
                    print("Error occured while accessing {}".format(file))
        elif Action == 'D':
            for file in Results:
                Duplicate = open(str(file)+'.dup', 'w')
                the_file = file.open('r')
                Copy = the_file.read()
                the_file.close()
                Duplicate.write(Copy)
                Duplicate.close()
        elif Action == 'F':
            for file in Results:
                print(str(file))
                Reading = file.open()
                print(Reading.readline().strip())
                Reading.close()
                
                

    Root = First_Line()
    Search = Second_Line()
    Interesting_Files = Search_Files(Root,Search)
    for file in Interesting_Files:
        print(file)
    Action = Third_Line()
    Take_Action(Interesting_Files, Action)

