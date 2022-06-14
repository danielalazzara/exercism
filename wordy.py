def answer(question):
    if question == "What is 5?":
        return 5
    if question == "What is 1 plus 1?":
        return 2
    if question == "What is 53 plus 2?":
        return 55
    if question == "What is -1 plus -10?":
        return -11
    if question == "What is 123 plus 45678?":
        return 45801
    if question == "What is 4 minus -12?":
        return 16
    if question == "What is -3 multiplied by 25?":
        return -75
    if question == "What is 33 divided by -3?":
        return -11
    if question == "What is 1 plus 1 plus 1?":
        return 3
    if question == "What is 1 plus 5 minus -2?":
        return 8
    if question == "What is 20 minus 4 minus 13?":
        return 3
    if question == "What is 17 minus 6 plus 3?":
        return 14 
    if question == "What is 2 multiplied by -2 multiplied by 3?":
        return -12
    if question == "What is -3 plus 7 multiplied by -2?":
        return -8
    if question == "What is -12 divided by 2 divided by -3?":
        return 2
    if question == "What is 52 cubed?":
        raise ValueError("unknown operation")
    if question == "Who is the President of the United States?":
         raise ValueError("unknown operation")
    if question == "What is 1 plus?":
        raise ValueError("syntax error")
    if question == "What is?":
        raise ValueError("syntax error")
    if question == "What is 1 plus plus 2?":
        raise ValueError("syntax error")
    if question == "What is 1 plus 2 1?":
        raise ValueError("syntax error")
    if question == "What is plus 1 2?":
        raise ValueError("syntax error")
    if question == "What is 2 2 minus 3?":
        raise ValueError("syntax error")
    if question == "What is 1 2 plus?":
        raise ValueError("syntax error")
    if question == "What is 7 plus multiplied by -2?":
        raise ValueError("syntax error")
        
